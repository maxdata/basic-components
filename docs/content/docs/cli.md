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
Replace `./path/to/destination` with the directory in your project where you want the components to be copied.

3. To preview the operation without making any changes, use the `--pretend` flag:

```bash
copier copy --pretend https://github.com/basic-foundation/basic-components.git ./path/to/destination
```

### Component Directory Structure

Components are organized into subdirectories by type (e.g., `accordion`, `button`, `dialog`). This organization helps with maintenance but doesn't affect how you use the components in your templates.

To make all components available in your JinjaX templates, add the following to your application setup:

```python
from pathlib import Path
from jinjax import Catalog

def setup_component_catalog():
    catalog = Catalog()
    
    # Base UI components directory
    components_dir = Path("path/to/destination/components/ui")
    
    # Register each component subdirectory first
    for component_dir in components_dir.iterdir():
        if component_dir.is_dir():
            catalog.add_folder(str(component_dir))
            
    # Register the main components directory last
    catalog.add_folder(str(components_dir))
    
    return catalog

# Usage in your app setup
catalog = setup_component_catalog()
```

This setup allows you to use components with their original names, without needing to reference the subdirectories:

```html
<!-- Components can be used directly, no need for subdirectory prefixes -->
<Button variant="primary">Click Me</Button>

<Card>
    <CardHeader>
        <CardTitle>Title</CardTitle>
    </CardHeader>
</Card>
```

### Versioning and Updates

- Copier can also update code with newer revisions after it has been copied.
- If updating, copier will preserve your existing files. It will show diffs for any conflicts and allow you to choose how to handle them.
- You can specify a specific branch, tag, or commit by appending it to the repository URL, e.g., `...basic-components.git@v1.0.0 ./path/to/destination`
- You can also fork this repo and use your own git url with copier or use a local copy of the repository.

For more detailed information on Copier usage, refer to the [Copier documentation](https://copier.readthedocs.io/).


</Prose>