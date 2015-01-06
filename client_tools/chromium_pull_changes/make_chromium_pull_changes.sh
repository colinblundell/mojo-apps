#!/bin/bash
SCRIPT_DIR="$(realpath $(dirname "${BASH_SOURCE[0]}"))"
#MOJO_SRC_DIR=$1
CHROMIUM_SRC_DIR=$1

cd $CHROMIUM_SRC_DIR
echo "Moving code from Mojo public repo to live under //third_party/mojo"
rm -rf third_party/mojo
mkdir -p third_party/mojo
#mkdir -p third_party/mojo/services
git mv mojo/public third_party/mojo/public
git mv mojo/edk third_party/mojo/edk
git mv mojo/mojo_public.gyp third_party/mojo
git mv mojo/mojo_edk.gyp third_party/mojo
git mv mojo/mojo_edk_system_impl.gyp third_party/mojo
git mv mojo/mojo_edk_tests.gyp third_party/mojo
#git mv mojo/services/public third_party/mojo/services/public
#echo "Applying mojo_gni.patch"
#git apply $SCRIPT_DIR/mojo_gni.patch
$CHROMIUM_SRC_DIR/tools/git/mffr.py -fi $SCRIPT_DIR/search_and_replace_changes.py
# NOTE: The following two fixes have been made Mojo-side and can be eliminated
# once Mojo is rolled into Chromium again.
echo "Applying edk_js_test patch"
git apply $SCRIPT_DIR/edk_js_test.patch
echo "Applying mojo_public_buildfiles patch"
git apply $SCRIPT_DIR/mojo_public_buildfiles.patch
# NOTE: The following patch needs to be made in Mojo somehow.
echo "Applying download_shell_binary patch"
git apply $SCRIPT_DIR/download_shell_binary.patch
#echo "Applying chrome_test patch"
#git apply $SCRIPT_DIR/chrome_test.patch
echo "Applying content_public_browser patch"
# NOTE: The following fixe is in course of being submitted as a separate
# patch.
git apply $SCRIPT_DIR/content_public_browser.patch
#echo "Applying html_viewer patch"
#git apply $SCRIPT_DIR/html_viewer.patch

echo "Applying mojom_bindings_generator_explicit patch"
git apply $SCRIPT_DIR/mojom_bindings_generator_explicit.patch
echo "Applying add_landmine.patch"
git apply $SCRIPT_DIR/add_landmine.patch
#echo "Applying gypfile_references_to_logging_files.patch"
#git apply $SCRIPT_DIR/gypfile_references_to_logging_files.patch
echo "Applying get_mojo_to_build.patch"
git apply $SCRIPT_DIR/get_mojo_to_build.patch
#echo "Applying add_mojo_base_include_dirs.patch"
#git apply $SCRIPT_DIR/add_mojo_base_include_dirs.patch
#echo "Applying fix_checkdeps.patch"
#git apply $SCRIPT_DIR/fix_checkdeps.patch
#echo "Adding build/config/mojo.gni"
#git add build/config/mojo.gni
git commit -am "Changes from make_chromium_pull_changes.sh"
#echo "Updating Mojo pull"
#cd $MOJO_SRC_DIR
#./mojo/tools/roll/rev_sdk.py $CHROMIUM_SRC_DIR
