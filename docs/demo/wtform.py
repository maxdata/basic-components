import json

from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import HTMLResponse
from starlette_wtf import StarletteForm
from wtforms import (
    StringField,
    validators,
    PasswordField,
)

from docs.templates import template, catalog


class HTMLRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_in_schema = False
        self.default_response_class = HTMLResponse


router = HTMLRouter()


class SampleForm(StarletteForm):
    """
    Form object with declarative validation
    """

    username = StringField(
        "Username",
        [validators.InputRequired(), validators.Length(min=4, max=25)],
        id="username",
        render_kw={"placeholder": "username"},
        description="Enter a unique username.",
    )
    email = StringField(
        "Email",
        [validators.InputRequired(), validators.Email()],
        id="email",
        render_kw={"placeholder": "your@email.com"},
        description="Your primary email address.",
    )
    password = PasswordField(
        "Password",
        [validators.InputRequired(), validators.Length(min=6)],
        id="password",
        render_kw={"placeholder": "••••••••"},
        description="Must be at least 6 characters.",
    )


@router.get("/demo/wtform")
async def display(request: Request):
    """
    display the form on the page via a template
    """
    form = SampleForm(request)
    return template(
        request=request,
        name="examples/wtform.html",
        context={"form": form},
    )


@router.post("/demo/wtform")
async def post(request: Request):
    """
    handle the form via post
    """
    form = await SampleForm.from_formdata(request)

    if not await form.validate():
        # return with a 422 response
        return template(
            request,
            "examples/wtform.html",
            context={"form": form},
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )

    # Form is valid, process the form data
    username = form.username.data
    email = form.email.data
    password = form.password.data
    # Log or handle the data as needed (e.g., save to a database)

    # return results to the page
    component = catalog.render(
        "FormResult",
        _content=json.dumps(
            {"username": username, "email": email, "password": password}
        ),
    )
    return HTMLResponse(component)
