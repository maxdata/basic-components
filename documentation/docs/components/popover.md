# Popover

Displays rich content in a portal, triggered by a button.

## Preview

<iframe
src="{{ preview_url}}/components/popover"
style="width: 100%; height: 400px; border: none;">
</iframe>

## Components

=== "Popover.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/Popover.jinja' %}
    ```
    {% endraw %}

=== "PopoverContent.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/PopoverContent.jinja' %}
    ```
    {% endraw %}

=== "PopoverTrigger.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/PopoverTrigger.jinja' %}
    ```
    {% endraw %}

## Usage

```html
{% include-markdown "../../backend/templates/popover.html" %}

```

## Examples

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/popover?option=content"
    style="width: 100%; height: 600px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/popover_content.html" %}
    ```
