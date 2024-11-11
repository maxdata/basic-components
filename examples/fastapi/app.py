from fastapi import FastAPI, APIRouter, Request
import jinjax
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


# configure Jinja template location
templates = Jinja2Templates(directory="./templates")

# configure JinjaX component catalog with the template environment
templates.env.add_extension(jinjax.JinjaX)
catalog = jinjax.Catalog(jinja_env=templates.env)
catalog.add_folder("./components")


class HTMLRouter(APIRouter):
    """
    Router to return HTML responses
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_in_schema = False
        self.default_response_class = HTMLResponse


router = HTMLRouter()


@router.get("/")
async def index(request: Request):
    """Return a template that contains components"""
    return templates.TemplateResponse(request, "index.html")


@router.get("/button")
async def button(request: Request):
    """Render components directly to the response"""
    return catalog.render("Button", variant="destructive", _content="HTMX IS ENABLED!")


app = FastAPI()

# static files for serving css
app.mount(
    "/static",
    StaticFiles(directory="./static"),
    name="static",
)


# include routes
app.include_router(router)
