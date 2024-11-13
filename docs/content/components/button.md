---
title: Button
description: Displays a button.
component: button
templates:  
  - Button.jinja 
---

<TabPreview component="Button" template="examples/button.html"/>

<Prose>

## Usage
</Prose>

<IncludeFile dir="docs/templates" file_name="examples/button.html"/>

<Prose>

## Attributes

| Name        | Type    | Default     | Description                                                           |
|-------------|---------|-------------|-----------------------------------------------------------------------|
| `className` | String  |             | Additional tailwind classes to apply to the component.                |
| `variant`   | String  | `"default"` | Sets the button style. Available: `default`, `outline`, `ghost`, etc. |
| `size`      | String  | `"default"` | Size of the button: `sm`, `lg`, `icon`.                               |
| `disabled`  | Boolean | `False`     | Disables the button if `True`.                                        |

## Code
</Prose>

<IncludeComponents dir="button" :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<Prose>

### Destructive

</Prose>

<TabPreview component="Destructive" template="examples/button_destructive.html"/>

<Prose>

### Outline

</Prose>

<TabPreview component="Outline" template="examples/button_outline.html"/>

<Prose>

### Secondary

</Prose>

<TabPreview component="Secondary" template="examples/button_secondary.html"/>

<Prose>

### Ghost

</Prose>

<TabPreview component="Ghost" template="examples/button_ghost.html"/>

<Prose>

### Link

</Prose>
<TabPreview component="Link" template="examples/button_link.html"/>

