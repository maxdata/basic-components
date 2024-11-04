---
title: Introduction
description: Re-usable server-side components based on shadcn/ui, built with JinjaX, Alpine.js, and Tailwind CSS, with support for htmx.
---

<Prose>

## Modern Server-Side Components

This project brings the elegant design patterns of [shadcn/ui](https://ui.shadcn.com) to the Python ecosystem, enabling
developers to build beautiful, accessible server-side interfaces. It's an unofficial port that leverages modern tools like
[JinjaX](https://jinjax.scaletti.dev/), [Alpine.js](https://alpinejs.dev/), and [htmx](https://htmx.org/) to create dynamic, responsive components
while maintaining the benefits of server-side rendering.

**Note:** This project is not affiliated with [shadcn](https://twitter.com/shadcn).

## Key Features

- **Server-First**: Built specifically for Python web frameworks (FastAPI, Django, Flask)
- **Modern Stack**: Combines JinjaX for components, Alpine.js for reactivity, and htmx for dynamic updates
- **Zero Dependencies**: Copy only the components you need - no package to install
- **Customizable**: Every component is yours to modify and extend
- **Light and Dark**: Built-in theming support with light and dark modes
- **Accessibility**: Maintains the accessibility features of shadcn/ui

## Not a Traditional Component Library

This is **not a traditional component library** that you install as a dependency. Instead, it's a collection of reusable components that you can copy directly into your project.

1. Choose the components you need
2. Use the [CLI](docs/cli) to add them to your project (or copy/paste manually)
3. Customize the code to match your needs
4. Build your interface using JinjaX's component system and TailwindCSS's utility classes for styling and htmx for dynamic updates

**Here's a simple example**

You can include a component using simple html tags in a Jinja template. 
Additional behavior can be added via attributes for Alpine or htmx. Click the `Alpine enabled` and `htmx enabled` buttons below.   
</Prose>

<TabPreview component="Button" template="examples/button_docs.html"/>
<Prose>

Components are implemented using JinjaX and contains all the info about styles and any logic required for behavior. 
 
</Prose>
<IncludeComponents :components="['Button.jinja']" />
<Prose>
Components are easily composable to create complex layouts using Tailwind utility classes. 
</Prose>

<TabPreview component="Example" template="examples/card.html"/>

<Prose>

## Project Status 

_This is an active project, with new components being added regularly. The list of components ported from shadcn/ui is not complete. See the [changelog](/docs/changelog) for details. [Contributions](/docs/contribution) are welcome!_


## FAQ

### Why copy/paste and not package as a dependency?

Traditional component libraries often couple style with implementation, making customization difficult. By providing
components you can copy and modify:
- You have complete control over the implementation
- You can customize the components to suit your needs
- You maintain full control, by copying the code directly  
- You have ownership and control over the code

### Which frameworks are supported?

Any Python web framework that supports Jinja templates works with these components. We provide specific setup guides for
FastAPI, Django, and Flask.

### Can I use this in my project?

Yes! This project is MIT licensed and free to use in personal and commercial projects. No attribution required.

### Why did you create this?

The project was created to provide a way to build full-stack applications using server-side rendering, with Alpine.js and htmx for interactivity and Tailwind CSS for styling. Traditional Jinja templates with standard patterns like extending and including templates can become messy, especially with numerous Tailwind utility classes. Using JinjaX, along with Tailwind CSS and htmx, enables a clean pattern of composing logic that is easy to extend and debug.

### I want component X, but it's not here. Can you add it?

We plan to port all components from shadcn/ui. However, you don't need to wait—feel free to contribute by adding it yourself! Most components are straightforward to port, and we've included a [guide](/docs/porting-guide) that we've followed, using AI to handle much of the heavy lifting. Your contributions are welcome and appreciated.

</Prose>




