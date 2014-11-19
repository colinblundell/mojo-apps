#!/bin/bash
SCRIPT_DIR="$(realpath $(dirname "${BASH_SOURCE[0]}"))"
CHROMIUM_SRC_DIR=$1

cd $CHROMIUM_SRC_DIR
git apply $SCRIPT_DIR/mojo_gni.patch
$CHROMIUM_SRC_DIR/tools/git/mffr.py -fi $SCRIPT_DIR/search_and_replace_changes.py
git apply $SCRIPT_DIR/add_landmine.patch
git apply $SCRIPT_DIR/get_mojo_to_build.patch
git apply $SCRIPT_DIR/get_content_to_build.patch
git apply $SCRIPT_DIR/get_chrome_to_build.patch
git add build/config/mojo.gni
