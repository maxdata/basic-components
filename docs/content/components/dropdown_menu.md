---
title: Dropdown Menu
description: Displays a menu to the user — such as a set of actions or functions — triggered by a button.
templates:
  - DropdownMenu.jinja
  - DropdownMenuCheckboxItem.jinja
  - DropdownMenuContent.jinja
  - DropdownMenuGroup.jinja
  - DropdownMenuItem.jinja
  - DropdownMenuLabel.jinja
  - DropdownMenuRadioItem.jinja
  - DropdownMenuSeparator.jinja
  - DropdownMenuSub.jinja
  - DropdownMenuSubContent.jinja
  - DropdownMenuSubTrigger.jinja
  - DropdownMenuTrigger.jinja
---

<TabPreview component="Alert" template="examples/dropdown_menu.html"/>

<Prose>

## Installation

</Prose>

<Installation name="Dropdown Menu" component="dropdown_menu"/>

<Prose>

## Usage

</Prose>

<IncludeFile dir="docs/templates" file_name="examples/dropdown_menu.html"/>

<Prose>

## Code
</Prose>

<IncludeComponents dir="dropdown_menu" :components="{{ metadata.templates }}" />
