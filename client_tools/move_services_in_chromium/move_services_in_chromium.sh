#!/bin/bash
SCRIPT_DIR="$(realpath $(dirname "${BASH_SOURCE[0]}"))"

cd ~/chromium/src
echo "Moving code from Mojo public services to live under //third_party/mojo_services"
rm -rf third_party/mojo/services
mkdir -p third_party/mojo_services/src
# NOTE: mojo_sdk_root.gni has to be present in //mojo/services/mojo_sdk_root.gni
# for the network service's public BUILD.gn file to work.
cp mojo/services/mojo_sdk_root.gni third_party/mojo_services/src
git add third_party/mojo_services/src/mojo_sdk_root.gni
git mv mojo/services/public third_party/mojo_services/src/public
for d in accessibility clipboard content_handler geometry gpu input_events native_viewport navigation surfaces view_manager window_manager; do
  git mv mojo/services/$d third_party/mojo_services/src/$d
done

git commit -am "move_services_in_chromium.sh: Move Mojo services code" > /dev/null
commit_after_code_move=`git rev-parse HEAD`

./tools/git/mffr.py -fi $SCRIPT_DIR/search_and_replace_changes.py

# These patches are all part of this CL.
echo "Applying fix_checkdeps"
git apply $SCRIPT_DIR/fix_checkdeps.patch
echo "Applying fix_checkdeps_2"
git apply $SCRIPT_DIR/fix_checkdeps_2.patch
echo "Applying add_license"
git apply $SCRIPT_DIR/add_license.patch
git add third_party/mojo_services/LICENSE
git add third_party/mojo_services/README.chromium
echo "Applying make_owners_file_changes"
git apply $SCRIPT_DIR/make_owners_file_changes.patch
git add third_party/mojo_services/OWNERS
echo "Applying mojo_services_public_config"
git apply $SCRIPT_DIR/mojo_services_public_config.patch
git add mojo/services/public/build/config/BUILD.gn

git commit -am "move_services_in_chromium.sh: Functional changes" > /dev/null

echo "Sorting headers"
./tools/git/for-all-touched-files.py -c "tools/sort-headers.py --force [[FILENAME]]" > /dev/null
git commit -am "move_services_in_chromium.sh: Sort headers" > /dev/null

echo "Reordering references in buildfiles"
for f in `git diff --name-only HEAD~2`; do
  $SCRIPT_DIR/reorder_references_in_buildfiles.py $f
done
git commit -am "move_services_in_chromium.sh: Reorder references in buildfiles" > /dev/null

echo "Restoring //third_party/mojo_services/src to a pristine state"
git checkout $commit_after_code_move -- third_party/mojo_services/src
git commit -am "move_services_in_chromium.sh: Restore Mojo services code to pristine state" > /dev/null

echo "Adding Mojo-side patches that need to be rolled into Chromium before this CL can land"

# These patches are Mojo-side CLs that need to land and roll into
# Chromium and be removed here before this CL can land.
echo "Applying mojo_service_buildfiles"
git apply $SCRIPT_DIR/mojo_service_buildfiles.patch
git commit -am "Mojo-side changes that need to be rolled in to Chromium" > /dev/null
