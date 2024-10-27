# Label

Displays a label for a form field.

## Preview

<iframe
src="{{ preview_url}}/components/label"
style="width: 100%; height: 200px; border: none;">
</iframe>

## Props

| Prop        | Type    | Default | Description                               |
|-------------|---------|---------|-------------------------------------------|
| `htmlFor`   | String  | `False` | The id of the field the label refers to.  |
| `className` | String  | `""`    | Additional CSS classes for customization. |

## Components

=== "Label.jinja"
{% raw %}
```jinja
{% include '../../../components/ui/Label.jinja' %}
```
{% endraw %}

## Usage

```html
{% include-markdown "../../backend/templates/label.html" %}
```
