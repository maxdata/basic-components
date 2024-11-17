---
title: Sheet
description: Displays content on one side of the screen in a modal dialog.
templates:
  - Sheet.jinja
  - SheetClose.jinja
  - SheetContent.jinja
  - SheetDescription.jinja
  - SheetFooter.jinja
  - SheetHeader.jinja
  - SheetOverlay.jinja
  - SheetTitle.jinja
  - SheetTrigger.jinja
---

<TabPreview component="Alert" template="examples/sheet.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Sheet" component="sheet"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/alert.html"/>

<Prose>

## Attributes

| Component        | Prop        | Type   | Default           | Description                                    |
|------------------|-------------|--------|-------------------|------------------------------------------------|
| SheetContent     | `side`      | String | `"right"`         | Position of the sheet (top/bottom/left/right). |


## Code
</Prose>

<IncludeComponents dir="sheet" :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<Prose>

## Sides

</Prose>

<TabPreview component="Sides" template="examples/sheet_side.html"/>
