---
title: Radio Group
description: A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.
component: radio_group
templates:
  - RadioGroup.jinja
  - RadioGroupItem.jinja
---

<TabPreview component="Radio Group" template="examples/radio_group.html"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/alert.html"/>

<Prose>

## Code
</Prose>

<IncludeComponents dir="radio" :components="{{ metadata.templates }}" />
