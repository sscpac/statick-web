# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## Unreleased

### Added

### Fixed

### Removed

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
