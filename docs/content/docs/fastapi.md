---
title: FastAPI
description: Setting up FastAPI to serve components.
---

<Prose>

This guide demonstrates how to set up a FastAPI application with Basic Components, showcasing:

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

The source is in `examples/fastapi`.

```
examples/fastapi/
├── app.py                      # FastAPI application
├── components                  # JinjaX components
│   ├── Button.jinja
│   ├── Card.jinja
│   ├── CardContent.jinja
│   ├── CardDescription.jinja
│   ├── CardFooter.jinja
│   ├── CardHeader.jinja
│   └── CardTitle.jinja
├── package-lock.json
├── package.json                # npm config (Tailwind)
├── pyproject.toml              # python project config
├── static                      # Static assets
│   ├── dist
│   │   └── output.css          # Compiled Tailwind CSS
│   └── src
│       └── input.css           # Source Tailwind CSS
├── tailwind.config.js          # Tailwind config
├── templates                   # Jinja template dir
│   └── index.html
└── uv.lock
```


</Prose>

<IncludeFiles :files="[
{'name': 'index.html', 'file': 'examples/fastapi/templates/index.html', 'lang':'html'},
{'name': 'app.py', 'file': 'examples/fastapi/app.py', 'lang':'python'}]"/>

<Prose>

## Setup Instructions

**Install Dependencies**
```bash
# Navigate to project directory
cd examples/fastapi

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
# Start FastAPI server
.venv/bin/fastapi dev --port 10000
```

You should see:
```bash 
INFO:     Uvicorn running on http://127.0.0.1:10000 (Press CTRL+C to quit)
INFO:     Started reloader process [37550] using WatchFiles
INFO:     Started server process [37552]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Enable Tailwind Watch Mode**
   In a separate terminal:
```bash 
npm run watch 
```
This will automatically rebuild Tailwind CSS when you make changes to your components.

## Verify Installation

1. Open your browser to [http://127.0.0.1:10000](http://127.0.0.1:10000)
2. You should see the example page with:
    - Styled components using Tailwind CSS
    - Working htmx button that updates on click
    - Dark mode support

![Example Page](/static/img/fastapi_img.png)

## Common Issues and Solutions

1. **Styles Not Updating**
    - Ensure Tailwind watch process is running
    - Check that `/static/css/tailwind.css` is being served
    - Verify CSS path in template is correct

2. **Components Not Found**
    - Verify `COMPONENT_DIR` path in app.py
    - Check component file extensions (.jinja)
    - Ensure JinjaX extension is properly loaded

3. **Static Files 404**
    - Check `STATIC_DIR` path in app.py
    - Verify directory structure matches configuration
    - Ensure static files mount is before router inclusion

4. **htmx Not Working**
    - Check browser console for errors
    - Verify htmx script is loaded
    - Confirm route handlers return proper HTML responses

## Next Steps

- Review the [Components Guide](/docs/components) to learn about available components
- Explore [Modern Tools](/docs/modern_tools) to understand the tech stack
- Check out the [Examples](/examples) for more usage patterns


</Prose>




