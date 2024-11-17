---
title: Dialog
description: A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.
templates:
  - Dialog.jinja
  - DialogClose.jinja
  - DialogContent.jinja
  - DialogDescription.jinja
  - DialogFooter.jinja
  - DialogHeader.jinja
  - DialogOverlay.jinja
  - DialogPortal.jinja
  - DialogTitle.jinja
  - DialogTrigger.jinja
---

<TabPreview component="Dialog" template="examples/dialog.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Dialog" component="dialog"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/dialog.html"/>

<Prose>

## Attributes

| Prop      | Type   | Default  | Description                            |
|-----------|--------|----------|----------------------------------------|
| `open`    | Bool   | `False`  | Controls the visibility of the dialog. |

## Code
</Prose>

<IncludeComponents dir="dialog" :components="{{ metadata.templates }}" />

<Prose>

## Examples

### Custom close button

</Prose>

<TabPreview component="Custom close Button" template="examples/dialog_close_button.html"/>
