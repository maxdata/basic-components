# Link

Displays a link.

## Preview

<iframe
src="{{ preview_url}}/components/link"
style="width: 100%; height: 200px; border: none;">
</iframe>

## Props

| Prop        | Type    | Default | Description                               |
|-------------|---------|---------|-------------------------------------------|
| `href`      | String  | `#`     | The url for the link.                     |
| `className` | String  | `""`    | Additional CSS classes for customization. |

## Components

=== "Link.jinja"
{% raw %}
```jinja
{% include '../../../components/ui/Link.jinja' %}
```
{% endraw %}

## Usage

```html
{% include-markdown "../../backend/templates/link.html" %}
```

## Examples

### Icon

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/link?option=icon"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/link_icon.html" %}
    ```
