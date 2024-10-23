# Accordion

The Accordion component is used to display collapsible sections of content. It allows users to toggle between hiding and showing content, making it useful for FAQs, expandable lists, and more.

## Accordion

=== "Preview"
    <iframe
    src="http://localhost:10000/components/accordion"
    style="width: 100%; height: 300px; border: none;">
    </iframe>

=== "Accordion.jinja"
    ```jinja
    {% include '../../../components/ui/Accordion.jinja' %}
    ```
=== "AccordionContent.jinja"
    ```jinja
    {% include '../../../components/ui/AccordionContent.jinja' %}
    ```
=== "AccordionItem.jinja"
    ```jinja
    {% include '../../../components/ui/AccordionItem.jinja' %}
    ```
=== "AccordionTrigger.jinja"
    ```jinja
    {% include '../../../components/ui/AccordionTrigger.jinja' %}
    ```

## Usage

```html
{% include-markdown "../../backend/templates/accordion.html" %}
```
