---
title: Input
description: Displays a form input field.
templates:
  - Input.jinja
examples:  
  - Error: examples/input_error.html 
  - Disabled: examples/input_disabled.html 
  - Label: examples/input_label.html 
  - File: examples/input_file.html 
  - Button: examples/input_button.html 
  - Disabled: examples/input_disabled.html 
---

<TabPreview component="Input" template="examples/input.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Input" component="input"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/input.html"/>

<Prose>

## Attributes

| Prop           | Type           | Default  | Description                                                    |
|----------------|----------------|----------|----------------------------------------------------------------|
| `name`         | String         | `""`     | The name attribute for the input field.                        |
| `type`         | String         | `"text"` | Specifies the type of input (e.g., `text`, `password`).        |
| `value`        | String         | `""`     | The initial value of the input.                                |
| `placeholder`  | String         | `""`     | Placeholder text shown inside the input.                       |
| `autocomplete` | Optional[String] | `""` | Determines if autocomplete is enabled for the input.           |
| `required`     | Boolean        | `False`  | Marks the input as required.                                   |
| `className`    | String         | `""`     | Additional CSS classes for customization.                      |
| `disabled`     | Boolean        | `False`  | Disables the input if `True`.                                  |
| `error`        | Boolean        | `False`  | Applies error styling if `True`.                               |

## Code
</Prose>

<IncludeComponents dir="input" :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<Prose>

### Button

</Prose>
<TabPreview component="Button" template="examples/input_button.html"/>

<Prose>

### Disabled

</Prose>
<TabPreview component="Disabled" template="examples/input_disabled.html"/>

<Prose>

### Error

</Prose>
<TabPreview component="Error" template="examples/input_error.html"/>

<Prose>

### File

</Prose>
<TabPreview component="File" template="examples/input_file.html"/>

<Prose>

### Label

</Prose>
<TabPreview component="Label" template="examples/input_label.html"/>

<Prose>

### Peer Disabled

</Prose>
<TabPreview component="Peer Disabled" template="examples/input_peer_disabled.html"/>
