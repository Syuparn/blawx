# Changelog

Notable changes to Blawx will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
As of v0.2-alpha, this project is attempting to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
While alpha, however, any version changes may cause breaking changes that may not be specifically noted as such.

## [v1.0.3-alpha](https://github.com/Lexpedite/blawx/releases/tag/v1.0.2-alpha) 2022-02-03

### Added
* Blawx reports compiler errors (resolving [#61](https://github.com/Lexpedite/blawx/issues/61))

### Removed
* Admin interface for documentation

## [v1.0.2-alpha](https://github.com/Lexpedite/blawx/releases/tag/v1.0.2-alpha) 2022-02-03

### Changed
* Documentation and default workspaces have been deleted from the database, and are now loaded from
  YAML fixtures in the installation process.

## [v1.0.1-alpha](https://github.com/Lexpedite/blawx/releases/tag/v1.0.1-alpha) 2022-02-03

### Added
* Category Display Block
* `update.sh` Script to stop, rebuild, and run local docker container

### Changed
* Dockerfile loads blawx files from local
* Explanations use language from category display block
* Object declaration blocks use language from category display block
* Dockerfile reorganized to rebuild faster


## [v1.0.0-alpha](https://github.com/Lexpedite/blawx/releases/tag/v1.0.0-alpha) 2022-02-01
v1.0.0-alpha is nearly a complete rewrite of the code, to facilitate two major changes:
* New reasoning engine (from Flora-2 to s(CASP))
* Server-side workspace management

### **Major Version Change**

The move from v0 to v1 indicates there is no compatibility between Blawx code written for v1, and for previous versions.

### Added
* Natural language explanations
* Multiple model responses to queries
* Numerical constraints
* Logical constraints
* Compiler warnings
* Live code generation
* Server side management of workspaces
* User Authentication
* Example workspaces (not modifiable by anonymous users)
* Assumptions, hypothetical reasoning

### Changed
* Code generation has been moved to the client side
* The entire block language has been updated
* The web API uses code stored on the server
* JSON input data schema has changed

### Removed
* Silent variables
* Several Logical statements
* Dates, Times, Durations, and Strings
* Includes
* Data blocks

## [v0.2.4-alpha RC1](https://github.com/Blawx/blawx/releases/tag/v0.2.4-alphaRC1) 2021-01-22
### Added
* Date, Time, Datetime, and Duration Datatypes ([Issue #48](https://github.com/Blawx/blawx/issues/48))
* Date Math Functions
* String Functions
* New Attribute Declarations with Cardinality
* The docker container now includes a Jekyll set of documentation at /docs.
* Silent and unnamed variable blocks.
* Tooltips and help links to all blocks.
* Beginner's Guide in documentation
* Image type hints on method and type selectors
### Changed
* Toolbox reorganized
* Updated reasoner to Flora-2.1RC1 ([Issue #55](https://github.com/Blawx/blawx/issues/55))
* "String" renamed to "Text"
* "True/False" renamed to "Yes/No"
* New String Value Block
  
  **Breaking Change: Workspaces from previous versions using string values will not load.**

* Reimplemented Reasoner
  
  Reasoner responses for small queries will be significantly faster. Reasoner responses will also scale better with hardware. Workspaces or data that take more than 30 seconds of processor time will fail.

* New Object blocks are now created for each Category in the workspace. ([Issue #42](https://github.com/Blawx/blawx/issues/42))
### Fixed
* Allow Long Search Results ([Issue #1](https://github.com/Blawx/blawx/issues/1))
* Stop using sleep in Reasoner.php ([Issue #26](https://github.com/Blawx/blawx/issues/26))
* Queries don't work if they are not at the bottom ([Issue #24](https://github.com/Blawx/blawx/issues/24))

## [v0.2.3-alpha](https://github.com/Blawx/blawx/releases/tag/v0.2.3-alpha) 2020-06-29
### Added
* adding `?load=url` to address for interface will pre-load a .blawx file
  at that url.

## [v0.2.2-alpha](https://github.com/Blawx/blawx/releases/tag/v0.2.2-alpha) 2020-06-06
### Added
* Script for updating running container in development enviroments.
* Start of gh-pages based documentation
* Keyboard navigation.
### Changed
* Implemented custom true/false value block ([Issue #8](https://github.com/Blawx/blawx/issues/8))
  **Note that this may be a breaking change for people using the docassemble-blawx integration.**
* Changes to what counts as conflicting results for the purpose of override blocks, only applies
  to workspaces using the new true/false blocks.
### Fixed
* Docker install missing sudo.
* Docker install missing python3. ([Issue #38](https://github.com/Blawx/blawx/issues/38))
* Overridden answers still returned. ([Issue #2](https://github.com/Blawx/blawx/issues/2))
* Aggregate functions not working. ([Issue #19](https://github.com/Blawx/blawx/Issues/19))

## [v0.2.1-alpha](https://github.com/Blawx/blawx/releases/tag/v0.2.1-alpha) 2020-05-26
### Added
* Dockerized install process ([Issue #21](https://github.com/Blawx/blawx/issues/21))
* Calculation Block ([Issue #20](https://github.com/Blawx/blawx/issues/20))
* Changelog
### Changed
* Remove extra implication operators ([Issue #16](https://github.com/Blawx/blawx/issues/16))
* Math operators and aggregate functions now report "Number" as their output type.

## [v0.2-alpha](https://github.com/Blawx/blawx/releases/tag/v0.2-alpha) 2020-05-22
### Changed
* Installation process clarified, simplified. ([Issue #9](https://github.com/Blawx/blawx/issues/9))
### Fixed
* Reasoner was crashing on machines with slower processors. ([Issue #25](https://github.com/Blawx/blawx/issues/25))ff
