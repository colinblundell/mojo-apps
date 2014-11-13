#!/bin/bash
SCRIPT_DIR="$(realpath $(dirname "${BASH_SOURCE[0]}"))"
MOJO_SRC_DIR=$1
CHROMIUM_SRC_DIR=$2

cd $MOJO_SRC_DIR
$CHROMIUM_SRC_DIR/tools/git/mffr.py -fi $SCRIPT_DIR/change_gn.py
