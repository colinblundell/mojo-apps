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
# Changing the references to the gypfiles from the Mojo repo under //mojo.
[r"'public/mojo_public.gyp", r"'../third_party/mojo/mojo/public/mojo_public.gyp", ["*gyp"]],
[r"'edk/mojo_edk.gyp", r"'../third_party/mojo/mojo/edk/mojo_edk.gyp", ["*gyp"]],
[r"'edk/mojo_edk_tests.gyp", r"'../third_party/mojo/mojo/edk/mojo_edk_tests.gyp", ["*gyp"]],
[r"'services/public/mojo_services_public.gyp", r"'../third_party/mojo/services/public/mojo_services_public.gyp", ["*gyp"]],
# Changing the references to the gypfiles from the Mojo repo via DEPTH.
[r"<\(DEPTH\)/mojo/public", r"<(DEPTH)/third_party/mojo/mojo/public", ["*gyp", "*.gypi"]],
[r"<\(DEPTH\)/mojo/edk", r"<(DEPTH)/third_party/mojo/mojo/edk", ["*gyp", "*.gypi"]],
[r"<\(DEPTH\)/mojo/services/public", r"<(DEPTH)/third_party/mojo/services/public", ["*gyp", "*.gypi"]],
# Changing references to download_shell_binary.py.
[r"(mojo/public/tools/download_shell_binary.py)", r"third_party/mojo/\1", ["*"]],
]
