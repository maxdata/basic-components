---
title: CLI
description: Adding components to your project
---

<Prose>

Be sure you have read the [installation](/docs/installation) docs and set up your project first. 

## Copy/Paste

Code for components can be copy/pasted directly from the example pages via the `Code` tabs. You can install components
anywhere in you project. The rest of the information in these docs assume they are located in the `components/ui` dir in
your project. See the [JinjaX](/docs/utilities#jinjax) docs for more info. 

## Vendoring Components

The components in this project can also be copied (vendored) directly into your project using the `components` tool 
in the `basic-components` package via `uv`. You can then customize them as needed. This is the recommendedd way to 
install components because it will also include any dependencies (other component dependencies) required.

To vendor a component into your project using the `components` tool:

```bash
uvx --from basic-components add <component_name> 
```

The components will be added to your project in the `components/ui/<component_name>` directory. 

See the [utilities](/docs/utilities) docs for more information. 
</Prose>