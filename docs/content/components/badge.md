---
title: Badge
description: Displays a badge or a component that looks like a badge.
templates:
  - Badge.jinja

examples:  
  - Destructive: examples/badge_destructive.html 
  - Outline: examples/badge_outline.html 
  - Secondary: examples/badge_secondary.html 
---

<TabPreview component="Badge" template="examples/badge.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Badge" component="badge"/>

<Prose>

## Usage
</Prose>

<IncludeFile dir="docs/templates" file_name="examples/badge.html"/>

<Prose>
## Attributes

| Name        | Type   | Default     | Description                                                       |
|-------------|--------|-------------|-------------------------------------------------------------------|
| `variant`   | String | `"default"` | Sets the component style. Available: `default`, `secondary`, etc. |

## Code
</Prose>

<IncludeComponents dir="badge" :components="{{ metadata.templates }}" />

<Prose>

## Examples

</Prose>

<Prose>

### Destructive

</Prose>

<TabPreview component="Destructive" template="examples/badge_destructive.html"/>


<Prose>

### Outline

</Prose>

<TabPreview component="Outline" template="examples/badge_outline.html"/>


<Prose>

### Secondary

</Prose>

<TabPreview component="Secondary" template="examples/badge_secondary.html"/>
