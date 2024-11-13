# app.py
from pathlib import Path
from flask import Flask
import jinja2
import jinjax

# Initialize Flask
app = Flask(__name__)

# Configure Jinja environment with JinjaX
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"), extensions=[jinjax.JinjaX]
)

# Setup JinjaX catalog
catalog = jinjax.Catalog(jinja_env=env)

# Base components directory
components_dir = Path("components/ui")

# Register each component subdirectory first
for component_dir in components_dir.iterdir():
    if component_dir.is_dir():
        catalog.add_folder(str(component_dir))


# Add catalog to Jinja globals
env.globals["catalog"] = catalog


# Routes
@app.route("/")
def index():
    return env.get_template("index.html").render()


@app.route("/button")
def button():
    """Example endpoint for HTMX updates."""
    return catalog.render("Button", variant="destructive", _content="HTMX IS ENABLED!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
