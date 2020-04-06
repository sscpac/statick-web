# Statick Web Plugins

![Unit Tests](https://github.com/sscpac/statick-web/workflows/Unit%20Tests/badge.svg)
![Black](https://github.com/sscpac/statick-web/workflows/Black%20Formatting/badge.svg)
[![PyPI version](https://badge.fury.io/py/statick-web.svg)](https://badge.fury.io/py/statick-web)
[![Codecov](https://codecov.io/gh/sscpac/statick-web/branch/master/graph/badge.svg)](https://codecov.io/gh/sscpac/statick-web)
![Python Versions](https://img.shields.io/pypi/pyversions/statick-web.svg)
![License](https://img.shields.io/pypi/l/statick-web.svg)
![Daily Downloads](https://img.shields.io/pypi/dd/statick-web.svg)
![Weekly Downloads](https://img.shields.io/pypi/dw/statick-web.svg)
![Monthly Downloads](https://img.shields.io/pypi/dm/statick-web.svg)

This is a set of plugins for [Statick](https://github.com/sscpac/statick) that will discover Web (HTML, CSS, JavaScript)
files and perform static analysis on those files.

The current plugins will discover Web files in a project and can be configured to check those files using

- [eslint](https://eslint.org/)
- [htmllint](https://github.com/htmllint/htmllint)
- [jshint](https://jshint.com/)
- [prettier](https://prettier.io/)
- [stylelint](https://github.com/stylelint/stylelint)

Custom exceptions can be applied the same way they are with
[Statick exceptions](https://github.com/sscpac/statick/blob/master/GUIDE.md#exceptionsyaml).

## Installation

The recommended method to install these Statick plugins is via pip:

    pip install statick-web

You can also clone the repository and use it locally.

## Usage

Make sure you install all the dependencies from apt/npm:

    cat install.txt | xargs sudo apt-get install -y
    cat npm-deps.txt | xargs sudo npm install -g

### Pip Install

The most common usage is to use statick and statick-web from pip.
In that case your directory structure will look like the following:

- doc
  - web-project
  - statick-output

To run with the default configuration for the statick-web tools use:

    statick web-project/ statick-output/ --profile web-profile.yaml

### Pip Install and Custom Configuration

There are times when you will want to have a custom Statick configuration.
This is usually done to run a different set of tools than are called out in the default profile, or to add exceptions.
For this case you will have to add the new Statick configuration somewhere.
This example will have custom exceptions in the web-project, such that the directory structure is:

- doc
  - web-project
    - statick-config
      - rsc
        - exceptions.yaml
  - statick-output

For this setup you will run the following:

    statick web-project/ statick-output/ --user-paths web-project/statick-config/ --profile web-profile.yaml

### Source Install and Custom Configuration

The last type of setup will be to have all of the tools available from cloning repositories, not installing from pip.
The directory structure will look like:

- doc
  - web-project
    - statick-config
      - rsc
        - exceptions.yaml
  - statick-output
  - statick
  - statick-web

Using the example where we want to override the default exceptions with
custom ones in the web-project, the command to run would be:

    ./statick/statick web-project/ statick-output/ --user-paths statick-web/,web-project/statick-config/ --profile web-profile.yaml

## Tests and Contributing

If you write a new feature for Statick or are fixing a bug,
you are strongly encouraged to add unit tests for your contribution.
In particular, it is much easier to test whether a bug is fixed (and identify
future regressions) if you can add a small unit test which replicates the bug.

Before submitting a change, please run tox to check that you have not
introduced any regressions or violated any code style guidelines.

### Formatting

Statick code is formatted using [black](https://github.com/psf/black).
To fix locally use

    pip install black
    black src tests
