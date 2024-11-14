---
title: Utilities
description: Helper functions for setting up components and merging Tailwind classes
---

<Prose>

To use the utility function below, install the `basic-components` package into your project. You can also get the code
from GitHub. 

```bash
uv add basic-machines 
```

## JinjaX 

### Component Directory Structure

Components are organized into subdirectories by type (e.g., `accordion`, `button`, `dialog`). 
This organization helps with maintenance but doesn't affect how you use the components in your templates. This allows 
you to use components with their original names, without needing to reference the subdirectories:

```html
<!-- Components can be used directly, no need for subdirectory prefixes -->
<Button variant="primary">Click Me</Button>

<Card>
    <CardHeader>
        <CardTitle>Title</CardTitle>
    </CardHeader>
</Card>
```

Basic Components includes a `setup_component_catalog()` helper function to include all components in subdirectories. 

Each component is assumed to be packaged in a subdirectory within the `components` root directory. Components are under the 
`components/ui` top level directory. 

```bash
project-root
├── components
    ├── custom
    │   ├── CustomComponent.jinja
    └── ui
        ├── ...
        ├── button
        │   └── Button.jinja
        ├── card
        │   ├── Card.jinja
        │   ├── CardContent.jinja
        │   ├── CardDescription.jinja
        │   ├── CardFooter.jinja
        │   ├── CardHeader.jinja
        │   └── CardTitle.jinja
        ├── ...
```

You can place your own components within your own subdirectory also, for example `components/custom`. Note that components 
should be named uniquely, or JinjaX will load the first one it finds. 

```python
from basic_components.utils.jinjax import setup_component_catalog
from starlette.templating import Jinja2Templates
import jinjax

COMPONENT_DIR = "components"

templates = Jinja2Templates(directory="templates")
templates.env.add_extension(jinjax.JinjaX)
catalog = jinjax.Catalog(jinja_env=templates.env)

# include subdirectories in the JinjaX catalog. 
# optionally include icons 
catalog = setup_component_catalog(
    catalog, components_dir=COMPONENT_DIR
)

# add any extra dirs to the catalog with custom components
catalog.add_folder("components/custom")
```

You can get the code for the Jinjax helper from the [GitHub repo](https://github.com/basicmachines-co/basic-components/blob/main/basic_components/utils/jinjax.py).



## cn()

Basic Components provides a utility function `cn()` for merging Tailwind CSS classes while handling conflicts properly. 
This needs to be added as a global in the Jinja environment so it is available in all templates.  

```python
from starlette.templating import Jinja2Templates
from basic_components.utils.tailwind import tw

templates = Jinja2Templates(directory="templates")

# Add cn to globals
templates.env.globals["cn"] = tw
```

### Usage

The `cn()` function is then globally available in templates.

{{'
```jinja
{#def
    className: str = ""
#}
<div 
    class="{{ cn(
        'flex flex-col-reverse sm:flex-row sm:space-x-2',
        'sm:justify-end' if 'sm:justify-start' not in className else '',
        className
    ) }}"
>
    {{ content }}
</div>
```
'}}

### Features

- Handles class conflicts (last one wins)
- Supports responsive modifiers (sm:, md:, etc.)
- Supports state modifiers (hover:, focus:, etc.)
- Handles arbitrary values ([...])
- Preserves non-conflicting classes

You can get the code for the tailwind merge from the [GitHub repo](https://github.com/basicmachines-co/basic-components/blob/main/basic_components/utils/tailwind.py).

</Prose>