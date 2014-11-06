mojo-apps
=========

Holds Mojo apps intended to be built in a standalone fashion.

To see it in action, do the following on a Linux64 machine (note: nothing will work on any other OS):

```
$ git clone https://github.com/colinblundell/mojo-apps.git mojo_apps
$ cd mojo_apps
$ ./build/install-build-deps.sh
```

At this point you should be ready to go forward, although I must warn you that that the script for installing build deps doesn't have any error checking.

You can run one of the supported apps:

```
$ ./run_app.sh echo
$ ./run_app.sh apptest
```

You can also change the location that the Mojo SDK is dropped into if you desire by editing build/config/mojo.gni (don't forget the trailing slash!) and then doing the following:

```
$ rm -rf third_party/mojo
$ ./build/install-build-deps.sh
```

This repo has no external dependencies other than those fetched by install-build-deps.sh.
