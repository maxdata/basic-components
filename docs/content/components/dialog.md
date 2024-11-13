---
title: Dialog
description: A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.
templates:
  - Dialog.jinja
  - DialogBody.jinja
  - DialogClose.jinja
  - DialogFooter.jinja
  - DialogHeader.jinja
  - DialogOverlay.jinja
  - DialogTitle.jinja
  - DialogTrigger.jinja
---

<TabPreview component="Dialog" template="examples/dialog.html"/>

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
