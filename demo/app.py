from pathlib import Path

import jinjax
from fastapi import FastAPI, Request
from jinja2.ext import DebugExtension
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette_wtf import CSRFProtectMiddleware
from starlette_wtf import StarletteForm
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
    SelectField,
    FileField,
    BooleanField,
    RadioField,
    IntegerField,
    validators,
)

# project root
BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()

print(f"BASE_DIR={BASE_DIR}")
templates = Jinja2Templates(directory=f"{BASE_DIR}/demo/templates")
templates.env.add_extension(DebugExtension)

templates.env.add_extension(jinjax.JinjaX)  # pyright: ignore [reportPrivateImportUsage]
catalog = jinjax.Catalog(jinja_env=templates.env)  # pyright: ignore [reportPrivateImportUsage]
catalog.add_folder(f"{BASE_DIR}/components")
catalog.add_folder(f"{BASE_DIR}/components/ui")
catalog.add_folder(f"{BASE_DIR}/components/icons")
catalog.add_folder(f"{BASE_DIR}/demo/examples")

# Serve static files (CSS, etc.) from shad-cn
app.mount("/dist", StaticFiles(directory=f"{BASE_DIR}/shadcn-ui/dist"), name="dist")

# CSRF Middleware for form handling
app.add_middleware(SessionMiddleware, secret_key="session_key")
app.add_middleware(CSRFProtectMiddleware, csrf_secret="your_secret_key_here")


@app.get("/", response_class=HTMLResponse)
async def components(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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
        default="example@example.com",
        description="Your primary email address.",
    )
    password = PasswordField(
        "Password",
        [validators.InputRequired(), validators.Length(min=6)],
        id="password",
        description="Must be at least 6 characters.",
    )
    bio = TextAreaField(
        "Bio",
        [validators.Optional(), validators.Length(max=200)],
        id="bio",
        description="Write a brief bio about yourself.",
        default="I love coding and coffee.",
    )
    age = IntegerField(
        "Age",
        [validators.Optional(), validators.NumberRange(min=18, max=100)],
        id="age",
        default=25,
        description="Your age (must be between 18 and 100).",
    )
    gender = RadioField(
        "Gender",
        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
        id="gender",
        description="Select your gender.",
        default="M",
    )
    country = SelectField(
        "Country",
        choices=[("US", "United States"), ("CA", "Canada"), ("UK", "United Kingdom")],
        id="country",
        default="US",
        description="Choose your country.",
    )
    agree_terms = BooleanField(
        "I agree to the terms and conditions",
        [validators.InputRequired()],
        id="agree_terms",
        description="You must agree before submitting.",
    )
    profile_picture = FileField(
        "Profile Picture",
        [validators.Optional()],
        id="profile_picture",
        description="Upload your profile picture (optional).",
    )


@app.get("/form", response_class=HTMLResponse)
async def display_form(request: Request):
    form = SampleForm(request)
    return templates.TemplateResponse(
        "sample_form.html", {"request": request, "form": form}
    )


@app.post("/form", response_class=HTMLResponse)
async def post_sample_form(request: Request):
    form = await SampleForm.from_formdata(request)
    if await form.validate():
        # Form is valid, process the form data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Log or handle the data as needed (e.g., save to a database)
        print(f"Name: {username}, Email: {email}, Password: {password}")

        # Redirect to a success page or any other action
        return RedirectResponse(url="/success", status_code=303)
    else:
        # If form validation fails, re-render the form with errors
        return templates.TemplateResponse(
            "sample_form.html", {"request": request, "form": form}
        )


# Success endpoint
@app.get("/success")
async def success(request: Request):
    return {"message": "Form submitted successfully!"}


@app.get("/dashboard", response_class=HTMLResponse)
async def components(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
async def components(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
