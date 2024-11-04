from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from docs.templates import template
from docs.site import site_config


class HTMLRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_in_schema = False
        self.default_response_class = HTMLResponse


router = HTMLRouter()


@router.get("/button")
async def button(request: Request):
    context = {
        "config": site_config,
    }
    return template(request, "demo/button_docs.html", context=context)
