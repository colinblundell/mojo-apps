[
# Changing the GN dependencies.
[r'("//)mojo/services/([^/]*/public[^"]*")', r'\1third_party/mojo_services/src/\2', ['*BUILD.gn']],
# Changing the include paths.
[r'"mojo/services/([^/]*/public)', r'"third_party/mojo_services/src/\1', ['*cc', '*h', '*mojom']],
# Changing the references to the Mojo gypfiles from paths not under //mojo.
#[r"mojo/mojo_public.gyp", r"third_party/mojo/mojo_public.gyp", ["*gyp", "*.gypi"]],
#[r"mojo/mojo_edk.gyp", r"third_party/mojo/mojo_edk.gyp", ["*gyp", "*.gypi"]],
#[r"mojo/mojo_edk_tests.gyp", r"third_party/mojo/mojo_edk_tests.gyp", ["*gyp", "*.gypi"]],
#[r"(mojo/mojom_bindings_generator.gypi)", r"third_party/\1", ["*gyp", "*.gypi"]],
#[r"(mojo/mojom_bindings_generator_explicit.gypi)", r"third_party/\1", ["*gyp", "*.gypi"]],
#[r"(<\(DEPTH\))/(mojo/public)", r"\1/third_party/mojo/src/\2", ["*gyp", "*.gypi"]],
## Changing the references to the Mojo gypfiles under //mojo.
#[r"'mojo_public.gyp", r"'../third_party/mojo/mojo_public.gyp", ["mojo/*gyp"]],
#[r"'mojo_edk.gyp", r"'../third_party/mojo/mojo_edk.gyp", ["mojo/*gyp"]],
#[r"'mojo_edk_tests.gyp", r"'../third_party/mojo/mojo_edk_tests.gyp", ["mojo/*gyp"]],
#[r"'mojo_variables.gypi", r"'../third_party/mojo/mojo_variables.gypi", ["mojo/*gyp"]],
#[r"'(mojom_bindings_generator.gypi)", r"'../third_party/mojo/\1", ["mojo/*gyp"]],
## Changing references to ".." to "../.." in the Mojo gypfiles.
#[r"\.\.", r"../..", ["third_party/mojo/*gyp"]],
## Changing references to "'edk" and "'public" in the Mojo gypfiles to be
## preceded by "src/mojo/".
#[r"'edk", r"'src/mojo/edk", ["third_party/mojo/*gyp*"]],
#[r"'public", r"'src/mojo/public", ["third_party/mojo/*gyp*"]],
##[r"'services/public/mojo_services_public.gyp", r"'../third_party/mojo/services/public/mojo_services_public.gyp", ["*gyp"]],
##[r"<\(DEPTH\)/mojo/services/public", r"<(DEPTH)/third_party/mojo/services/public", ["*gyp", "*.gypi"]],
## Changing references to download_shell_binary.py.
#[r"(mojo/public/tools/download_shell_binary.py)", r"third_party/mojo/src/\1", ["*"]],
]
