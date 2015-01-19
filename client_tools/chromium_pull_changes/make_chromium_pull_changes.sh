#!/bin/bash
SCRIPT_DIR="$(realpath $(dirname "${BASH_SOURCE[0]}"))"
CHROMIUM_SRC_DIR=$1

cd $CHROMIUM_SRC_DIR
echo "Moving code from Mojo public repo to live under //third_party/mojo"
rm -rf third_party/mojo
mkdir -p third_party/mojo/src/mojo
#mkdir -p third_party/mojo/services
git mv mojo/public third_party/mojo/src/mojo/public
git mv mojo/edk third_party/mojo/src/mojo/edk
git mv mojo/mojo_public.gyp third_party/mojo
git mv mojo/mojo_edk.gyp third_party/mojo
git mv mojo/mojo_edk_system_impl.gypi third_party/mojo
git mv mojo/mojo_edk_tests.gyp third_party/mojo
git mv mojo/mojo_variables.gypi third_party/mojo
git mv mojo/mojom_bindings_generator.gypi third_party/mojo
git mv mojo/mojom_bindings_generator_explicit.gypi third_party/mojo
git mv mojo/mojom_bindings_generator_variables.gypi third_party/mojo
#git mv mojo/services/public third_party/mojo/services/public
#echo "Applying mojo_gni.patch"
#git apply $SCRIPT_DIR/mojo_gni.patch
$CHROMIUM_SRC_DIR/tools/git/mffr.py -fi $SCRIPT_DIR/search_and_replace_changes.py
# NOTE: The following two fixes have been made Mojo-side and can be eliminated
# once Mojo is rolled into Chromium again.
#echo "Applying edk_js_test patch"
#git apply $SCRIPT_DIR/edk_js_test.patch
#echo "Applying mojo_public_buildfiles patch"
#git apply $SCRIPT_DIR/mojo_public_buildfiles.patch
# NOTE: The following patch needs to land in Mojo and then get rolled into
# Chromium.
# UPDATE: Currently I've commented out the application of this patch because I
# did an experiment where I rolled in a version of the Mojo code that had this
# patch applied.
#echo "Applying download_shell_binary patch"
#git apply $SCRIPT_DIR/download_shell_binary.patch

#echo "Applying chrome_test patch"
#git apply $SCRIPT_DIR/chrome_test.patch
# NOTE: The following 2 fixes are in course of being submitted as separate
# patches.
#git apply $SCRIPT_DIR/nacl_ppapi_changes.patch
#git apply $SCRIPT_DIR/athena_deps.patch
#echo "Applying html_viewer patch"
#git apply $SCRIPT_DIR/html_viewer.patch

#echo "Applying mojom_bindings_generator_explicit patch"
#git apply $SCRIPT_DIR/mojom_bindings_generator_explicit.patch
#echo "Applying gypfile_references_to_logging_files.patch"
#git apply $SCRIPT_DIR/gypfile_references_to_logging_files.patch

# The following patches are all part of this CL and will land in the CL.
echo "Applying add_landmine.patch"
git apply $SCRIPT_DIR/add_landmine.patch
echo "Applying add_license.patch"
git apply $SCRIPT_DIR/add_license.patch
git add third_party/mojo/LICENSE
git add third_party/mojo/README.chromium
echo "Applying get_mojo_to_build.patch"
git apply $SCRIPT_DIR/get_mojo_to_build.patch
echo "Applying mojo_base_logging_files.patch"
git apply $SCRIPT_DIR/mojo_base_logging_files.patch
echo "Applying gypfile_changes_for_mojo_public_to_build.patch"
git apply $SCRIPT_DIR/gypfile_changes_for_mojo_public_to_build.patch
echo "Applying get_mojo_edk_tests_to_build_in_gyp.patch"
git apply $SCRIPT_DIR/get_mojo_edk_tests_to_build_in_gyp.patch
echo "Applying add_mojo_base_include_dirs.patch"
git apply $SCRIPT_DIR/add_mojo_base_include_dirs.patch
echo "Applying change_mojo_sdk_root_gni.patch"
git apply $SCRIPT_DIR/change_mojo_sdk_root_gni.patch
echo "Applying change_download_mojo_shell.patch"
git apply $SCRIPT_DIR/change_download_mojo_shell.patch
echo "Applying mojo_services_public_gypfile.patch"
git apply $SCRIPT_DIR/mojo_services_public_gypfile.patch
#echo "Applying fix_checkdeps.patch"
#git apply $SCRIPT_DIR/fix_checkdeps.patch
#echo "Adding build/config/mojo.gni"
#git add build/config/mojo.gni
echo "Committing changes"
git commit -am "Changes from make_chromium_pull_changes.sh" > /dev/null

echo "Reordering references in buildfiles"
for f in `git diff --name-only HEAD~1`; do
  ~/mojo_apps/client_tools/chromium_pull_changes/reorder_references_in_buildfiles.py $f
done
git commit -am "make_chromium_pull_changes.sh: Reordered references in buildfiles"
echo "Redoing Mojo pull as a check against inserting Mojo-side changes"
~/mojo/src/mojo/tools/roll/rev_sdk.py $CHROMIUM_SRC_DIR
