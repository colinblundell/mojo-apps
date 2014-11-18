[
# Changing the dependencies on //mojo to be relative.
[r'"//(mojo/public[^"]*")', r'rebase_path("\1, ".", mojo_root)', ['mojo/public*BUILD.gn', 'mojo/edk*BUILD.gn', 'mojo/services/public*BUILD.gn', "mojo/public*.gni"]],
# Changing the dependencies on //third_party to be relative.
[r'"//(third_party[^"]*")', r'rebase_path("\1, ".", mojo_third_party_root)', ['mojo/public*BUILD.gn', "mojo/public*.gni"]],
# Changing the dependencies on //testing to be relative.
[r'"//(testing[^"]*")', r'rebase_path("\1, ".", mojo_third_party_root)', ['mojo/public*BUILD.gn', "*mojo/public*.gni"]],
# Adding the import of //build/config/mojo.gni.
[r'(LICENSE file.)', r'\1\n\nimport("//build/config/mojo.gni")', ['mojo/public*BUILD.gn', 'mojo/edk*BUILD.gn', 'mojo/services/public*BUILD.gn', "*mojom.gni"]],
# Adding the public config.
[r'([ ]+)(sources =.*)', r'\1public_configs = [ rebase_path("mojo/build/config", ".", mojo_root) + ":mojo_sdk" ]\n\1\2', ['mojo/public*BUILD.gn']],
# Removing the public config from BUILD.gn files that don't use it to avoid
# gn errors.
[r'[ ]*public_configs = \[ rebase_path\("mojo/build/config", ".", mojo_root\) \+ ":mojo_sdk" \]', '', ['*mojo/public/interfaces/bindings/tests/BUILD.gn', "*mojo/public/interfaces/application/BUILD.gn", "*mojo/public/python/BUILD.gn"]],
]
