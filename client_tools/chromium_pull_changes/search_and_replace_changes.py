[
# Changing the dependencies on //mojo/public.
[r'("//)(mojo/public[^"]*")', r'\1third_party/mojo/\2', ['*BUILD.gn']],
[r'(\.\./)(mojo/public)', r'\1third_party/mojo/\2', ['*']],
# Changing the dependencies on //mojo/services/public.
[r'("//)(mojo/services/public[^"]*")', r'\1third_party/\2', ['*BUILD.gn']],
[r'(\.\./)(mojo/services/public)', r'\1third_party/\2', ['*']],
# Changing the dependencies on //mojo/edk.
[r'("//)(mojo/edk[^"]*")', r'\1third_party/mojo/\2', ['*BUILD.gn']],
[r'(\.\./)(mojo/edk)', r'\1third_party/mojo/\2', ['*']],
# Changing the include paths to be relative.
[r'"mojo/services/public', r'"services/public', ['*cc', '*h', '*mojom']],
]
