---
title: Introduction
description: Server-side UI components inspired by shadcn/ui, built with JinjaX, Alpine.js, and Tailwind CSS, with seamless HTMX integration.
---

<Prose>

This project is an unofficial [JinjaX](https://jinjax.scaletti.dev/) port of [shadcn/ui](https://ui.shadcn.com), not
affiliated with [shadcn](https://twitter.com/shadcn).
Its goal is to equip developers using Python frameworks with server-side rendering, such as FastAPI, Django, or Flask, with
high-quality,
responsive components that behave similarly to their React counterparts. Components can be easily extended
with [HTMX](https://htmx.org/) to create dynamic interfaces.

This is **NOT** a component library.

It's a collection of re-usable components that you can copy and paste or add to your apps.

**What do you mean not a component library?**

It means you do not install it as a dependency.
You do not install the components into your environment, instead you copy them into your project. 

Pick the components you need.
Use the [CLI](/docs/cli) to automatically add component, or copy and paste the code into your project and customize to your
needs. The code is yours.

_This project is a work in progress. The list of components ported from shadcn/ui is not complete. 
See the [changelog](/docs/changelog) for details. [Contributions](/docs/contribution) are welcome._

## FAQ

### Why copy/paste and not packaged as a dependency?
The idea behind this is to give you ownership and control over the code, allowing you to decide how the components are built and styled.
Start with some sensible defaults, then customize the components to your needs.
One of the drawbacks of packaging the components in a package is that the style is coupled with the implementation.
The design of your components should be separate from their implementation.

### Which frameworks are supported?

You can use any framework that supports Jinja templates, including Fastapi, Flask, or Django.

### Can I use this in my project?

Yes! Feel free to use for personal and commercial projects. No attribution required. The is project is FOSS and MIT licensed.

### Why did you create this?

I wanted to have a way to build full stack applications using server-side rendering and Alpine.js and HTMX for interactivity and Tailwind CSS for styling.
I tried using Jinja templates with 'regular' patterns like extending and including templates but it was a mess, especially with all the tailwind utility styles everywhere.
Using JinjaX, along with Tailwind and HTMX, enables a very nice pattern of composing logic that is also very easy to extend and debug.

### I want component X, but it's not here. Can you add it?

I plan to port all components from shadcn/ui.
But you don't need to wait, feel free to do it yourself and make a [contribution](/docs/contribution).
Most components are straightforward to port, and I've included a guide that I've followed, using AI to do a lot of the heavy lifting.

</Prose>




