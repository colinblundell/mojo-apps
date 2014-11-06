#!/bin/bash

ROOT_DIR="$(dirname $(realpath $(dirname "${BASH_SOURCE[0]}")))"
BUILD_DIR="$ROOT_DIR/build"
BUILDTOOLS_DIR="$ROOT_DIR/buildtools"
THIRD_PARTY_DIR="$ROOT_DIR/third_party/"
mkdir -p $THIRD_PARTY_DIR

# BODY

# Install the Mojo SDK and shell.

cd $THIRD_PARTY_DIR
rm -rf mojo
git clone https://github.com/colinblundell/mojo-sdk.git mojo
$THIRD_PARTY_DIR/mojo/build/install-build-deps.sh

# Install gsutil (required by download_mojo_shell.py).
cd $THIRD_PARTY_DIR
curl --remote-name https://storage.googleapis.com/pub/gsutil.tar.gz
tar xfz gsutil.tar.gz
rm gsutil.tar.gz

# TODO(blundell): Should this script be provided by the SDK?
cd $ROOT_DIR
$BUILD_DIR/download_mojo_shell.py

# Install and set up the environment for a GN + Ninja build.

# Install gn.
$THIRD_PARTY_DIR/gsutil/gsutil cp gs://chromium-gn/56e78e1927e12e5c122631b7f5a46768e527f1d2 $BUILDTOOLS_DIR/gn
chmod 700 $BUILDTOOLS_DIR/gn

# Build and install ninja.
cd $THIRD_PARTY_DIR
rm -rf ninja
git clone https://github.com/martine/ninja.git -b v1.5.1
./ninja/bootstrap.py
cp ./ninja/ninja $BUILDTOOLS_DIR
chmod 700 $BUILDTOOLS_DIR/ninja

# Copy in the secondary build dir of the Mojo SDK at the right location.
cd $BUILD_DIR
rm -rf secondary
mkdir -p secondary/third_party/mojo
cd secondary/third_party/mojo
cp -r $THIRD_PARTY_DIR/mojo/build/secondary/* .
