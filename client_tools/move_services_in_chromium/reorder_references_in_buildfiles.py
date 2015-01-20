#!/usr/bin/python
import os, sys

def main():
  assert len(sys.argv) > 1
  input_files = sys.argv[1:]
  for input_file in input_files:
    if not os.path.exists(input_file):
      continue

    # If not a buildfile, just spit the input back out.
    if not (input_file.endswith("BUILD.gn") or input_file.endswith(".gni") or
            input_file.endswith(".gyp") or input_file.endswith(".gypi")):
      continue

    f = open(input_file)
    mojo_references = []
    within_list = False
    contents = f.readlines()
    f.close()

    sys.stdout = open(input_file, "w")

    for line in contents:
      at_end_of_list = False
      code = line.rstrip("\n")
      if code.endswith("["):
        assert len(mojo_references) == 0, input_file
        within_list = True
        print code
        continue
      elif code.endswith("]") or code.endswith("],"):
        within_list = False
        at_end_of_list = True

      if within_list and code.find("third_party/mojo_services") != -1:
        mojo_references.append(code)
      else:
        if (len(mojo_references) and
            (mojo_references[0] < code or at_end_of_list)):
          assert within_list or at_end_of_list, input_file
          for reference in mojo_references:
            print reference
          mojo_references = []
        print code
    f.close()

if __name__ == '__main__':
  main()
