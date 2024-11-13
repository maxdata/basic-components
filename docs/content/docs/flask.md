---
title: Flask
description: Setting up Flask to serve components.
---

<Prose>

This guide demonstrates how to set up a minimal Flask application with Basic Components, showcasing:

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

The source is in `examples/flask`:

```
examples/flask/
├── app.py                      # Single-file Flask application
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
{'name': 'index.html', 'file': 'examples/flask/templates/index.html', 'lang':'html'},
{'name': 'app.py', 'file': 'examples/flask/app.py', 'lang':'python'}]"/>

<Prose>

## Setup Instructions

**Install Dependencies**
```bash
# Navigate to project directory
cd examples/flask

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
# Start Flask server
python app.py
```

You should see:
```bash
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:10000
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX
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


## Common Issues and Solutions

1. **Styles Not Loading**
    - Check `static/dist/output.css` exists
    - Verify static folder structure
    - Clear browser cache
    - Check Flask static file settings

2. **Components Not Found**
    - Verify component paths
    - Check JinjaX catalog setup
    - Ensure file extensions are .jinja
    - Check template loader configuration

3. **Templates Not Rendering**
    - Check template directory structure
    - Verify Jinja environment setup
    - Check route return values
    - Enable Flask debugging

4. **HTMX Issues**
    - Verify script loading
    - Check route definitions
    - Inspect browser console
    - Test endpoint responses


## Next Steps

- Review the [Components Guide](/docs/components) to learn about available components
- Explore [Modern Tools](/docs/modern_tools) to understand the tech stack
- Check out the [Examples](/examples) for more usage patterns
- Consider Flask extensions for additional functionality
- Explore production deployment options


</Prose>