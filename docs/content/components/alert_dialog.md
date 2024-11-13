---
title: Alert Dialog
description: A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.
templates:
  - AlertDialog.jinja
  - AlertDialogAction.jinja
  - AlertDialogCancel.jinja
  - AlertDialogContent.jinja
  - AlertDialogDescription.jinja
  - AlertDialogFooter.jinja
  - AlertDialogHeader.jinja
  - AlertDialogOverlay.jinja
  - AlertDialogPortal.jinja
  - AlertDialogTrigger.jinja
  - AlertDialogTitle.jinja
---



<TabPreview component="Alert Dialog" template="examples/alert_dialog.html"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/alert_dialog.html"/>

<Prose>

## Code
</Prose>

<IncludeComponents dir="alert_dialog" :components="{{ metadata.templates }}" />
