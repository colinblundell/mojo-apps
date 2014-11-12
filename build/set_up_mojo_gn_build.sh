#!/bin/bash
# Performs required setup to build the Mojo SDK with gn.
MOJO_SDK_ROOT=$1
ROOT_DIR="$(dirname $(realpath $(dirname "${BASH_SOURCE[0]}")))"
BUILD_DIR="$ROOT_DIR/build"

# Copy in the secondary build dir of the Mojo SDK at the right location.
rm -rf $BUILD_DIR/secondary/$MOJO_SDK_ROOT
mkdir -p $BUILD_DIR/secondary/$MOJO_SDK_ROOT/mojo
cd $BUILD_DIR/secondary/$MOJO_SDK_ROOT/mojo
cp -r $ROOT_DIR/$MOJO_SDK_ROOT/mojo/build/secondary/* .
