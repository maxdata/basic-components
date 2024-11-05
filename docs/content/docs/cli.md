---
title: CLI
description: Adding components to your project
---

<Prose>

Be sure you have read the [installation](/docs/installation) docs and setup your project first. 

## Copy/Paste

Code for components can be copy/pasted directly from the example pages via the `Code` tabs.

## Vendoring Components

The components in this project can also be copied (vendored) directly into your project using [Copier](https://copier.readthedocs.io/en/stable/).
You can then customize them as needed.

To vendor these components into your project using copier:

1. Ensure you have Copier installed:

```bash
pip install copier
```

2. Run the following command from your project directory, specifying the destination:

```bash
copier copy https://github.com/basicmachines-co/basic-components.git ./path/to/destination
```
Replace `./path/to/destination` with the directory where you want the components to be copied.

3. To preview the operation without making any changes, use the `--pretend` flag:

```bash
copier copy --pretend https://github.com/basic-foundation/basic-components.git ./path/to/destination
```

### Versioning and Updates

**Notes:**

- Copier can also update code with newer revisions after it has been copied.
- If updating, copier will preserve your existing files. It will show diffs for any conflicts and allow you to choose how to handle them.
- You can specify a specific branch, tag, or commit by appending it to the repository URL, e.g., `...basic-components.git@v1.0.0 ./path/to/destination`
- You can also fork this repo and use your own git url with copier or use a local copy of the repository.

For more detailed information on Copier usage, refer to the [Copier documentation](https://copier.readthedocs.io/).


</Prose>