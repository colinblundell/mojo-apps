[
# Changing the dependencies on //mojo/services/public to be relative.
[r'"//mojo/(services/public[^"]*")', r'rebase_path("\1, ".", mojo_services_root)', ['mojo/public*BUILD.gn', 'mojo/edk*BUILD.gn', 'mojo/services/public*BUILD.gn', "*mojom.gni"]],
# Changing the dependencies on //third_party to be relative.
[r'"//(third_party[^"]*")', r'rebase_path("\1, ".", mojo_third_party_root)', ['mojo/services/public*BUILD.gn']],
# Changing the dependencies on //testing to be relative.
[r'"//(testing[^"]*")', r'rebase_path("\1, ".", mojo_third_party_root)', ['mojo/services/public*BUILD.gn']],
# Adding the public configs.
#[r'([ ]+)(sources =.*)', r'\1public_configs = [ rebase_path("mojo/build/config", ".", mojo_root) + ":mojo_sdk" ]\n\1\2', ['mojo/services/public/*BUILD.gn']],
[r'([ ]+)(sources =.*)', r'\1public_configs = [\n\1  rebase_path("services/build/config", ".", mojo_services_root) + ":services"\n\1]\n\n\1\2', ['mojo/services/public/*BUILD.gn']],
# Changing the include paths to be relative.
[r'"mojo/services/public', r'"services/public', ['mojo/services/public*cc', 'mojo/services/public*h', 'mojo/services/public*mojom']],
# Removing the public config from BUILD.gn files that don't use it to avoid
# gn errors.
#[r'[ ]*public_configs = \[ rebase_path\("mojo/build/config", ".", mojo_root\) \+ ":mojo_sdk" \]', '', ["*mojo/services/public/interfaces/content_handler/BUILD.gn", "*mojo/services/public/interfaces/network/BUILD.gn"]],
]
