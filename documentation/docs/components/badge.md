# Badge

Displays a badge or a component that looks like a badge.

## Badge 

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/badge"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Badge.jinja"
{% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/Badge.jinja" %}
    ```
{% endraw %}    

## Usage

```html
{% include-markdown "../../backend/templates/badge.html" %}
```

## Examples

### Destructive

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/badge?option=destructive"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/badge_destructive.html" %}
    ```

### Outline

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/badge?option=outline"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/badge_outline.html" %}
    ```

### Secondary

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/badge?option=secondary"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/badge_secondary.html" %}
    ```
