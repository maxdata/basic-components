---
title: Checkbox
description: A control that allows the user to toggle between checked and not checked.
templates:
  - Checkbox.jinja
---


<TabPreview component="Checkbox" template="examples/Checkbox.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Checkbox" component="checkbox"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/checkbox.html"/>

<Prose>

## Attributes

| Name        | Type   | Default | Description                                            |
|-------------|--------|---------|--------------------------------------------------------|
| `className` | String |         | Additional tailwind classes to apply to the component. |
| `label`     | String |         | Text displayed for the label.                          |
| `checked`   | String | False   | Set the checked status of the component.               |
| `disabled`  | String | False   | Set the disabled status of the component.              |

## Code
</Prose>

<IncludeComponents dir="checkbox" :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<Prose>

### Disabled

</Prose>

<TabPreview component="Disabled" template="examples/checkbox_disabled.html"/>
