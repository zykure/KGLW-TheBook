# KGLW - TheBook

This ebook collects all lyrics from the Australian band King Gizzard & the Lizard Wizard.
The include songs are grouped by album, and albums are added in chronological order (oldest first.)
There is also an index at the end of the document that lists all songs in alphabetical order, regardless of album.

## Copyright

All lyrics are copyright by King Gizzard & the Lizard Wizard and the respective authors, as noted in each song.

## Requirements

* TexLive or MiKTeX installation with TeX4ht / TeX4ebook support
* LaTeX packages: `inputenc, fontenc, utopia, imakeidx, fancyhdr, graphicx, xcolor, hyperref`
  * The `indexing4ht` package from https://github.com/michal-h21/helpers4ht is included here
* Xindy (for indexing support with TeX4ht)
* Calibre or Kindlegen (to produce MOBI format for Kindle devices)
* HTML Tidy (for cleaning up HTML files)

Ubuntu one-liner:

```sh
sudo apt install texlive-extra texlive-extra-utils xindy calibre tidy
```

## Building

Simply run the build script `build.sh` (Linux) or `build.bat` Windows.
This should produce the PDF result from LaTeX, and the EPUB/MOBI converted result using TeX4ht.

## Notes

A big thanks to @michal-h21 for creating the TeX4ebook package: https://github.com/michal-h21/tex4ebook

Shoutout to https://kglw.net, https://weirdoswarm.org, https://gizzheads.de and the Gizz global community!

