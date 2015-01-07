[
# Changing the dependencies on //mojo/public.
[r'("//)(mojo/public[^"]*")', r'\1third_party/mojo/\2', ['*BUILD.gn']],
[r'(\.\./)(mojo/public)', r'\1third_party/mojo/\2', ['*']],
# Changing the dependencies on //mojo/services/public.
#[r'("//)(mojo/services/public[^"]*")', r'\1third_party/\2', ['*BUILD.gn']],
#[r'(\.\./)(mojo/services/public)', r'\1third_party/\2', ['*']],
# Changing the dependencies on //mojo/edk.
[r'("//)(mojo/edk[^"]*")', r'\1third_party/mojo/\2', ['*BUILD.gn']],
[r'(\.\./)(mojo/edk)', r'\1third_party/mojo/\2', ['*']],
# Changing the include paths to be relative.
#[r'"mojo/services/public', r'"services/public', ['*cc', '*h', '*mojom']],
# Changing the references to the Mojo gypfiles from paths not under //mojo.
[r"mojo/mojo_public.gyp", r"third_party/mojo/mojo/mojo_public.gyp", ["*gyp", "*.gypi"]],
[r"mojo/mojo_edk.gyp", r"third_party/mojo/mojo/mojo_edk.gyp", ["*gyp", "*.gypi"]],
[r"mojo/mojo_edk_tests.gyp", r"third_party/mojo/mojo/mojo_edk_tests.gyp", ["*gyp", "*.gypi"]],
[r"(mojo/mojom_bindings_generator.gypi)", r"third_party/mojo/\1", ["*gyp", "*.gypi"]],
[r"(mojo/mojom_bindings_generator_explicit.gypi)", r"third_party/mojo/\1", ["*gyp", "*.gypi"]],
[r"(<\(DEPTH\))/(mojo/public)", r"\1/third_party/mojo/\2", ["*gyp", "*.gypi"]],
# Changing the references to the Mojo gypfiles under //mojo.
[r"'mojo_public.gyp", r"'../third_party/mojo/mojo/mojo_public.gyp", ["mojo/*gyp"]],
[r"'mojo_edk.gyp", r"'../third_party/mojo/mojo/mojo_edk.gyp", ["mojo/*gyp"]],
[r"'mojo_edk_tests.gyp", r"'../third_party/mojo/mojo/mojo_edk_tests.gyp", ["mojo/*gyp"]],
[r"'mojo_variables.gypi", r"'../third_party/mojo/mojo/mojo_variables.gypi", ["mojo/*gyp"]],
[r"'(mojom_bindings_generator.gypi)", r"'../third_party/mojo/mojo/\1", ["mojo/*gyp"]],
# Changing references to ".." to "../.." in the Mojo gypfiles.
[r"\.\.", r"../..", ["third_party/mojo/mojo/*gyp"]],
#[r"'services/public/mojo_services_public.gyp", r"'../third_party/mojo/services/public/mojo_services_public.gyp", ["*gyp"]],
#[r"<\(DEPTH\)/mojo/services/public", r"<(DEPTH)/third_party/mojo/services/public", ["*gyp", "*.gypi"]],
# Changing references to download_shell_binary.py.
[r"(mojo/public/tools/download_shell_binary.py)", r"third_party/mojo/\1", ["*"]],
]
