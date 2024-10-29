# Text Area

Displays a resizable form textarea.

## Preview

<iframe
src="{{ preview_url}}/components/textarea"
style="width: 100%; height: 200px; border: none;">
</iframe>

## Props

| Prop          | Type   | Default | Description                                 |
|---------------|--------|---------|---------------------------------------------|
| `className`   | String | `""`    | Additional CSS classes for customization.   |
| `value`       | String | `""`    | The value of the textarea                   |
| `placeholder` | String | `""`    | Placeholder text displayed in the textarea. |
| `disabled`    | bool   | `""`    | Disables the textarea                       |

## Components

=== "TextArea.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/Textarea.jinja' %}
    ```
    {% endraw %}


## Usage
{% raw %}   

```html
{% include-markdown "../../backend/templates/textarea.html" %}
```
{% endraw %}

## Examples

## Disabled 

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/textarea?option=disabled"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
{% raw %}   
    ```html
    {% include-markdown "../../backend/templates/textarea_disabled.html" %}
    ```
{% endraw %}   

## With Label

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/textarea?option=label"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    {% raw %}   
    ```html
    {% include-markdown "../../backend/templates/textarea_label.html" %}
    ```
    {% endraw %}   

## With Text

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/textarea?option=text"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    {% raw %}   
    ```html
    {% include-markdown "../../backend/templates/textarea_text.html" %}
    ```
    {% endraw %}   

## With Button

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/textarea?option=button"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    {% raw %}   
    ```html
    {% include-markdown "../../backend/templates/textarea_button.html" %}
    ```
    {% endraw %}   

## Form

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/textarea?option=form"
    style="width: 100%; height: 400px; border: none;">
    </iframe>

=== "Code"
    {% raw %}   
    ```html
    {% include-markdown "../../backend/templates/textarea_form.html" %}
    ```
    {% endraw %}   
