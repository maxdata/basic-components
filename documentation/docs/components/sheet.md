# Sheet

Displays content one side of the screen in a modal dialog.

## Preview

<iframe
src="{{ preview_url}}/components/Sheet"
style="width: 100%; height: 400px; border: none;">
</iframe>

## Props

| Component        | Prop        | Type   | Default           | Description                                    |
|------------------|-------------|--------|-------------------|------------------------------------------------|
| Sheet            | `className` | String | `"sheet"`         | Additional CSS classes for customization.      |
| SheetClose       | `className` | String | `"sheet-close"`   | Additional CSS classes for customization.      |
| SheetClose       | `className` | String | `""`              | Additional CSS classes for customization.      |
| SheetContent     | `className` | String | `"sheet-content"` | Additional CSS classes for customization.      |
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
