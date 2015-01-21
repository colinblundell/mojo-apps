#!/bin/bash
SCRIPT_DIR="$(realpath $(dirname "${BASH_SOURCE[0]}"))"

cd ~/chromium/src
echo "Moving code from Mojo public services to live under //third_party/mojo_services"
rm -rf third_party/mojo/services
mkdir -p third_party/mojo_services/src
# NOTE: mojo_sdk_root.gni has to be prenent in //mojo/services/mojo_sdk_root.gni
# for the network service's public BUILD.gn file to work.
cp mojo/services/mojo_sdk_root.gni third_party/mojo_services/src
git add third_party/mojo_services/src/mojo_sdk_root.gni
git mv mojo/mojo_services_public.gyp third_party/mojo_services
git mv mojo/services/public third_party/mojo_services/src/public
for d in accessibility clipboard content_handler geometry gpu input_events native_viewport navigation surfaces view_manager window_manager; do
  git mv mojo/services/$d third_party/mojo_services/src/$d
done
# Note: The network service has an impl that belongs in Chromium and thus should
# stay where it is.
#mkdir third_party/mojo_services/src/network
#git mv mojo/services/network/public third_party/mojo_services/src/network/public

git commit -am "move_services_in_chromium.sh: Move Mojo services code"
commit_after_code_move=`git rev-parse HEAD`

./tools/git/mffr.py -fi $SCRIPT_DIR/search_and_replace_changes.py

# These patches are all part of this CL.
echo "Applying fix_checkdeps"
git apply $SCRIPT_DIR/fix_checkdeps.patch
echo "Applying add_license"
git apply $SCRIPT_DIR/add_license.patch
git add third_party/mojo_services/LICENSE
git add third_party/mojo_services/README.chromium
echo "Applying make_owners_file_changes"
git apply $SCRIPT_DIR/make_owners_file_changes.patch
git add third_party/mojo_services/OWNERS
echo "Applying mojo_services_public_network"
git apply $SCRIPT_DIR/mojo_services_public_network.patch

# This patch should be replaced by having this script move
# network_service_root.gni to //third_party/mojo_services/src once
# the gni file exists on origin/master in Chromium.
echo "Applying network_service_root"
git apply $SCRIPT_DIR/network_service_root.patch

# These patches are separate Chromium CLs that can be removed once
# they land in Chromium.
echo "Applying network_service_buildfile"
git apply $SCRIPT_DIR/network_service_buildfile.patch

# These patches are Mojo-side CLs that need to land and roll into
# Chromium and then can be removed here.
echo "Applying mojo_service_buildfiles"
git apply $SCRIPT_DIR/mojo_service_buildfiles.patch

git commit -am "move_services_in_chromium.sh: Functional changes" > /dev/null

echo "Sorting headers"
./tools/git/for-all-touched-files.py -c "tools/sort-headers.py --force [[FILENAME]]" > /dev/null
git commit -am "move_services_in_chromium.sh: Sort headers" > /dev/null

echo "Reordering references in buildfiles"
for f in `git diff --name-only HEAD~2`; do
  $SCRIPT_DIR/reorder_references_in_buildfiles.py $f
done
git commit -am "move_services_in_chromium.sh: Reorder references in buildfiles"
#echo "Redoing Mojo pull as a check against inserting Mojo-side changes"
#~/mojo/src/mojo/tools/roll/rev_sdk.py $CHROMIUM_SRC_DIR

echo "Restoring //third_party/mojo_services/src to a pristine state"
git checkout $commit_after_code_move -- third_party/mojo_services/src
git commit -am "move_services_in_chromium.sh: Restore Mojo services code to pristine state"
