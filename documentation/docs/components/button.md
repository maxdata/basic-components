# Button

Displays a button or a component that looks like a button.


## Preview

<iframe
src="{{ preview_url}}/components/button"
style="width: 100%; height: 200px; border: none;">
</iframe>

## Props

| Name        | Type    | Default | Description                                                           |
|-------------|---------|------|-----------------------------------------------------------------------|
| `className` | String  |  | Additional tailwind classes to apply to the button.                   |
| `variant`   | String  | `"default"` | Sets the button style. Available: `default`, `outline`, `ghost`, etc. |
| `size`      | String  | `"default"` | Size of the button: `sm`, `lg`, `icon`.                               |
| `disabled`  | Boolean | `False` | Disables the button if `True`.                                        |

## Components

=== "Button.jinja"
{% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/Button.jinja" %}
    ```
{% endraw %}
    

## Usage

```html
{% include-markdown "../../backend/templates/button.html" %}
```

## Examples

### Destructive

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/button?option=destructive"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/button_destructive.html" %}
    ```

### Outline

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/button?option=outline"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/button_outline.html" %}
    ```

### Secondary

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/button?option=secondary"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/button_secondary.html" %}
    ```

### Ghost

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/button?option=ghost"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/button_ghost.html" %}
    ```

### Link

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/button?option=link"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/button_link.html" %}
    ```
