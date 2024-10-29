# Toast

A succinct message that is displayed temporarily.

## Preview

<iframe
src="{{ preview_url}}/components/toast"
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

=== "Toast.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/Toast.jinja' %}
    ```
    {% endraw %}
=== "ToastContent.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/ToastContent.jinja' %}
    ```
    {% endraw %}
=== "ToastTrigger.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/ToastTrigger.jinja' %}
    ```
    {% endraw %}


## Usage
{% raw %}   

```html
{% include-markdown "../../backend/templates/toast.html" %}
```
{% endraw %}

## Examples

## Success

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/toast?option=success"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    {% raw %}   
    ```html
    {% include-markdown "../../backend/templates/toast_success.html" %}
    ```
    {% endraw %}   

## Warning

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/toast?option=warning"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    {% raw %}   
    ```html
    {% include-markdown "../../backend/templates/toast_warning.html" %}
    ```
    {% endraw %}   

## Error

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/toast?option=error"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    {% raw %}   
    ```html
    {% include-markdown "../../backend/templates/toast_error.html" %}
    ```
    {% endraw %}   

## Destructive

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/toast?option=destructive"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    {% raw %}   
    ```html
    {% include-markdown "../../backend/templates/toast_destructive.html" %}
    ```
    {% endraw %}   
