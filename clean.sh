#!/bin/bash

ENDINGS="
*.opf
*.aux
*.4ct
*.4tc
*.idv
*.idx
*.ilg
*.ind
*.lg
*.log
*.ncx
*.out
*.tmp
*.toc
*.xdy
*.xref
thebook-*/
thebook.css
thebook.dvi
thebook.out.ps
thebook*.html
"

for end in ${ENDINGS}; do
    rm -rv -- "${end}" 2>/dev/null
done
