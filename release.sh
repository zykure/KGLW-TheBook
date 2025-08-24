#!/bin/bash

REL_NAME=$(date +'%Y.%m.%d')
REL_FILES="thebook.pdf thebook.epub thebook.mobi"

REL_TITLE="${REL_NAME}"
REL_NOTES=""

gh release create ${REL_NAME} -t ${REL_TITLE} -n ${REL_NOTES} ${REL_FILES}
