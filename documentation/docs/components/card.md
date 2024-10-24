# Card

Displays a card with header, content, and footer.

## Card

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/card"
    style="width: 100%; height: 300px; border: none;">
    </iframe>

=== "Card.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/Card.jinja' %}
    ```
    {% endraw %}

=== "CardContent.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/CardContent.jinja' %}
    ```
    {% endraw %}

=== "CardDescription.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/CardDescription.jinja' %}
    ```
    {% endraw %}

=== "CardFooter.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/CardFooter.jinja' %}
    ```
    {% endraw %}

=== "CardHeader.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/CardHeader.jinja' %}
    ```
    {% endraw %}

=== "CardTitle.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/CardTitle.jinja' %}
    ```
    {% endraw %}


## Usage

```html
{% include-markdown "../../backend/templates/card.html" %}
```

## Examples


=== "Preview"
    <iframe
    src="{{ preview_url}}/components/card?option=example"
    style="width: 100%; height: 600px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/card_example.html" %}
    ```
