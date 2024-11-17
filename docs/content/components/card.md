---
title: Card
description: Displays a callout for user attention.
component: card
templates:
  - Card.jinja
  - CardContent.jinja
  - CardDescription.jinja
  - CardFooter.jinja
  - CardHeader.jinja
  - CardTitle.jinja
---

<TabPreview component="Card" template="examples/card.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Card" component="card"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/card.html"/>

<Prose>

## Code
</Prose>

<IncludeComponents dir="card" :components="{{ metadata.templates }}" />

<Prose>

## Examples
</Prose>

<Prose>

### Example

</Prose>


<TabPreview component="Example" template="examples/card_example.html"/>
