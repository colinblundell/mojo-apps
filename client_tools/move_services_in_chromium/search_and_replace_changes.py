[
# Changing the GN dependencies.
[r'(//)mojo/services/([^/]*/public[^"]*")', r'\1third_party/mojo_services/src/\2', ['*BUILD.gn']],
# Changing the include paths.
[r'"mojo/services/([^/]*/public)', r'"third_party/mojo_services/src/\1', ['*cc', '*h', '*mojom']],
# Changing the references to the Mojo services gypfile under //mojo.
[r"'mojo_services_public.gyp", r"'../third_party/mojo_services/mojo_services_public.gyp", ["mojo/*gyp"]],
# Fixing up mojo_services_public.gyp.
[r'(//)mojo/services/([^/]*/public[^ ]*)', r'\1third_party/mojo_services/src/\2', ["*mojo_services_public.gyp"]],
# Change back references to the network service.
[r'third_party/mojo_services/src/network', r'mojo/services/network', ['*']],
[r"\-Iservices", r"-Isrc", ["*mojo_services_public.gyp"]],
[r"'services", r"'src", ["*mojo_services_public.gyp"]],
[r"\.\./third_party", r"..", ["*mojo_services_public.gyp"]],
]
