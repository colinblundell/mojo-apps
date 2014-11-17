#!/bin/bash
SCRIPT_DIR="$(realpath $(dirname "${BASH_SOURCE[0]}"))"
MOJO_SRC_DIR=$1
CHROMIUM_SRC_DIR=$2

cd $MOJO_SRC_DIR
git apply $SCRIPT_DIR/new_buildfiles.patch
$CHROMIUM_SRC_DIR/tools/git/mffr.py -fi $SCRIPT_DIR/change_gn.py
git apply $SCRIPT_DIR/bindings_generation.patch
git apply $SCRIPT_DIR/mojo_gni.patch
git apply $SCRIPT_DIR/add_missing_dependencies.patch
git apply $SCRIPT_DIR/presubmit_fixup.patch
git apply $SCRIPT_DIR/mojom_public_configs.patch
git apply $SCRIPT_DIR/mojom_import_dirs.patch
git apply $SCRIPT_DIR/fixup_mojom_gni_comments.patch
git apply $SCRIPT_DIR/mojo_gni_import_dirs.patch
git add mojo/services/build
git add mojo/services/public/DEPS
