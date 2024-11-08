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

from docs.templates import template


class HTMLRouter(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_in_schema = False
        self.default_response_class = HTMLResponse


router = HTMLRouter()


class SampleForm(StarletteForm):
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


@router.get("", response_class=HTMLResponse)
async def display(request: Request):
    form = SampleForm(request)
    return template(
        request=request,
        name="examples/wtform.html",
        context={"form": form},
    )


@router.post("", response_class=HTMLResponse)
async def post(request: Request):
    form = await SampleForm.from_formdata(request)
    if not await form.validate():
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
    print(f"Name: {username}, Email: {email}, Password: {password}")

    # trigger event via response header
    return template(
        request,
        "examples/wtform.html",
        context={"form": form},
        status_code=status.HTTP_201_CREATED,
        headers={
            # "HX-Trigger": json.dumps(
            #     {"show-toast": {"target": "window", "value": "form-info"}}
            # )
            # "HX-Trigger": json.dumps({"show-toast": "form-info"})  ## $event.detail: {value: 'form-info', elt: form.space-y-4.htmx-request}
            # "HX-Trigger": json.dumps({"show-toast": {"target": "window"}})  ## $event.detail: {target: 'window', elt: form.space-y-4.htmx-request}
            # "HX-Trigger": "show-toast:form-info"
            "HX-Trigger": json.dumps(
                {"show-toast": {"target": "window", "value": "form-info"}}
            )
        },
    )


# Success endpoint
@router.get("/success")
async def success(request: Request):
    return {"message": "Form submitted successfully!"}
