# Form

Components for forms with inputs, labels and validation styling.

## Preview

<iframe
src="{{ preview_url}}/components/form"
style="width: 100%; height: 200px; border: none;">
</iframe>

## Components

=== "Form.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/Form.jinja' %}
    ```
    {% endraw %}

=== "FormControl.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/FormControl.jinja' %}
    ```
    {% endraw %}

=== "FormDescription.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/FormDescription.jinja' %}
    ```
    {% endraw %}

=== "FormItem.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/FormItem.jinja' %}
    ```
    {% endraw %}

=== "FormLabel.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/FormLabel.jinja' %}
    ```
    {% endraw %}

=== "FormMessage.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/FormMessage.jinja' %}
    ```
    {% endraw %}

## Usage

```html
{% include-markdown "../../backend/templates/form.html" %}
```

## Examples 

### Errors 

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/form?option=errors"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/form_errors.html" %}
    ```
