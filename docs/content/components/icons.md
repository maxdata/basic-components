---
title: Icons
description: Icons components from lucide.dev
---


<Prose>

Components are included for each of the icons in the <Link href="/https://lucide.dev/">Lucide</Link> icon library.

</Prose>


<TabPreview component="Icons" template="examples/icons.html"/>

<Prose>

## Attributes

| Prop        | Type   | Default   | Description                                         |
|-------------|--------|-----------|-----------------------------------------------------|
| `className` | String | `h-4 w-4` | Additional CSS classes for customization like size. |

## Search

</Prose>


<Card className="p-4">

<Input
    type="search"
    name="query"
    hx-get="/icons/search"
    hx-trigger="load, input changed delay:300ms, search"
    hx-target="#icons"
    hx-swap="outerHTML"
    hx-indicator="#search-indicator"
    className="w-full"
    id="search"
    placeholder="Search icons..."
/>
  <!-- search results -->
  <div id="icons" class="w-full">
      <LoaderPinwheel/>
  </div>
</Card>
