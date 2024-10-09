from fastapi import FastAPI, Request
from jinja2.ext import DebugExtension
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import jinjax
from pathlib import Path
from wtforms import Form, StringField, PasswordField, validators
from starlette_wtf import StarletteForm, CSRFProtectMiddleware

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

print(f"BASE_DIR={BASE_DIR}")
templates = Jinja2Templates(directory="templates")
templates.env.add_extension(DebugExtension)

templates.env.add_extension(jinjax.JinjaX)  # pyright: ignore [reportPrivateImportUsage]
catalog = jinjax.Catalog(jinja_env=templates.env)  # pyright: ignore [reportPrivateImportUsage]
catalog.add_folder(f"{BASE_DIR}/components/ui")
catalog.add_folder(f"{BASE_DIR}/examples")

# Serve static files (CSS, etc.)
app.mount("/dist", StaticFiles(directory="dist"), name="dist")
app.mount("/icons", StaticFiles(directory="node_modules/lucide-static/icons"), name="icons")
app.mount("/lucide-static", StaticFiles(directory="node_modules/lucide-static/"), name="lucide-static")

# CSRF Middleware
app.add_middleware(SessionMiddleware, secret_key="session_key")
app.add_middleware(CSRFProtectMiddleware,csrf_secret="your_secret_key_here" )


@app.get("/", response_class=HTMLResponse)
async def components(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



class SampleForm(StarletteForm):
    username = StringField('Username', [validators.InputRequired(), validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.InputRequired(), validators.Email()], description="an email is an email")
    password = PasswordField('Password', [validators.InputRequired()])


@app.get("/form", response_class=HTMLResponse)
async def display_form(request: Request):
    form = SampleForm(request)
    return templates.TemplateResponse("sample_form.html", {"request": request, "form": form})

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
        return templates.TemplateResponse("sample_form.html", {"request": request, "form": form})


# Success endpoint
@app.get("/success")
async def success(request: Request):
    return {"message": "Form submitted successfully!"}
