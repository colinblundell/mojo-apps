#!/usr/bin/python
import sys

def main():
  assert len(sys.argv) > 1
  input_files = sys.argv[1:]
  for input_file in input_files:
    f = open(input_file)
    mojo_references = []
    within_list = False
    for line in f.readlines():
      code = line.strip()
      if code.endswith("["):
        assert len(mojo_references) == 0
        within_list = True
        print code
        continue
      elif code.endswith("]"):
        within_list = False

      if within_list and code.find("third_party/mojo") != -1:
        mojo_references.append(code)
      else:
        if len(mojo_references) and mojo_references[0] < code:
          assert within_list or code.endswith("]")
          for reference in mojo_references:
            print reference
          mojo_references = []
        print code
    f.close()

if __name__ == '__main__':
  main()
