---
title: Django
description: Setting up Django to serve components.
---

<Prose>

This guide demonstrates how to set up a minimal Django application with Basic Components, showcasing:

- JinjaX component integration
- Tailwind CSS styling
- Alpine.js interactivity
- HTMX dynamic updates

## Prerequisites

Before starting, ensure you have:

- Python 3.8 or higher
- [UV](https://docs.astral.sh/uv/getting-started/installation/)
- Node.js 16+ and npm 8+
- A text editor or IDE

## Project Structure

The source is in `examples/django`:

```
examples/django/
├── app.py                      # Single-file Django application
├── components                  # JinjaX components
│   └── ui
│       ├── button
│       │   └── Button.jinja
│       └── card
│           ├── Card.jinja
│           ├── CardContent.jinja
│           ├── CardDescription.jinja
│           ├── CardFooter.jinja
│           ├── CardHeader.jinja
│           └── CardTitle.jinja
├── package-lock.json
├── package.json                # npm config (Tailwind)
├── pyproject.toml              # python project config
├── static                      # Static assets
│   ├── dist
│   │   └── output.css         # Compiled Tailwind CSS
│   └── src
│       └── input.css          # Source Tailwind CSS
├── tailwind.config.js         # Tailwind config
├── templates                  # Jinja template dir
│   └── index.html
└── uv.lock
```

</Prose>

<IncludeFiles :files="[
{'name': 'index.html', 'file': 'examples/django/templates/index.html', 'lang':'html'},
{'name': 'app.py', 'file': 'examples/django/app.py', 'lang':'python'}]"/>

<Prose>

## Setup Instructions

**Install Dependencies**
```bash
# Navigate to project directory
cd examples/django

# Install npm dependencies for Tailwind
npm install

# Build Tailwind CSS
npm run build

# Create and activate Python virtual environment
uv sync
source .venv/bin/activate
```

**Run the Application**
```bash
# Start Django server
python app.py
```

You should see:
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

Django version 4.2.x, using settings None
Starting development server at http://0.0.0.0:10000/
Quit the server with CONTROL-C.
```

**Enable Tailwind Watch Mode**
In a separate terminal:
```bash
npm run watch
```
This will automatically rebuild Tailwind CSS when you make changes to your components.

## Verify Installation

1. Open your browser to [http://localhost:10000](http://localhost:10000)
2. You should see the example page with:
    - Styled components using Tailwind CSS
    - Working htmx button that updates on click
    - Dark mode support

![Example Page](/static/img/example_img.png)

## Key Features

1. **Single-File Setup**
    - Entire Django configuration in one file
    - Minimal dependencies and middleware
    - Simple component serving

2. **JinjaX Integration**
    - Direct component usage in templates
    - Automatic subdirectory handling
    - Clean component syntax

3. **Modern Stack**
    - Tailwind CSS for styling
    - Alpine.js for interactivity
    - HTMX for dynamic updates

## Common Issues and Solutions

1. **Styles Not Updating**
    - Ensure Tailwind watch process is running
    - Check that `static/dist/output.css` is being served
    - Verify static files configuration in `app.py`
    - Clear browser cache

2. **Components Not Found**
    - Check component directory structure
    - Verify JinjaX catalog configuration
    - Ensure component names match file names
    - Check component file extensions (.jinja)

3. **Static Files 404**
    - Verify STATICFILES_DIRS setting
    - Check static URL configuration
    - Ensure StaticMiddleware is enabled

4. **htmx Not Working**
    - Check browser console for errors
    - Verify htmx script is loaded
    - Confirm URL patterns are correct
    - Check htmx attributes on components

## Benefits of Single-File Setup

1. **Simplicity**
    - Easy to understand and maintain
    - No complex project structure
    - Quick to get started

2. **Portability**
    - Everything in one place
    - Easy to copy and share
    - Minimal configuration needed

3. **Development Focus**
    - Concentrate on components
    - Rapid prototyping
    - Simple debugging

## Next Steps

- Review the [Components Guide](/docs/components) to learn about available components
- Explore [Modern Tools](/docs/modern_tools) to understand the tech stack
- Check out the [Examples](/examples) for more usage patterns
- Consider expanding to a full Django project structure for larger applications

</Prose>