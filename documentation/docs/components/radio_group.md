# RadioGroup

A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.

## Preview

<iframe
src="{{ preview_url}}/components/radio_group"
style="width: 100%; height: 400px; border: none;">
</iframe>

## Components

=== "RadioGroup.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/RadioGroup.jinja' %}
    ```
    {% endraw %}

=== "RadioGroupItem.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/RadioGroupItem.jinja' %}
    ```
    {% endraw %}

## Usage

```html
{% include-markdown "../../backend/templates/radio_group.html" %}

```
