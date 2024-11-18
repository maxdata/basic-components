---
title: Quick Start
description: Basic Components brings modern UI component patterns to Python web applications. This guide will help you get up and running quickly with your first components.
---

<Prose>

Use the `components` cli to install components directly into your project.

</Prose>

<img src= "/static/img/components-add-demo.gif"/>

<Prose>

## Install a component


```bash
# Install uv package installer if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install your first component
uvx --from basic-components components add button

# Preview installation with --dry-run
uvx --from basic-components components add dropdown_menu --dry-run
```

## Prerequisites

Before installing components, ensure you have:

- Python 3.10 or higher
- [uv package installer](https://astral.sh/uv) installed
- A Python web framework (FastAPI, Django, or Flask), examples apps are included for each. 
- [Tailwind CSS](https://tailwindcss.com/) [configured](/docs/installation) in your project
- [JinjaX](https://jinjax.scaletti.dev/) installed and [configured](/docs/utilities#jinjax)
- [Alpine.js](https://alpinejs.dev/) [configured](https://alpinejs.dev/start-here) in your web templates
- [htmx](https://htmx.org/) configured in your web tempates

## Step-by-Step Setup

### 1. Initialize Components Directory

First, create the components directory structure:

```bash
uvx --from basic-components components init
```

This creates a `components/ui` directory in your project where components will be installed.

### 2. Install Components

Install your first component:

```bash
uvx --from basic-components components add button
```

Dependencies are handled automatically. For example, when installing `dropdown_menu`, its required components are installed too:

```bash
uvx --from basic-components components add dropdown_menu
```

### 3. Set Up Utilities

You have two options for adding required utilities:

#### Option 1: Install the utils package (Recommended)

Install the utils package which includes `cn()` and other utility functions:

```bash
uv add "basic-components[utils]"
```

This provides:

- `cn()` utility for Tailwind class name management
- JinjaX configuration helpers


#### Option 2: Manual Setup

If you prefer to manage the utilities yourself, create `lib/utils.py`:

```python
from typing import List

def cn(*args: List[str]) -> str:
    """Merge CSS class names"""
    # see https://github.com/basicmachines-co/basic-components/blob/main/basic_components/utils/tailwind.py
    return ' '.join(filter(None, args))
```

See the [utilities](/docs/utilities) docs for configuring the `cn()` function in the jinja global environment. 

### 4. Configure JinjaX

If you installed `basic-components[utils]`, you can use the provided configuration:

```python
from basic_components.utils.jinjax import setup_component_catalog
from starlette.templating import Jinja2Templates
import jinjax

COMPONENT_DIR = "components"

templates = Jinja2Templates(directory="templates")
templates.env.add_extension(jinjax.JinjaX)
catalog = jinjax.Catalog(jinja_env=templates.env)

# include all subdirectories in the JinjaX catalog. 
catalog = setup_component_catalog(
    catalog, components_dir=COMPONENT_DIR
)
```

Or configure JinjaX manually:

```python
from jinjax import Jinja

templates = Jinja(
    template_dirs=["templates"],
    component_dirs=["components"]
)

catalog = jinjax.Catalog(jinja_env=templates.env)

# add all dirs with components to the catalog
catalog.add_folder("components/ui")
catalog.add_folder("components/ui/button")
```

See the [utilities](/docs/utilities#jinjax) docs for more about the setting up components with JinjaX.

## Usage

Basic Components works with any Python web framework that supports JinjaX. Here are examples for common frameworks:

### FastAPI

</Prose>

<IncludeFiles :files="[
{'name': 'index.html', 'file': 'examples/fastapi/templates/index.html', 'lang':'html'},
{'name': 'app.py', 'file': 'examples/fastapi/app.py', 'lang':'python'}]"/>

<Prose>

See the [FastAPI example](https://github.com/basicmachines-co/basic-components/tree/main/examples/fastapi) for a complete working project.

Components are easy to integrate with htmx.

</Prose>
<img src= "/static/img/htmx-demo.gif"/>

<Prose>

### Django and Flask

Similar setup is available for Django and Flask. See complete working examples:

- [Django example](https://github.com/basicmachines-co/basic-components/tree/main/examples/django)
- [Flask example](https://github.com/basicmachines-co/basic-components/tree/main/examples/flask)

## Common Patterns

### Component Customization

Components accept a `className` argument for additional styles:

```html
<Button
    variant="outline"
    className="mt-4 w-full md:w-auto"
>
    Custom Button
</Button>
```

### Using Variants

Some components support variants for different styles:

```html
<Button variant="default">Default</Button>
<Button variant="destructive">Destructive</Button>
<Button variant="outline">Outline</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="ghost">Ghost</Button>
```

### Adding htmx Interactions

Components work seamlessly with htmx attributes:

```html
<Button
    variant="outline"
    hx-post="/api/submit"
    hx-target="#result"
    hx-swap="outerHTML"
>
    Submit
</Button>
```

### Managing State with Alpine.js

Components use Alpine.js for client-side state management:

```html
<div x-data="{ open: false }">
    <Button
        variant="outline"
        x-on:click="open = !open"
    >
        Toggle
    </Button>
    <div x-show="open" class="mt-4">
        Content
    </div>
</div>
```


## Next Steps

- Browse [available components](https://components.basicmachines.co/docs/components)
- Learn about [component dependencies](https://components.basicmachines.co/docs/dependencies)
- Read the [customization guide](https://components.basicmachines.co/docs/customization)
- Check out [example projects](https://github.com/basicmachines-co/basic-components/tree/main/examples)

## Troubleshooting

- Components must be installed in the `components/ui` directory
- Components may have dependencies that are installed automatically
- The `cn()` utility function is required for class name handling
- JinjaX must be configured to use the components directory

Need help? Check our [GitHub issues](https://github.com/basicmachines-co/basic-components/issues) or start a discussion.


</Prose>
