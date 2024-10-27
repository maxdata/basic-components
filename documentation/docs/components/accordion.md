# Accordion

The Accordion component is used to display collapsible sections of content. It allows users to toggle between hiding and showing content, making it useful for FAQs, expandable lists, and more.

## Preview

<iframe
src="{{ preview_url}}/components/accordion"
style="width: 100%; height: 300px; border: none;">
</iframe>

## Props

| Name        | Type    | Default     | Description                                            |
|-------------|---------|-------------|--------------------------------------------------------|
| `className` | String  |             | Additional tailwind classes to apply to the component. |

## Components

=== "Accordion.jinja"
{% raw %}
    ```jinja
    {% include '../../../components/ui/Accordion.jinja' %}
    ```
{% endraw %}

=== "AccordionContent.jinja"
{% raw %}
    ```jinja
    {% include '../../../components/ui/AccordionContent.jinja' %}
    ```
{% endraw %}

=== "AccordionItem.jinja"
{% raw %}
    ```jinja
    {% include '../../../components/ui/AccordionItem.jinja' %}
    ```
{% endraw %}    

=== "AccordionTrigger.jinja"
{% raw %}
    ```jinja
    {% include '../../../components/ui/AccordionTrigger.jinja' %}
    ```
{% endraw %}

## Usage

```html
{% include-markdown "../../backend/templates/accordion.html" %}
```
