# Toast

A succinct message that is displayed temporarily.

## Preview

<iframe
src="{{ preview_url}}/components/toast"
style="width: 100%; height: 200px; border: none;">
</iframe>

## Props

| Component    | Prop           | Type   | Default     | Description                                                                                             |
|--------------|----------------|--------|-------------|---------------------------------------------------------------------------------------------------------|
| Toast        | `id`           | String |             | The css id for the Toast.                                                                               |
| Toast        | `className`    | String | `""`        | Additional CSS classes for the toast container.                                                         |
| Toast        | `duration`     | Number | `30000`     | Duration in milliseconds before toast auto-dismisses.                                                   |
| ToastContent | `type`         | String | `"default"` | Style variant of the toast. Options: `"default"`, `"success"`, `"error"`, `"warning"`, `"destructive"`. |
| ToastContent | `title`        | String | `""`        | The title text displayed in the toast.                                                                  |
| ToastContent | `description`  | String | `""`        | The description text displayed below the title.                                                         |
| ToastTrigger | `className`    | String | `""`        | Additional CSS classes for the trigger button.                                                          |
| ToastTrigger | `variant`      | String | `"default"` | The Button component variant to use.                                                                    |
| ToastTrigger | `toast_target` | String |             | The target toast identifier to trigger.                                                                 |

Toast components require an `id` so that the dispatch event can call the component to display it. 

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
