# Select

Displays a list of options for the user to pick from—triggered by a button.

## Preview

<iframe
src="{{ preview_url}}/components/select"
style="width: 100%; height: 500px; border: none;">
</iframe>

The value of the selected item is stored in a hidden input field. 

## Props
| Component     | Prop          | Type           | Default  | Description                               |
|---------------|---------------|----------------|----------|-------------------------------------------|
| Select        | `name`        | String         | `""`     | The name attribute for the input field.   |
| Select        | `className`   | String         | `""`     | Additional CSS classes for customization. |
| SelectItem    | `value`       | String         | `""`     | The form value for the item.              |
| SelectLabel   | `className`   | String         | `""`     | Additional CSS classes for customization. |
| SelectTrigger | `className`   | String         | `""`     | Additional CSS classes for customization. |
| SelectValue   | `placeholder` | String         | `""`     | The placeholder text.                     |

## Components

=== "Select.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/Select.jinja' %}
    ```
    {% endraw %}

=== "SelectContent.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SelectContent.jinja' %}
    ```
    {% endraw %}

=== "SelectGroup.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SelectGroup.jinja' %}
    ```
    {% endraw %}

=== "SelectItem.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SelectItem.jinja' %}
    ```
    {% endraw %}

=== "SelectLabel.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SelectLabel.jinja' %}
    ```
    {% endraw %}

=== "SelectScrollDownButton.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SelectScrollDownButton.jinja' %}
    ```
    {% endraw %}

=== "SelectScrollUpButton.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SelectScrollUpButton.jinja' %}
    ```
    {% endraw %}

=== "SelectTrigger.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SelectTrigger.jinja' %}
    ```
    {% endraw %}

=== "SelectValue.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/SelectValue.jinja' %}
    ```
    {% endraw %}

## Usage

```html
{% include-markdown "../../backend/templates/select.html" %}

```

## Example

### Scrollable

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/select?option=scrollable"
    style="width: 100%; height: 500px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/select_scrollable.html" %}
    ```
