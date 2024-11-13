---
title: Alert Dialog
description: A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.
templates:
  - AlertDialog.jinja
  - AlertDialogBody.jinja
  - AlertDialogClose.jinja
  - AlertDialogFooter.jinja
  - AlertDialogHeader.jinja
  - AlertDialogOverlay.jinja
  - AlertDialogTitle.jinja
  - AlertDialogTrigger.jinja
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

<IncludeComponents dir="alert_dialog" :components="{{ metadata.templates }}" />
