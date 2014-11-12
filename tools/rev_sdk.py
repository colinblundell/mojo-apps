#!/usr/bin/env python
# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import subprocess
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.join(current_path, "..")

# Evaluate mojo.gni to obtain mojo_root and mojo_third_party_root.
mojo_gni_file = os.path.join(root_path, "build/config/mojo.gni")
execfile(mojo_gni_file)
assert(mojo_root.startswith("//"))
mojo_sdk_dir = os.path.join(mojo_root[2:], "mojo")
assert(mojo_third_party_root.startswith("//"))
mojo_third_party_dir = os.path.join(mojo_third_party_root[2:], "third_party")

dirs_to_clone = {
  # The core SDK.
  "mojo/public" : os.path.join(mojo_sdk_dir, "/public"),

  # The build dependencies of the core SDK.
  "third_party/cython" : os.path.join(mojo_third_party_dir, "cython"),
  "third_party/khronos" : os.path.join(mojo_third_party_dir, "khronos"),
  "build/secondary/testing/gtest" : os.path.join(mojo_sdk_dir, "build/secondary/testing/gtest"),

  # Client apps.
  # TODO(blundell): Copy in stuff for build/.
  "examples/apptest" : "apptest",
  "examples/echo" : "echo",

  # Support for a gn/ninja client build.
  "tools/generate_library_loader" : "tools/generate_library_loader",
}

def system(command):
  return subprocess.check_output(command)

def commit(message):
  subprocess.call(['git', 'commit', '-a', '-m', message])

def rev(source_dir, target_dir):
  os.chdir(source_dir)
  src_commit = system(["git", "show-ref", "HEAD", "-s"]).strip()

  for input_dir, output_dir in dirs_to_clone.iteritems():
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
  #commit("Update mojo sdk to rev " + src_commit)

if len(sys.argv) != 2:
  print "usage: rev_sdk.py <mojo source dir>"
  sys.exit(1)

rev(sys.argv[1], root_path)
