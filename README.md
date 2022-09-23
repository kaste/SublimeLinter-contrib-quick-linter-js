SublimeLinter-contrib-quick-lint-js
===================================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [quick-lint-js](https://quick-lint-js.com/).


## Installation

SublimeLinter must be installed in order to use this plugin.  Install via [Package Control](https://packagecontrol.io) or `git clone` as usual.

Ensure that `quick-lint-js` is actually installed somewhere on your system. For example,

```
$ winget install quick-lint-js
``` 

on a command line for Windows or

```
$ brew install quick-lint-js
```

on a Mac should do it.  Detailed information can be found [online](https://quick-lint-js.com/install/cli/).

After installing make sure you can actually run it. E.g.

```
$ quick-lint-js --version
```

You don't have to install it globally though, as always put the executable wherever you want and point SublimeLinter to it.  For example, in the global settings:

```
    "linters": {
        "quick-lint-js": {
            "executable": "C:\\Users\\honkytonk\\Downloads\\quick-lint-js\\bin\\quick-lint-js.exe"
        },
```



