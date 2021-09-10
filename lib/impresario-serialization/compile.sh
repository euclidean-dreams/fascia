#!/bin/bash

FLATBUFFERS_SOURCE_FILES="$(find src/ -type f -name "*.fbs" -printf "%p " | xargs)"
# shellcheck disable=SC2086
flatc --cpp --scoped-enums -o compiled/cpp/ -I src/ ${FLATBUFFERS_SOURCE_FILES}
# shellcheck disable=SC2086
flatc --python --scoped-enums -o compiled/python/ -I src/ ${FLATBUFFERS_SOURCE_FILES}

python3 generate_single_header.py
