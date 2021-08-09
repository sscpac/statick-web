# Statick Web Plugins

![Unit Tests](https://github.com/sscpac/statick-web/workflows/Unit%20Tests/badge.svg)
[![PyPI version](https://badge.fury.io/py/statick-web.svg)](https://badge.fury.io/py/statick-web)
[![Codecov](https://codecov.io/gh/sscpac/statick-web/branch/main/graph/badge.svg)](https://codecov.io/gh/sscpac/statick-web)
![Python Versions](https://img.shields.io/pypi/pyversions/statick-web.svg)
![License](https://img.shields.io/pypi/l/statick-web.svg)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
![Daily Downloads](https://img.shields.io/pypi/dd/statick-web.svg)
![Weekly Downloads](https://img.shields.io/pypi/dw/statick-web.svg)
![Monthly Downloads](https://img.shields.io/pypi/dm/statick-web.svg)

This is a set of plugins for [Statick](https://github.com/sscpac/statick) that will discover Web (HTML, CSS, JavaScript)
files and perform static analysis on those files.

Custom exceptions can be applied the same way they are with [Statick exceptions][Exceptions].

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Existing Plugins](#existing-plugins)
  * [Discovery Plugins](#discovery-plugins)
  * [Tool Plugins](#tool-plugins)
* [Contributing](#contributing)
  * [Mypy](#mypy)
  * [Formatting](#formatting)

## Installation

The recommended method to install these Statick plugins is via pip:

```shell
python3 -m pip install statick-web
```

You can also clone the repository and use it locally.

## Usage

Make sure you install all the dependencies from apt/npm.
See the [Actions][Actions] file to see exactly which commands work for various operating systems.
Pay particular attention to which packages are installed locally and globally.

### Pip Install

The most common usage is to use statick and statick-web from pip.
In that case your directory structure will look like the following:

```shell
project-root
 |- web-project
 |- statick-config
```

To run with the default configuration for the statick-web tools use:

```shell
statick web-project/ --output-directory statick-output/ --profile web-profile.yaml
```

### Pip Install and Custom Configuration

There are times when you will want to have a custom Statick configuration.
This is usually done to run a different set of tools than are called out in the default profile, or to add exceptions.
For this case you will have to add the new Statick configuration somewhere.
This example will have custom exceptions in the web-project, such that the directory structure is:

```shell
project-root
 |- web-project
 |- statick-config
     |- rsc
         |- exceptions.yaml
 |- statick-output
```

For this setup you will run the following:

```shell
statick web-project/ --output-directory statick-output/ --user-paths web-project/statick-config/ --profile web-profile.yaml
```

### Source Install and Custom Configuration

The last type of setup will be to have all of the tools available from cloning repositories, not installing from pip.
The directory structure will look like:

```shell
project-root
 |- web-project
 |- statick-config
     |- rsc
         |- exceptions.yaml
 |- statick-output
 |- statick
 |- statick-web
```

Using the example where we want to override the default exceptions with
custom ones in the web-project, the command to run would be:

```shell
./statick/statick web-project/ --output-directory statick-output/ --user-paths statick-web/,web-project/statick-config/ --profile web-profile.yaml
```

## Existing Plugins

### Discovery Plugins

Note that if a file exists without the extension listed it can still be discovered if the `file` command identifies it
as a specific file type.
This type of discovery must be supported by the discovery plugin and only works on operating systems where the `file`
command exists.

File Type | Extensions
:-------- | :---------
css        | `.css`
html       | `.html`
javascript | `.js`

### Tool Plugins

Tool | About
:--- | :----
[eslint][eslint]       | Find and fix problems in your JavaScript code.
[htmllint][htmllint]   | An unofficial html5 linter and validator.
[jshint][jshint]       | JSHint is a community-driven tool that detects errors and potential problems in JavaScript code.
[stylelint][stylelint] | A mighty, modern linter that helps you avoid errors and enforce conventions in your styles.

## Contributing

If you write a new feature for Statick or are fixing a bug,
you are strongly encouraged to add unit tests for your contribution.
In particular, it is much easier to test whether a bug is fixed (and identify
future regressions) if you can add a small unit test which replicates the bug.

Before submitting a change, please run tox to check that you have not
introduced any regressions or violated any code style guidelines.

### Mypy

Statick Web uses [mypy][MyPy] to check that type hints are being followed properly.
Type hints are described in [PEP 484][Pep484] and allow for static typing in Python.
To determine if proper types are being used in Statick Web the following command will show any errors, and create several
types of reports that can be viewed with a text editor or web browser.

```shell
python3 -m pip install mypy
mkdir report
mypy --ignore-missing-imports --strict --html-report report/ --txt-report report src
```

It is hoped that in the future we will generate coverage reports from mypy and use those to check for regressions.

### Formatting

Statick code is formatted using [black][Black].
To fix locally use

```shell
python3 -m pip install black
black src tests
```

[Actions]: .github/workflows/tests.yaml
[Black]: https://github.com/psf/black
[Exceptions]: https://github.com/sscpac/statick/blob/master/GUIDE.md#exceptionsyaml
[MyPy]: http://mypy-lang.org/
[Pep484]: https://www.python.org/dev/peps/pep-0484/
[eslint]: https://eslint.org/
[htmllint]: https://github.com/htmllint/htmllint
[jshint]: https://jshint.com/about/
[stylelint]: https://stylelint.io/
