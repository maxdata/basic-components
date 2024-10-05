from fastapi import FastAPI, Request
from jinja2.ext import DebugExtension
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import jinjax
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

print(f"BASE_DIR={BASE_DIR}")
templates = Jinja2Templates(directory="templates")
templates.env.add_extension(DebugExtension)

templates.env.add_extension(jinjax.JinjaX)  # pyright: ignore [reportPrivateImportUsage]
catalog = jinjax.Catalog(jinja_env=templates.env)  # pyright: ignore [reportPrivateImportUsage]
catalog.add_folder(f"{BASE_DIR}/components/ui")
catalog.add_folder(f"{BASE_DIR}/layouts")

# Serve static files (CSS, etc.)
app.mount("/dist", StaticFiles(directory="dist"), name="dist")


@app.get("/", response_class=HTMLResponse)
async def get_textinput(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
