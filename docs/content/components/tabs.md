---
title: Tabs
description: A set of layered sections of content—known as tab panels—that are displayed one at a time.
templates:
  - Tabs.jinja
  - TabsContent.jinja
  - TabsList.jinja
  - TabsTrigger.jinja
---


<TabPreview component="Tabs" template="examples/tabs.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Tabs" component="tabs"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/tabs.html"/>

<Prose>

## Attributes

| Component | Prop           | Type   | Default | Description                      |
|-----------|----------------|--------|---------|----------------------------------|
| Tabs      | `defaultValue` | String | ``      | The default tab to display.      |
| TableHead | `id`           | String | ``      | Id of the tab panel.             |
| TableHead | `value`        | String | ``      | Name of the tab panel.           |
| TableHead | `id`           | String | ``      | Id of the tab panel to select.   |
| TableHead | `value`        | String | ``      | Name of the tab panel to select. |

## Code

</Prose>

<IncludeComponents dir="tabs" :components="{{ metadata.templates }}" />

