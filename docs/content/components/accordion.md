---
title: Accordion
description: A vertically stacked set of interactive headings that each reveal a section of content.
component: accordion
templates:  
  - Accordion.jinja
  - AccordionContent.jinja
  - AccordionItem.jinja
  - AccordionTrigger.jinja
---

<TabPreview component="Accordion" template="examples/accordion.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Accordion" component="accordion"/>

<Prose>

## Usage
</Prose>

<IncludeFile dir="docs/templates" file_name="examples/accordion.html"/>

<Prose>
## Code
</Prose>

<IncludeComponents dir="accordion" :components="{{ metadata.templates }}" />


