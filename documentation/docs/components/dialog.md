# Dialog Component

The `Dialog` component provides a modal interface for important interactions, confirmations, or notifications.

## Preview

<iframe
src="{{ preview_url}}/components/dialog"
style="width: 100%; height: 400px; border: none;">
</iframe>

## Props

| Prop      | Type   | Default  | Description                            |
|-----------|--------|----------|----------------------------------------|
| `open`    | Bool   | `False`  | Controls the visibility of the dialog. |

## Components

=== "Dialog.jinja"
    {% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/Dialog.jinja" %}
    ```
    {% endraw %}
=== "DialogBody.jinja"
    {% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/DialogBody.jinja" %}
    ```
    {% endraw %}
=== "DialogClose.jinja"
    {% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/DialogClose.jinja" %}
    ```
    {% endraw %}
=== "DialogContent.jinja"
    {% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/DialogContent.jinja" %}
    ```
    {% endraw %}
=== "DialogDescription.jinja"
    {% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/DialogDescription.jinja" %}
    ```
    {% endraw %}
=== "DialogFooter.jinja"
    {% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/DialogFooter.jinja" %}
    ```
    {% endraw %}
=== "DialogHeader.jinja"
    {% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/DialogHeader.jinja" %}
    ```
    {% endraw %}
=== "DialogOverlay.jinja"
    {% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/DialogOverlay.jinja" %}
    ```
    {% endraw %}
=== "DialogTitle.jinja"
    {% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/DialogTitle.jinja" %}
    ```
    {% endraw %}
=== "DialogTrigger.jinja"
    {% raw %}
    ```jinja
    {% include-markdown "../../../components/ui/DialogTrigger.jinja" %}
    ```
    {% endraw %}

## Usage 

```html
{% include-markdown "../../backend/templates/dialog.html" %}
```
