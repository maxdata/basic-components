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

## Usage
</Prose>

<IncludeTemplate template="examples/accordion.html"/>

<Prose>
## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />


