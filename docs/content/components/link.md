---
title: Link
description: Displays a link.
templates:
  - Link.jinja
---

<TabPreview component="Link" template="examples/link.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Link" component="link"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/link.html"/>

<Prose>

## Attributes

| Prop        | Type    | Default | Description                               |
|-------------|---------|--|-------------------------------------------|
| `href`      | String  |  | The url for the link.                     |
| `className` | String  |  | Additional CSS classes for customization. |


## Code
</Prose>

<IncludeComponents dir="link" :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<TabPreview component="Icon" template="examples/link_icon.html"/>
