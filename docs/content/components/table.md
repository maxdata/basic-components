---
title: Table
description: A responsive table component.
templates:
  - Table.jinja
  - TableBody.jinja
  - TableCaption.jinja
  - TableCell.jinja
  - TableFooter.jinja
  - TableHead.jinja
  - TableHeader.jinja
  - TableRow.jinja
---

<TabPreview component="Table" template="examples/table.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Table" component="table"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/table.html"/>

<Prose>

## Attributes

| Component    | Prop        | Type   | Default | Description                                                |
|--------------|-------------|--------|---------|------------------------------------------------------------|
| TableHead    | `sortable`  | bool   | `False` | Displays and indicator if table is sortable by this colum. |
| TableHead    | `ascending` | bool   | `True`  | True if the order is ascending.                            |

## Code
</Prose>

<IncludeComponents dir="table" :components="{{ metadata.templates }}" />

