# Table

A responsive table component.

## Preview

<iframe
src="{{ preview_url}}/components/table"
style="width: 100%; height: 600px; border: none;">
</iframe>

## Props

| Component    | Prop        | Type   | Default | Description                                                |
|--------------|-------------|--------|---------|------------------------------------------------------------|
| Table        | `className` | String | `""`    | Additional CSS classes for customization.                  |
| TableBody    | `className` | String | `""`    | Additional CSS classes for customization.                  |
| TableCaption | `className` | String | `""`    | Additional CSS classes for customization.                  |
| TableCell    | `className` | String | `""`    | Additional CSS classes for customization.                  |
| TableFooter  | `className` | String | `""`    | Additional CSS classes for customization.                  |
| TableHead    | `className` | String | `""`    | Additional CSS classes for customization.                  |
| TableHead    | `sortable`  | bool   | `False` | Displays and indicator if table is sortable by this colum. |
| TableHead    | `sorted`    | String | `""`    | The name of the sort value.                                |
| TableHead    | `ascending` | bool   | `True`  | True if the order is ascending.                            |
| TableHeader  | `className` | String | `""`    | Additional CSS classes for customization.                  |
| TableHeader  | `className` | String | `""`    | Additional CSS classes for customization.                  |
| TableRow     | `className` | String | `""`    | Additional CSS classes for customization.                  |
| TableTitle   | `className` | String | `""`    | Additional CSS classes for customization.                  |
| TableTrigger | `className` | String | `""`    | Additional CSS classes for customization.                  |

## Components

=== "Table.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/Table.jinja' %}
    ```
    {% endraw %}

=== "TableBody.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/TableBody.jinja' %}
    ```
    {% endraw %}

=== "TableCaption.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/TableCaption.jinja' %}
    ```
    {% endraw %}

=== "TableCell.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/TableCell.jinja' %}
    ```
    {% endraw %}


=== "TableFooter.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/TableFooter.jinja' %}
    ```
    {% endraw %}

=== "TableHead.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/TableHead.jinja' %}
    ```
    {% endraw %}

=== "TableHeader.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/TableHeader.jinja' %}
    ```
    {% endraw %}

=== "TableRow.jinja"
    {% raw %}
    ```jinja
    {% include '../../../components/ui/TableRow.jinja' %}
    ```
    {% endraw %}


## Usage
{% raw %}   

```html
{% include-markdown "../../backend/templates/table.html" %}
```
{% endraw %}


## Examples

## Sorting 

Server side sorting is enabled via htmx using `hx-get`
```html
<th hx-get="/table?order_by=invoice&ascending=False" 
    hx-swap="outerHTML" 
    hx-target="#sorted-table">
    ...
</th>
```

The server side endpoint returns the html content to swap. 

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/table?option=sorting"
    style="width: 100%; height: 600px; border: none;">
    </iframe>


=== "Code"
{% raw %}   
    ```html
    {% include-markdown "../../backend/templates/table_sorting.html" %}
    ```
{% endraw %}   
