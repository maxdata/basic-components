"""
FastAPI example application demonstrating:
- JinjaX component integration
- Static file serving for Tailwind CSS
- HTMX dynamic updates
- Component rendering
"""

from pathlib import Path
from typing import Any
from fastapi import FastAPI, APIRouter, Request
import jinjax
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


# Configuration
TEMPLATE_DIR = "./templates"
COMPONENT_DIR = "./components/ui"
STATIC_DIR = "./static"

# Setup Jinja templates with JinjaX support
templates = Jinja2Templates(directory=TEMPLATE_DIR)
templates.env.add_extension(jinjax.JinjaX)

# Configure JinjaX component catalog
catalog = jinjax.Catalog(jinja_env=templates.env)

components_dir = Path(f"{COMPONENT_DIR}")

# Register each component subdirectory
for component_dir in components_dir.iterdir():
    if component_dir.is_dir():
        catalog.add_folder(str(component_dir))

catalog.add_folder(COMPONENT_DIR)


class HTMLRouter(APIRouter):
    """Router configured to return HTML responses by default."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.include_in_schema = False
        self.default_response_class = HTMLResponse


router = HTMLRouter()


@router.get("/")
async def index(request: Request) -> HTMLResponse:
    """Render the main page with component examples."""
    return templates.TemplateResponse(request, "index.html")


@router.get("/button")
async def button(request: Request) -> HTMLResponse:
    """
    Example endpoint demonstrating direct component rendering.
    Used by htmx for dynamic button updates.
    """
    return catalog.render("Button", variant="destructive", _content="HTMX IS ENABLED!")


# Create FastAPI application
app = FastAPI(
    title="Basic Components Demo",
    description="Demonstration of JinjaX components with FastAPI",
)

# Mount static files for CSS
app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)

# Include HTML routes
app.include_router(router)
