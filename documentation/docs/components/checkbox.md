# Checkbox

A control that allows the user to toggle between checked and not checked.

## Preview

<iframe
src="{{ preview_url}}/components/checkbox"
style="width: 100%; height: 200px; border: none;">
</iframe>

## Props

| Name        | Type   | Default | Description                                            |
|-------------|--------|---------|--------------------------------------------------------|
| `className` | String |         | Additional tailwind classes to apply to the component. |
| `label`     | String |         | Text displayed for the label.                          |
| `checked`   | String | False   | Set the checked status of the component.               |
| `disabled`  | String | False   | Set the disabled status of the component.              |

## Components

=== "Checkbox.jinja"
{% raw %}
```jinja
{% include-markdown "../../../components/ui/Checkbox.jinja" %}
```
{% endraw %}

## Usage

```html
{% include-markdown "../../backend/templates/checkbox.html" %}
```
