---
title: CLI
description: Adding components to your project
---

<Prose>

Be sure you have read the [installation](/docs/installation) docs and set up your project first. 

## Vendoring Components

The components in this project can be copied (vendored) directly into your project using the `components` tool 
in the `basic-components` package via `uv`. You can then customize them as needed. This is the recommendedd way to 
install components because it will also include any dependencies (other referenced components) required.

To vendor a component into your project using the `components` tool:

```bash
uvx --from basic-components add <component_name> 
```

The components will be added to your project in the `components/ui/<component_name>` directory. 

### Example

```bash
➜ uvx --from basic-components components add button 
Installing button from 
'https://github.com/basicmachines-co/basic-components.git' ...

Copying from template version 0.0.0.post163.dev0+70554ca
    create  button
    create  button/Button.jinja


╭─────────────────────────── Installation Complete ────────────────────────────╮
│ ✓ Added button component                                                     │
│                                                                              │
│  components-dir=components/ui                                                │
╰──────────────────────────────────────────────────────────────────────────────╯

```
View the results
```bash
➜ tree components 
components
└── ui
    └── button
        └── Button.jinja

2 directories, 1 file

```

See the [utilities](/docs/utilities) docs for more information about setting up your project to use the components. 

### Components cli tool

The `components` cli tool has several options. 

Add a component
```bash
uvx --from basic-components add button
```

Add a component, specifying the repo
```bash
uvx --from basic-components add button --repo-url https://github.com/basicmachines-co/basic-components.git
```

Add a component, specifying the repo and branch or tag
```bash
uvx --from basic-components add button --repo-url https://github.com/basicmachines-co/basic-components.git --branch main
```

The `repo-url` arg can also point to a local directory if you have the project checked out. You can also pass the components 
destination directory via the `components-dir` arg.

## Copy/Paste

Code for components can also be copy/pasted directly from the example pages via the `Code` tabs. You can install components
anywhere in you project. The rest of the information in these docs assume they are located in the `components/ui` dir in
your project. See the [JinjaX](/docs/utilities#jinjax) docs for more info on how to set up components in your project.

## Other tools

If you don't want to use `uv`, then you can also use the `components` cli by installing it using `pip` or `poetry`. This
will only install the libs needed for the cli, not the components. 

### Pip
```bash
pip install "basic-components[cli]"
```

To use the `components` tool, you can run

```bash
pipx run components add <component>
```

### Poetry
```bash
poetry add "basic-components[cli]"
```

To use the `components` tool, you can run

```bash
poetry run components add <component>
```


</Prose>