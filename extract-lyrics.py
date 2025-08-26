#!/usr/bin/env python3

import json
import re
import sys

########################################

COMMENT_REGEX = re.compile(r'%(.*)$')
COMMAND_REGEX = re.compile(r'\\([A-Za-z]+)(\[(.*)\])?\{(.*?)\}', re.MULTILINE | re.DOTALL)
SPLIT_REGEX = re.compile(r'[.:…?!]')

CHAR_REPLACEMENTS = {
    '\\': '',
    '\$': '$',
    '\&': '&',
    #',': '',
    #'.': '',
    #';': '',
    #':': '',
    '…': '',
    '?': '',
    '!': '',
    '(': '',
    ')': '',
    "``": '',
    "''": '',
}

def replace_chars(text: str):
    for k, v in CHAR_REPLACEMENTS.items():
        text = text.replace(k, v)
    return text

def split_line(text: str):
    return SPLIT_REGEX.split(text)

########################################

class Song:
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

########################################

class Album:
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

########################################

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <outfile.json> <infile1.tex> [<infile2.tex> ...]")
    sys.exit(1)
    
outfile = sys.argv[1]

album_list = []

for infile in sys.argv[2:]:
    
    print(f"Reading input file: {infile}")
    with open(infile, 'r') as f:
        current_album, current_song = None, None
        for line in f.readlines():
            
            line = COMMENT_REGEX.sub('', line)
            
            # process first line segment
            m = COMMAND_REGEX.search(line)
            while m:
                p0, p1 = m.start(), m.end()
                cmd, _, opt, arg = m.groups()

                if cmd == 'album':
                    # update current album name
                    album_name = replace_chars(arg)
                    current_album = Album(album_name)
                    album_list.append(current_album)
                    line = line[:p0] + line[p1:]
                    break
                elif cmd == 'song':
                    # update current song name
                    song_name = replace_chars(arg)
                    current_song = Song(song_name, album_name)
                    current_album.add_song(current_song)
                    line = line[:p0] + line[p1:]
                    break
                elif cmd == 'word':
                    # replace \word{foo}  -> foo
                    line = line[:p0] + arg.strip() + line[p1:]
                else:
                    # ignore any other commands
                    line = line[:p0] + line[p1:]
                    
                m = COMMAND_REGEX.search(line)
                continue

            # process line
            for line in split_line(line):

                line = replace_chars(line).strip()
                if not line:
                    continue

                if not current_album or not current_song:
                    continue
                    
                print(f"{current_song}: '{line}'")
                current_song.add_lyrics(line)
                
                
print(f"Writing output file: {outfile}")
with open(outfile, 'w') as f:
    data = {
        'albums': [ a.as_dict() for a in album_list ],
    }
    json.dump(data, f, indent=2)
