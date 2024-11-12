---
title: FastAPI
description: Setting up FastAPI to serve components.
---

<Prose>

The example app below incorporates setting up Jinja
templates, serving static files for Tailwind CSS, rendering JinjaX components, and using htmx. This is a 
working example that can be used as a reference.   

The source is in `examples/fastapi`.

</Prose>

<IncludeFiles :files="[
{'name': 'index.html', 'file': 'examples/fastapi/templates/index.html', 'lang':'html'},
{'name': 'app.py', 'file': 'examples/fastapi/app.py', 'lang':'python'}]"/>

<Prose>

## Setup

Install deps and setup environment 
```bash
cd examples/fastapi

# install tailwind css
npm install  

# build tailwind output css
npm run build 
 
# install python env, (creates .venv) dir
uv sync
source .venv/bin/activate
```

## Run

Run app 
```bash 
.venv/bin/fastapi dev -p 10000
```

You should see
```bash 
INFO:     Uvicorn running on http://127.0.0.1:10000 (Press CTRL+C to quit)
INFO:     Started reloader process [37550] using WatchFiles
INFO:     Started server process [37552]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Run tailwind watch in a separate terminal window to rebuild tailwind styles automatically
```bash 
npm run watch 
```

## Example page 

Open your browser to [http://127.0.0.1:10000](http://127.0.0.1:10000). You should see the example page.

![img.png](/static/img/fastapi_img.png)

</Prose>




