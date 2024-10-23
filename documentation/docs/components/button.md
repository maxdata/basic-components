# Button

Displays a button or a component that looks like a button.


## Button 

=== "Preview"
    <iframe
    src="http://localhost:10000/components/button"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Button.jinja"
    ```jinja
    {% include-markdown "../../../components/ui/Button.jinja" %}
    ```
    

## Usage

```html
{% include-markdown "../../backend/templates/button.html" %}
```

## Examples

### Destructive

=== "Preview"
    <iframe
    src="http://localhost:10000/components/button?option=destructive"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/button_destructive.html" %}
    ```

### Outline

=== "Preview"
    <iframe
    src="http://localhost:10000/components/button?option=outline"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/button_outline.html" %}
    ```

### Secondary

=== "Preview"
    <iframe
    src="http://localhost:10000/components/button?option=secondary"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/button_secondary.html" %}
    ```

### Ghost

=== "Preview"
    <iframe
    src="http://localhost:10000/components/button?option=ghost"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/button_ghost.html" %}
    ```

### Link

=== "Preview"
    <iframe
    src="http://localhost:10000/components/button?option=link"
    style="width: 100%; height: 200px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/button_link.html" %}
    ```
