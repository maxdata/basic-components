from pydantic import BaseModel, HttpUrl
from typing import List, Union

from docs.config import settings


class NavItem(BaseModel):
    type: str = "item"
    group: str = None
    title: str
    href: str


class NavGroup(BaseModel):
    type: str = "group"
    title: str
    items: List[Union[NavItem, "NavGroup"]]


class SiteConfig(BaseModel):
    """The top-level configuration for the site."""

    site_name: str
    repo_url: HttpUrl
    mainNav: List[NavItem]
    sidebarNav: List[Union[NavItem, NavGroup]]


config = {
    "site_name": settings.APP_NAME,
    "repo_url": "https://github.com/basicmachines-co/basic-components",
    "mainNav": [
        {"title": "Docs", "group": "/docs", "href": "/docs/introduction"},
        {
            "title": "Components",
            "group": "/components",
            "href": "/components/accordion",
        },
        {"title": "Examples", "group": "/examples", "href": "/examples"},
    ],
    "sidebarNav": [
        {
            "title": "Getting Started",
            "items": [
                {"title": "Introduction", "href": "/docs/introduction"},
                {"title": "Installation", "href": "/docs/installation"},
                {"title": "Components", "href": "/docs/components"},
                {"title": "HTMX", "href": "/docs/htmx"},
                {"title": "Dark Mode", "href": "/docs/dark_mode"},
                {"title": "CLI", "href": "/docs/cli"},
                {"title": "Typography", "href": "/docs/typography"},
                {"title": "About", "href": "/docs/about"},
                {"title": "Contribution", "href": "/docs/contribution"},
                {"title": "Changelog", "href": "/docs/changelog"},
            ],
        },
        {
            "title": "Installation",
            "items": [
                {"title": "Fastapi", "href": "/docs/fastapi"},
                {"title": "Flask", "href": "/docs/fastapi"},
                {"title": "Django", "href": "/docs/django"},
            ],
        },
        {
            "title": "Components",
            "items": [
                {"title": "Accordion", "href": "/components/accordion"},
                {"title": "Alert", "href": "/components/alert"},
                {"title": "Badge", "href": "/components/Badge"},
                {"title": "Button", "href": "/components/button"},
                {"title": "Card", "href": "/components/card"},
                {"title": "Checkbox", "href": "/components/checkbox"},
                {"title": "Dialog", "href": "/components/dialog"},
                {"title": "Dropdown Menu", "href": "/components/dropdown_menu"},
                {"title": "Form", "href": "/components/form"},
                {"title": "Input", "href": "/components/input"},
                {"title": "Label", "href": "/components/label"},
                {"title": "Mode Toggle", "href": "/components/mode_toggle"},
                {"title": "Popover", "href": "/components/popover"},
                {"title": "Radio Group", "href": "/components/radio_group"},
                {"title": "Select", "href": "/components/select"},
                {"title": "Sheet", "href": "/components/sheet"},
                {"title": "Table", "href": "/components/table"},
                {"title": "Textarea", "href": "/components/textarea"},
                {"title": "Toast", "href": "/components/toast"},
            ],
        },
        {
            "title": "Extras",
            "items": [
                {"title": "WTForm", "href": "/components/wtform"},
                {"title": "Icons", "href": "/components/icons"},
            ],
        },
    ],
}

site_config = SiteConfig.model_validate(config)
