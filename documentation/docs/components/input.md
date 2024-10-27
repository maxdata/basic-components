# Form

Displays a form input field.

## Preview

<iframe
src="{{ preview_url}}/components/input"
style="width: 100%; height: 200px; border: none;">
</iframe>

## Props

| Prop           | Type           | Default  | Description                                                    |
|----------------|----------------|----------|----------------------------------------------------------------|
| `name`         | String         | `""`     | The name attribute for the input field.                        |
| `type`         | String         | `"text"` | Specifies the type of input (e.g., `text`, `password`).        |
| `value`        | String         | `""`     | The initial value of the input.                                |
| `placeholder`  | String         | `""`     | Placeholder text shown inside the input.                       |
| `autocomplete` | Optional[String] | `""` | Determines if autocomplete is enabled for the input.           |
| `required`     | Boolean        | `False`  | Marks the input as required.                                   |
| `className`    | String         | `""`     | Additional CSS classes for customization.                      |
| `disabled`     | Boolean        | `False`  | Disables the input if `True`.                                  |
| `error`        | Boolean        | `False`  | Applies error styling if `True`.                               |

## Components

=== "Input.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/Input.jinja' %}
    ```
    {% endraw %}


## Usage

```html
{% include-markdown "../../backend/templates/input.html" %}
```

## Examples 

### Errors 

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/input?option=error"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/input_error.html" %}
    ```

### Disabled

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/input?option=disabled"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/input_disabled.html" %}
    ```

### Label

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/input?option=label"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/input_label.html" %}
    ```
