# Sheet

Extends the Dialog component to display content that complements the main content of the screen.

## Preview

<iframe
src="{{ preview_url}}/components/Sheet"
style="width: 100%; height: 400px; border: none;">
</iframe>

The value of the Sheeted item is stored in a hidden input field. 

## Props

| Component        | Prop        | Type   | Default           | Description                                    |
|------------------|-------------|--------|-------------------|------------------------------------------------|
| Sheet            | `id`        | String | `"sheet"`         | Unique identifier for the sheet component.     |
| SheetClose       | `id`        | String | `"sheet-close"`   | Unique identifier for the close button.        |
| SheetClose       | `className` | String | `""`              | Additional CSS classes for customization.      |
| SheetContent     | `id`        | String | `"sheet-content"` | Unique identifier for the content.             |
| SheetContent     | `side`      | String | `"right"`         | Position of the sheet (top/bottom/left/right). |
| SheetContent     | `className` | String | `""`              | Additional CSS classes for customization.      |
| SheetDescription | `className` | String | `""`              | Additional CSS classes for customization.      |
| SheetFooter      | `className` | String | `""`              | Additional CSS classes for customization.      |
| SheetHeader      | `className` | String | `""`              | Additional CSS classes for customization.      |
| SheetOverlay     | `className` | String | `""`              | Additional CSS classes for customization.      |
| SheetTitle       | `className` | String | `""`              | Additional CSS classes for customization.      |
| SheetTrigger     | `className` | String | `""`              | Additional CSS classes for customization.      |

## Components

=== "Sheet.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/Sheet.jinja' %}
    ```
    {% endraw %}

=== "SheetClose.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SheetClose.jinja' %}
    ```
    {% endraw %}

=== "SheetContent.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SheetContent.jinja' %}
    ```
    {% endraw %}

=== "SheetDescription.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SheetDescription.jinja' %}
    ```
    {% endraw %}


=== "SheetFooter.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SheetFooter.jinja' %}
    ```
    {% endraw %}

=== "SheetHeader.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SheetHeader.jinja' %}
    ```
    {% endraw %}

=== "SheetOverlay.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SheetOverlay.jinja' %}
    ```
    {% endraw %}

=== "SheetTitle.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SheetTitle.jinja' %}
    ```
    {% endraw %}

=== "SheetTrigger.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SheetTrigger.jinja' %}
    ```
    {% endraw %}

## Usage

```html
{% include-markdown "../../backend/templates/sheet.html" %}

```

## Example

### Sides

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/sheet?option=side"
    style="width: 100%; height: 500px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/sheet_side.html" %}
    ```
