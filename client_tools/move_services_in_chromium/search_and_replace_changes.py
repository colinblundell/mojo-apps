[
# Changing the GN dependencies.
[r'(//)mojo/services/([^/]*/public[^"]*")', r'\1third_party/mojo_services/src/\2', ['*BUILD.gn']],
# Changing the include paths.
[r'"mojo/services/([^/]*/public)', r'"third_party/mojo_services/src/\1', ['*cc', '*h', '*mojom']],
# Change back references to the network service.
[r'third_party/mojo_services/src/network', r'mojo/services/network', ['*']],
]
