#!/usr/bin/env python3

import json
import re
import sys

########################################

# Regex to find LaTeX comments
COMMENT_REGEX = re.compile(r'%(.*)$', re.DOTALL)

# Regex to find LaTeX commands
COMMAND_REGEX = re.compile(r'\\([A-Za-z]+)(\[.*\])?\{(.*?)\}', re.MULTILINE | re.DOTALL)

# Regex to split lines into segments
SPLIT_REGEX = re.compile(r'([.:;:…?!\(\)])')

# Replacement table for LaTeX symbols (for song titles, etc.)
SYMBOL_REPLACEMENTS = {
    '\\': '',
    '\$': '$',
    '\&': '&',
    "``": '',
    "''": '',
    "--": '-',
}

# Extended replacement table for LaTeX symbols (for lyrics lines)
SYMBOL_REPLACEMENTS_ALL = {
    '(': '',
    ')': '',
}

def replace_symbols(text: str, replace_all: bool = False):
    """Replace special characters in text.

    Example:
        replace_symbols("``Hello world.'' \\") -> "Hello world."
        replace_symbols("Hello (world.)", replace_all=True) -> "Hello world."
    """
    replacements = SYMBOL_REPLACEMENTS
    if replace_all:
        replacements.update(SYMBOL_REPLACEMENTS_ALL)
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text.strip()

def split_line(text: str, keep_delim: bool = False):
    """Split line of text into segments.

    Example:
        split_line("One, Two. Three. Four!") -> ["One, Two", "Three.", "Four!"]
    """
    tok = SPLIT_REGEX.split(text)  # split into segments and separators
    if keep_delim:
        if len(tok) % 2 == 1:
            tok.append("")
        pairs = zip(tok[::2], tok[1::2])  # combine into pairs
        return [ (a+b).strip() for a,b in pairs ]  # merge separators back
    else:
        return [ a.strip() for a in tok[::2] ]

########################################

class Song:
    """Stores song data (collection of lyrics)."""
    def __init__(self, name: str, album: str):
        self.name = name
        self.album_name = album
        self.lyrics = []

    def __str__(self):
        return f"{self.album_name}/{self.name}"

    def add_lyrics(self, text: str):
        self.lyrics.append(text)

    def get_lyrics(self, unique = False):
        if unique:
            return list(set(self.lyrics))
        else:
            return self.lyrics

    def as_dict(self):
        return {
            'name': self.name,
            'album': self.album_name,
            'lyrics': self.lyrics,
        }
        
    def count_lines(self):
        return len(self.lyrics)

########################################

class Album:
    """Stores album data (collection of songs)."""
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def __str__(self):
        return f"{self.name}"

    def add_song(self, song: Song):
        self.songs.append(song)

    def get_songs(self):
        return self.songs

    def as_dict(self):
        return {
            'name': self.name,
            'songs': [ s.as_dict() for s in self.songs ],
        }

    def count_songs(self):
        return len(self.songs)

    def count_lines(self):
        return sum([ s.count_lines() for s in self.songs ])

########################################

class AlbumCollection:
    """Stores collection of albums."""
    def __init__(self):
        self.albums = []

    def __str__(self):
        return f"{self.name}"

    def add_album(self, albums: Album):
        self.albums.append(albums)

    def get_albums(self):
        return self.albums

    def as_dict(self):
        return {
            'albums': [ a.as_dict() for a in self.albums ],
        }

    def count_albums(self):
        return len(self.albums)

    def count_songs(self):
        return sum([ a.count_songs() for a in self.albums ])

    def count_lines(self):
        return sum([ a.count_lines() for a in self.albums ])

########################################

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <outfile.json> <infile1.tex> [<infile2.tex> ...]")
    sys.exit(1)

outfile = sys.argv[1]

album_list = AlbumCollection()

for infile in sys.argv[2:]:

    print(f"Reading input file: {infile}")
    with open(infile, 'r') as f:
        current_album, current_song = None, None
        
        # Iterate through file, line by line
        for line in f.readlines():

            # Remove comments
            line = COMMENT_REGEX.sub('', line)

            # Pre-process first line segment, handle any LaTeX commands
            m = COMMAND_REGEX.search(line)
            while m:
                p0, p1 = m.start(), m.end()
                cmd, opt, arg = m.groups()

                if cmd == 'album':
                    # Update current album : \album{foo}
                    album_name = replace_symbols(arg)
                    current_album = Album(album_name)
                    album_list.add_album(current_album)
                    
                    line = line[:p0] + line[p1:]
                    break
                    
                elif cmd == 'song':
                    # Update current song : \song{foo}
                    song_name = replace_symbols(arg)
                    current_song = Song(song_name, album_name)
                    current_album.add_song(current_song)
                    
                    line = line[:p0] + line[p1:]
                    break
                    
                elif cmd == 'word':
                    # Handle indexed words : \word{foo} -> foo
                    line = line[:p0] + arg.strip() + line[p1:]
                    
                else:
                    # Ignore any other commands
                    line = line[:p0] + line[p1:]

                # Process next line segment
                m = COMMAND_REGEX.search(line)
                continue

            # Must have album and song already defined
            if not current_album or not current_song:
                continue

            # Tokenize line, add segments to song lyrics
            for tok in split_line(line):

                # Replace remaining LaTeX symbols
                tok = replace_symbols(tok, replace_all=True).strip()
                if not tok:
                    continue

                # Update lyrics
                print(f"{current_song}: '{tok}'")
                current_song.add_lyrics(tok)

print()
print("Scan completed.")
print(f"  {album_list.count_albums()} albums.")
print(f"  {album_list.count_songs()} songs.")
print(f"  {album_list.count_lines()} lines of lyrics.")

# Save lyrics database as JSON
print()
print(f"Writing output file: {outfile}")
with open(outfile, 'w') as f:
    data = album_list.as_dict()
    json.dump(data, f, indent=2)

print("Done.")
