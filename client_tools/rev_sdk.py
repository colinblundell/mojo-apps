#!/usr/bin/env python
# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import subprocess
import sys

sdk_dirs_to_clone = [
  # The core SDK.
  "mojo/public",
]

services_dirs_to_clone = [
  # Public services.
  "mojo/services/public",
  #"mojo/services/build/config",
]

client_dirs_to_clone = [
  # Client apps.
  #"examples/apptest",
  "examples/echo",
  #"examples/sample_app",

  # Dependencies of client apps.
#  "base",
#  "crypto",
#  "gin",
#  "gpu",
#  "net",
#  "sdch",
#  "skia",
  # NOTE: Contains dependencies of the Mojo SDK as well.
#  "testing",
  # NOTE: Contains dependencies of the Mojo SDK as well.
#  "third_party",
#  "ui",
#  "url",
#  "v8",

  # Support for a gn/ninja client build.
  "build",
  "tools",
]

# Directories not tracked by git that should be copied in.
client_dirs_to_copy = [
  "testing/gtest",
  "third_party/angle",
  "third_party/boringssl/src",
  "third_party/mesa/src",
  "third_party/skia",
  "third_party/yasm/source/patched-yasm",
]

def system(command):
  return subprocess.check_output(command)

def commit(message):
  subprocess.call(['git', 'commit', '-a', '-m', message])

def rev(source_dir, target_dir, dirs_to_clone):
  os.chdir(source_dir)
  src_commit = system(["git", "show-ref", "HEAD", "-s"]).strip()

  for input_dir in dirs_to_clone:
    output_dir = input_dir 

    # Strip any "services/" prefixes to avoid stutter.
    if output_dir.startswith("services/"):
      output_dir = output_dir[len("services/"):]
    os.chdir(target_dir)
    if os.path.exists(output_dir):
      print "removing directory %s" % output_dir
      system(["git", "rm", "-r", output_dir])
    print "cloning directory %s into %s" % (input_dir, output_dir)

    os.chdir(os.path.join(source_dir, input_dir))
    files = system(["git", "ls-files"])
    for f in files.splitlines():
      dest_path = os.path.join(target_dir, output_dir, f)
      system(["mkdir", "-p", os.path.dirname(dest_path)])
      system(["cp", os.path.join(f), dest_path])
    os.chdir(target_dir)
    system(["git", "add", output_dir])

  os.chdir(target_dir)
  with open("MOJO_SDK_VERSION", "w") as version_file:
    version_file.write(src_commit)
  system(["git", "add", "MOJO_SDK_VERSION"])
  commit("Update mojo sdk to rev " + src_commit)

def copy(source_dir, target_dir, dirs_to_copy):
  os.chdir(target_dir)
  for d in dirs_to_copy:
    output_dir = os.path.join(target_dir, d)
    if os.path.exists(output_dir):
      print "removing directory %s" % output_dir
      system(["rm", "-rf", output_dir])
    system(["cp", "-r", os.path.join(source_dir, d), output_dir])
    system(["rm", "-rf", os.path.join(output_dir, ".git")])
    system(["git", "add", output_dir])
  commit("Update dirs copied in from the Mojo repo")

if len(sys.argv) != 3:
  print "usage: rev_sdk.py <mojo source dir> <chromium source dir>"
  sys.exit(1)

current_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.join(current_path, "..")

mojo_sdk_dir = os.path.join(root_path, "third_party", "mojo", "src")
#assert(mojo_services_root.startswith("//"))
#mojo_services_root = mojo_services_root[2:]
#mojo_services_dir = os.path.join(root_path, mojo_services_root, "services")

mojo_repo_dir = sys.argv[1]
chromium_repo_dir = sys.argv[2]

# Rev the SDK and shell.
client_tools_path = os.path.join(root_path, "client_tools")
rev(mojo_repo_dir, mojo_sdk_dir, sdk_dirs_to_clone)
system([os.path.join(client_tools_path, "download_mojo_shell.py")])

# Rev services.
#rev(mojo_repo_dir, mojo_services_dir, services_dirs_to_clone)

# Update the Mojo build for the new SDK.
#system([os.path.join(mojo_sdk_dir, "build/install-build-deps.sh")])

# Rev client apps.
#system(["cp", os.path.join(root_path, "build/config/mojo.gni"), root_path])
#rev(mojo_repo_dir, root_path, client_dirs_to_clone)
#system(["mv", os.path.join(root_path, "mojo.gni"), os.path.join(root_path, "build/config")])
#commit("Restore mojo.gni")

# Copy in dirs of client apps that aren't tracked in git.
#copy(mojo_repo_dir, root_path, client_dirs_to_copy)

# Update buildfiles of client apps.
#system([os.path.join(chromium_repo_dir, "tools/git/mffr.py"), "-fi", "change_buildfiles.py"])
#commit("Update BUILD.gn files of client apps")
