# CHANGELOG


## v0.2.0 (2024-11-17)

### Bug Fixes

- Fix dependecy groups in pyproject.toml
  ([`b6e4fc8`](https://github.com/basicmachines-co/basic-components/commit/b6e4fc80e23410d5d0bc990d40000b4a7bfbd585))

### Documentation

- Add CHANGELOG to docs site
  ([`0b35e1d`](https://github.com/basicmachines-co/basic-components/commit/0b35e1df3c154a20a64399d93a9ad363c84d90f5))

### Features

- Add component dependency analyzer tool
  ([`3aa76c8`](https://github.com/basicmachines-co/basic-components/commit/3aa76c8868887e010aca4e6af925cea37988f32f))

Introduce a new tool to analyze component dependencies with optional TOML and JSON output. This tool
  can identify PascalCase component references and supports integrations, special icon cases, and
  core components. Added a corresponding TOML file for known dependencies.

### Refactoring

- Adjust project configuration and file structure
  ([`7fc49f2`](https://github.com/basicmachines-co/basic-components/commit/7fc49f272ccb9616270bd2c5142af658e22e94f2))

Move dependencies and script definitions in pyproject.toml for better structure. Rename and relocate
  cli.py to components.py to improve clarity. Update .gitignore to include .env files.

- Restructure component files and update dependencies
  ([`d74ea0e`](https://github.com/basicmachines-co/basic-components/commit/d74ea0eb55b11a9b6b403541e24de80960921751))

Moved component files to new directories for better organization. Updated pyproject.toml and uv.lock
  reflecting changes and added tomli-w dependency. Enhanced CLI tool with dependency handling and a
  dry run feature.


## v0.1.7 (2024-11-15)

### Bug Fixes

- Update tag for semantic-release action
  ([`ebd48b3`](https://github.com/basicmachines-co/basic-components/commit/ebd48b3261dc9718eefd315d26a500255d8ed387))

- Push to pypi and github. Install uv in build_command for semantic_release
  ([`e29837f`](https://github.com/basicmachines-co/basic-components/commit/e29837f4f7b6906ce70003edd898a5cb39c313f6))

- Add uv to docker image for release
  ([`084c008`](https://github.com/basicmachines-co/basic-components/commit/084c00804d1fc834f1fb5a40fcc25d93ce5c99e7))

- Redo release workflow based on python-semantic-release docs
  ([`b03dd50`](https://github.com/basicmachines-co/basic-components/commit/b03dd504c013f8c9f1622248f43c1d7f26d92618))

### Chores

- **release**: 0.1.7 [skip ci]
  ([`e7a1452`](https://github.com/basicmachines-co/basic-components/commit/e7a14526696dda306d0b332d21d2f290a4a66116))

### Documentation

- Add installation docs for components
  ([`3f963aa`](https://github.com/basicmachines-co/basic-components/commit/3f963aaad07652cd3e5561f8509b4ac802e3bcca))

### Features

- Add tabs component and fix broken Icon references
  ([`1d81161`](https://github.com/basicmachines-co/basic-components/commit/1d811615f92c33f248d209fdbde9903f5d0f9d25))


## v0.1.6 (2024-11-15)

### Chores

- Fix github release workflow
  ([`2f4092e`](https://github.com/basicmachines-co/basic-components/commit/2f4092ecf68cd6d77a71d88f018783a2016c813a))

- Update intallation docs and README
  ([`ba44c67`](https://github.com/basicmachines-co/basic-components/commit/ba44c67df0b240301819d4e806def7bf5fc5472c))


## v0.1.5 (2024-11-14)

### Chores

- Fix version_toml for semantic_release
  ([`6e5ef7d`](https://github.com/basicmachines-co/basic-components/commit/6e5ef7d9364abedf40feb2e0b1a205c967aa7903))


## v0.1.4 (2024-11-14)

### Chores

- Fix pyproject toml for semantic_release
  ([`7db428a`](https://github.com/basicmachines-co/basic-components/commit/7db428a925db897e172df80136cf5d3daf7eb446))


## v0.1.3 (2024-11-14)

### Chores

- Fix github release workflow
  ([`6210da8`](https://github.com/basicmachines-co/basic-components/commit/6210da8d82dd4daced77560b70a3af9e1e80c408))


## v0.1.2 (2024-11-14)

### Chores

- Add github actions release workflow
  ([`f32e6fe`](https://github.com/basicmachines-co/basic-components/commit/f32e6fe98e5766f9403e6d35044fb801a36f4e14))

- More doc updates for cli and utils functions
  ([`5ad08fb`](https://github.com/basicmachines-co/basic-components/commit/5ad08fb315b71990d3af78d4f73337f9950994d2))


## v0.1.1 (2024-11-14)

### Chores

- Update docs for installing, using cli
  ([`d481aef`](https://github.com/basicmachines-co/basic-components/commit/d481aef15e36bf18ce05e21b250b14a3a7a5b7df))

- Update llms.md for components cli tool
  ([`a1632d8`](https://github.com/basicmachines-co/basic-components/commit/a1632d81f6466380fda41d474e8a063e59485704))

- Update example projects
  ([`a2981a5`](https://github.com/basicmachines-co/basic-components/commit/a2981a527e7a9f13dba7bce2e5f42a85341a7cb7))

- More docs cleanup for installing basic-components
  ([`7b2ac4c`](https://github.com/basicmachines-co/basic-components/commit/7b2ac4c6ab81751774b9127aa6badf6697384b36))

- Remove Jinja from frameworks in pyproject.toml
  ([`70554ca`](https://github.com/basicmachines-co/basic-components/commit/70554cac5c33cad2230b2db74c366a8135ca479c))

- Update pyproject.toml and README to include dependency groups
  ([`022d452`](https://github.com/basicmachines-co/basic-components/commit/022d4522de88d35a0bda9009d87b55ee0661e45b))

- Add usage docs for the components cli
  ([`fae648b`](https://github.com/basicmachines-co/basic-components/commit/fae648bd2c697dbea2908af4aa88fcba7c0fef67))

- Upate docs for components cli
  ([`05d6ee4`](https://github.com/basicmachines-co/basic-components/commit/05d6ee4e8fe96ea0f6f2448f5a60c1de716ae508))

### Features

- Integrate basic-components utilities and refactor setup
  ([#8](https://github.com/basicmachines-co/basic-components/pull/8),
  [`90b5d2e`](https://github.com/basicmachines-co/basic-components/commit/90b5d2e6cef39f8f4d03a1e4d2e4f0eedec9f0d8))

* feat: integrate basic-components utilities and refactor setup

Introduce `setup_component_catalog` and Tailwind utilities. Add dependency `basic-components` to
  examples, refactor `setup_component_catalog` usage, and add `tw` to Jinja globals.

* feat(tailwind): enhance class merging logic and improve docs

Enhance `tw` function to handle class conflicts and maintain consistent ordering. Update
  documentation with advanced component patterns, including state management, event handling, and
  styling best practices.

---------

Co-authored-by: phernandez <phernandez@basicmachines.co>
