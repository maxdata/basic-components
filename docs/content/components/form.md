---
title: Form
description: Components for forms with inputs, labels and validation styling.
templates:
  - Form.jinja
  - FormControl.jinja
  - FormDescription.jinja
  - FormItem.jinja
  - FormLabel.jinja
  - FormMessage.jinja
---

<TabPreview component="Form" template="examples/form.html"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/form.html"/>

<Prose>

## Code
</Prose>

<IncludeComponents dir="form" :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<Prose>

### Errors

</Prose>

<TabPreview component="Errors" template="examples/form_errors.html"/>
