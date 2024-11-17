---
title: Popover
description: Displays rich content in a portal, triggered by a button.
templates:
  - Popover.jinja
  - PopoverContent.jinja
  - PopoverTrigger.jinja
---

<TabPreview component="Popover" template="examples/popover.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Popover" component="popover"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/popover.html"/>

<Prose>

## Attributes

| Name        | Type    | Default     | Description                                                           |
|-------------|---------|-------------|-----------------------------------------------------------------------|
| `variant`   | String  | `"default"` | Sets the button style. Available: `default`, `outline`, `ghost`, etc. |


## Code
</Prose>

<IncludeComponents dir="popover" :components="{{ metadata.templates }}" />



