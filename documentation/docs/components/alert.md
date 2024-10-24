# Alert

Displays a callout for user attention.

## Alert

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/alert"
    style="width: 100%; height: 300px; border: none;">
    </iframe>

=== "Alert.jinja"
{% raw %}
    ```jinja
    {% include '../../../components/ui/Alert.jinja' %}
    ```
{% endraw %}

=== "AlertDescription.jinja"
{% raw %}
    ```jinja
    {% include '../../../components/ui/AlertDescription.jinja' %}
    ```
{% endraw %}

=== "AlertDialogContent.jinja"
{% raw %}
    ```jinja
    {% include '../../../components/ui/AlertDialogContent.jinja' %}
    ```
{% endraw %}    


## Usage

```html
{% include-markdown "../../backend/templates/alert.html" %}
```

## Examples 

### Destructive 

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/alert?option=destructive"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/alert_destructive.html" %}
    ```
