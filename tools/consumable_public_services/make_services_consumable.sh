#!/bin/bash
SCRIPT_DIR="$(realpath $(dirname "${BASH_SOURCE[0]}"))"
MOJO_SRC_DIR=$1
CHROMIUM_SRC_DIR=$2

cd $MOJO_SRC_DIR
git apply $SCRIPT_DIR/new_buildfiles.patch
$CHROMIUM_SRC_DIR/tools/git/mffr.py -fi $SCRIPT_DIR/change_gn.py
git apply $SCRIPT_DIR/bindings_generation.patch
# TODO(blundell): Talk to brettw about why this patch breaks gn gen.
#git apply $SCRIPT_DIR/python_buildfile.patch
git add mojo/build
git add build/config/mojo.gni
