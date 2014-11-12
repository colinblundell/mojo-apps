[
# Changing the dependencies on //mojo to be relative.
[r'"//(mojo[^"]*")', r'rebase_path("\1, ".", mojo_root)', ['examples*BUILD.gn']],
# Adding the import of //build/config/mojo.gni.
[r'(LICENSE file.)', r'\1\nimport("//build/config/mojo.gni")', ['examples*BUILD.gn']]
]
