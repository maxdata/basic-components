---
title: Introduction
description: Re-usable server-side components based on shadcn/ui. <br />Built with JinjaX, Alpine.js, and Tailwind CSS, with support for htmx.
---

<Prose>

## Modern Server-Side Components

This project brings the component design patterns of [shadcn/ui](https://ui.shadcn.com) to the Python ecosystem. It's an unofficial port that leverages modern tools like
[JinjaX](https://jinjax.scaletti.dev/), [Alpine.js](https://alpinejs.dev/), and [htmx](https://htmx.org/) to create dynamic, responsive components with server-side rendering.

**Note:** This project is not affiliated with [shadcn](https://twitter.com/shadcn).

## Features

- **Modern Stack**: Combines JinjaX for components, Alpine.js for reactivity, and htmx for dynamic behavior in HTML
- **Server-First**: Built specifically for Python web frameworks (FastAPI, Django, Flask)
- **Customizable**: Every component is yours to modify and extend
- **Minimal Dependencies**: Copy only the components you need - no package to install. You'll need to set up Tailwind CSS and include Alpine.js, htmx, and JinjaX in your project.
- **Accessibility**: Maintains the accessibility features of shadcn/ui
- **Light and Dark**: Built-in theming support with light and dark modes

## Not a Traditional Component Library

This is **not a traditional component library** that you install as a dependency into a virtualenv. 
Instead, it's a collection of reusable components that you can copy directly into your project.

1. Choose the components you need
2. Use the [CLI](/docs/cli) to add them to your project (or copy/paste manually)
3. [Configure](/docs/utilities) your code to use the components 
4. Customize the code to match your needs
5. Build your interface using JinjaX's component system and Tailwind CSS's utility classes for styling and htmx for dynamic updates

**Here's a simple example**

You can include a component using simple HTML tags in a Jinja template. 
Additional behavior can be added via attributes for Alpine.js or htmx. Click the `Alpine enabled` and `htmx enabled` buttons below.   
</Prose>

<TabPreview component="Button" template="examples/docs_button.html"/>
<Prose>

Components are implemented using JinjaX and contain all the info about styles and any logic required for behavior. 
 
</Prose>
<IncludeComponents dir="button" :components="['Button.jinja']" />
<Prose>
Components are easily composable, allowing you to combine them to create complex layouts using Tailwind utility classes. 
</Prose>

<TabPreview component="Example" template="examples/card.html"/>

<Prose>

## Project Status 

_This is an active project, with new components being added regularly. We welcome your feedback and contributions! See the [changelog](/docs/changelog) for details and check out the [contribution guide](/docs/contribution) to get involved!_


## FAQ

### Why copy/paste?

Traditional component libraries often couple style with implementation, making customization difficult. By providing
components you can copy and modify:
- You have complete control over the implementation and styling.
- You can customize the components to suit your needs.
- You maintain full control by copying the code directly  

### Which frameworks are supported?

Any Python web framework that supports Jinja templates works with these components. Setup guides for
[FastAPI](https://fastapi.tiangolo.com/), [Django](https://www.djangoproject.com/), and [Flask](https://flask.palletsprojects.com) with complete examples are included.

### Can I use this in my project?

Yes! This project is MIT licensed and free to use in personal and commercial projects. No attribution required.

### Why did you create this?

The project was created to provide a way to build full-stack applications using server-side rendering, with Alpine.js and htmx for interactivity and Tailwind CSS for styling. Traditional Jinja templates with standard patterns like extending and including templates can become messy, especially with numerous Tailwind utility classes. Using JinjaX, along with Tailwind CSS and htmx, enables a clean and maintainable pattern for composing components that are easy to extend and debug. Read more [here](/docs/modern_tools).

### Component X is missing

We plan to port all components from shadcn/ui. However, you don't need to wait—feel free to contribute by adding it yourself! Most components are straightforward to port, and we've included a [guide](/docs/ai) that we've followed, using AI to handle much of the heavy lifting. Your contributions are welcome and appreciated.

</Prose>




