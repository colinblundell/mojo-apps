[
# Changing the dependencies on //mojo/edk to be relative.
[r'"//(mojo/edk[^"]*")', r'rebase_path("\1, ".", mojo_root)', ['mojo/edk*BUILD.gn', 'mojo/services/public*BUILD.gn', 'mojo/public*BUILD.gn']],
# Adding the public configs.
[r'([ ]+)(sources =.*)', r'\1public_configs = [\n\1  rebase_path("mojo/build/config", ".", mojo_root) + ":mojo_sdk"\n\1]\n\n\1\2', ['mojo/edk*BUILD.gn']],
# Removing the public config from BUILD.gn files that don't use it to avoid
# gn errors.
#[r'[ ]*public_configs = \[ rebase_path\("mojo/build/config", ".", mojo_root\) \+ ":mojo_sdk" \]', '', ["*mojo/services/public/interfaces/content_handler/BUILD.gn", "*mojo/services/public/interfaces/network/BUILD.gn"]],
]
