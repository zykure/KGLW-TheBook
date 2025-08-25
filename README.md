# KGLW - TheBook

This e-book collects all lyrics from the Australian band **King Gizzard & the Lizard Wizard**.

<img src="./teaser-image.jpg" alt="Teaser image" width="400"/>

I started this project in June 2025 because I wanted to read Gizz lyrics on my e-book reader while listening to their music.
The included songs are grouped by album, and albums are added in chronological order (oldest first.)
There is also a song index at the end of the document that lists all songs in alphabetical order regardless of album,
and a word index that references selected words that are reoccuring throughout the lyrics.

## Download

You can download the latest version of the e-book in the following formats. EPUB and MOBI should work on most e-book reader devices.

[:arrow_forward:**PDF**](https://github.com/zykure/KGLW-TheBook/raw/refs/heads/main/thebook.pdf)

[:arrow_forward:**EPUB**](https://github.com/zykure/KGLW-TheBook/raw/refs/heads/main/thebook.epub)

[:arrow_forward:**MOBI**](https://github.com/zykure/KGLW-TheBook/raw/refs/heads/main/thebook.mobi)

Alternatively, head to the [Releases](https://github.com/zykure/KGLW-TheBook/releases) page to download the latest or an earlier version.

## Copyright

All artwork and lyrics are copyright by King Gizzard & the Lizard Wizard and the respective authors.\
See [kinggizzardandthelizardwizard.com](https://kinggizzardandthelizardwizard.com/) for details.

## Requirements

You can build the e-book yourself from the sources in this repository. Make sure you have the following requirements.

* TexLive or MiKTeX installation with TeX4ht / TeX4ebook support
* LaTeX packages: `geometry, parskip, setspace, relsize, CrimsonPro, fontenc, inputenc, imakeidx, tex4ebook, ifthen, fancyhdr, titlesec, contour, ulem, nowidow, needspace, lastpage, datetime, graphicx, xcolor, hyperref`
  * The `indexing4ht` package from https://github.com/michal-h21/helpers4ht is included here
* Xindy (for indexing support with TeX4ht)
* Calibre (to produce MOBI format for Kindle devices)
* HTML Tidy (for cleaning up HTML files)

Ubuntu one-liner:

```sh
sudo apt install texlive-extra texlive-extra-utils xindy calibre tidy
```

## Building

Download the sources via `git clone` or by downloading a [ZIP archive](https://github.com/zykure/KGLW-TheBook/archive/refs/heads/main.zip).

Then, simply run the build script `build.sh` (Linux) or `build.bat` (Windows).\
This should produce the PDF result from LaTeX, and the EPUB/MOBI converted result using TeX4ht.

## Notes

A big thanks to @michal-h21 for creating the TeX4ebook package: https://github.com/michal-h21/tex4ebook

Shoutout to [kglw.net](https://kglw.net), [weirdoswarm.org](https://weirdoswarm.org), [gizzheads.de](https://gizzheads.de) and the Gizz global community!
