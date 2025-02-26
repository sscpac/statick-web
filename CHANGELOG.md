# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## v0.4.0 - 2025-02-07

This set of plugins was merged into the main [Statick] repository and Python package.
All future development will happen in that repository.

### Updated

- The Statick dependency was pinned to lower than version 0.12.
  - This will ensure these plugins are not installed in the same space as the main `statick` package.
    Having both packages installed would cause conflicts between plugins.

## v0.3.0 - 2025-01-20

### Added

- Support for Python 3.12 and 3.13.
- Use of `pyproject.toml` instead of `setup.py` and `requirements.txt`.
- Supports new plugin discovery mechanism for the main Statick tool.
  - Switched from yapsy to setuptools for plugin mechanism. (sscpac/statick#508)

### Changed

- Disabled code coverage requirements in CI for now.
  - Unable to get line coverage working with new plugin mechanism.
    Unit tests still work to find problems.
- Rename plugin modules so they are shorter and less redundant.

### Removed

- No longer support Python 3.8.

## v0.2.0 - 2025-01-03

### Changed

- ESLint tool plugin updates.
  - Using new ESLint configuration file format.
    - <https://eslint.org/docs/latest/use/configure/configuration-files>
  - Request JSON output format from tool and update parsing results accordingly.

### Removed

- Removed Python 3.7 support.
- Removed flake8 when running unit tests.

## v0.1.3 - 2023-04-24

### Changed

- Updated publish workflow runner to Ubuntu 22.04 since 18.04 is removed. (#58)

## v0.1.2 - 2023-04-24

### Added

- Ubuntu 22.04 used in continuous integration workflows.
- Python 3.11 used in continuous integration workflows.
- Adding code to handle specific nodejs thrown errors where needed. (#55)

### Changed

- Update GitHub Actions to use latest versions.

### Fixed

- Ensuring that "Cannot find module" thrown errors from nodejs in markdownlint tool plugin cause statick to error. (#55)
- Using different error types (`comment-no-empty` and `block-no-empty` instead of
  `declaration-colon-after-space` and `block-opening-brace-space-before`)
  in stylelint unit tests that will hopefully not be deprecated.
  This fixes a unit test error in Statick tool plugins using recent versions of `stylelint`. (#56)

### Removed

- Ubuntu 18.04 removed from continuous integration workflows.
- Removed deprecated pypi package [codecov](https://github.com/codecov/codecov-python) from Tox configuration. (#56)
  Discussion at: <https://community.codecov.com/t/codecov-yanked-from-pypi-all-versions/4259>.

## v0.1.1 - 2022-10-11

### Changed

- Updated tool plugins to match new structure introduced in sscpac/statick#423.
- Update `inherits_from` usage in configuration file to match new list format.

### Fixed

- Pin flake8<5 and pycodestyle<2.9.0 until <https://github.com/tholo/pytest-flake8/issues/87> is fixed.

## v0.1.0 - 2022-01-04

### Removed

- Drop support for Python 3.6 due to end-of-life of that distribution.
  See <https://endoflife.date/python>.
  To continue using Statick with Python 3.6 [pin the version](https://pip.pypa.io/en/stable/user_guide/)
  used to the `0.0` tags.
  An example is at the discussion at <https://github.com/sscpac/statick/discussions/376>.

## v0.0.7 - 2021-12-21

### Added

- Support for python 3.10 (Thomas Denewiler, @tdenewiler, #36, #42).
- Weekly run of the unit tests.

### Fixed

- Specifying an encoding when calling open (pylint: [W1514](https://pylint.pycqa.org/en/latest/technical_reference/features.html)).
- Updated stylelint configuration to work with v14 and newer, [migration guide](https://github.com/stylelint/stylelint/blob/14.0.0/docs/migration-guide/to-14.md).

### Changed

- Switch codecov-action from v1 to v2 (Thomas Denewiler, @tdenewiler, #38).

## v0.0.6 - 2021-05-28

### Changed

- Switch type hints from comment style to inline style.
- Renaming plugin directories to match Statick's directory structure.
- For testing with Actions, the installed version of Node was upgraded from v10 to v14.
  Node v10 is no longer supported.
  Node v14 is recommended by the developers as it is a long-term support (LTS) release.

### Removed

- Remove testing support for Ubuntu 16.04 and Python 3.5.
  There is no guarantee Statick will work in those environments any longer.

## v0.0.5 - 2021-05-03

This is expected to be the final release that supports Python 3.5.
Ubuntu 16.04 has reached end-of-life status.
The final release of ROS Kinetic has been made.
See <https://github.com/sscpac/statick/discussions/290> for a discussion on Python 3.5 support in Statick.

### Added

- Add support for locally installed eslint configs and plugins.
  Adding `install_dir` config option to specify where eslint's plugins and configs are installed.
  On Ubuntu, locally installed eslint configs and plugins are required for eslint versions >= 6.0.0:
  <https://eslint.org/docs/user-guide/migrating-to-6.0.0#plugins-and-shareable-configs-are-no-longer-affected-by-eslints-location>
- Add support for parsing eslint error lines.

## v0.0.4 - 2021-01-19

### Changed

- Convert use of print() and show tool output flags to the built-in Python logging module. (Thomas Denewiler, @tdenewiler)

## v0.0.3 - 2020-12-22

### Added

- Take advantange of new `DiscoveryPlugin.find_files` function that only walks a package's path once instead of
  in each discovery plugin.
  This should lead to a speed improvement in the discovery phase. (Alexander Xydes, @xydesa)

## v0.0.2 - 2020-04-06

### Added

- Installing all tool rc files with this package.
  Added new separate levels and corresponding profiles for each separate tool.
  Using installed markdownlintrc file instead of copying into this repo.
- Publishing tags to pypi.
- Formatted all code using black. Added Github Action to ensure future commits are consistent with black formatting.
- Using markdownlint statick plugin to check documentation files.

### Changed

- Switched from travis ci to github actions.

### Fixed

- Limit discovery plugins to only find files corresponding to the tools specified. (Thomas Denewiler, @tdenewiler)

## v0.0.1 - 2020-02-14

### Added

- Initial release (Alexander Xydes, @axydes)
