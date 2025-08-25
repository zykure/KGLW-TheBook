#!/bin/bash

REL_NAME=$(date +'%Y.%m.%d')
REL_TITLE="${REL_NAME}"
REL_FILES="thebook.pdf thebook.epub thebook.mobi"

gh release create "${REL_NAME}" -t "${REL_TITLE}" ${REL_FILES}
