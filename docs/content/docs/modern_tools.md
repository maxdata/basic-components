---
title: Modern Tools
description: Modern Tools for server-side components
---

<Prose>

_Re-thinking (Python) server-side web development with components in the modern age._ 

Web development evolves at a blistering pace. Most improvements have occurred in Javascript/Typescript front-end SPA frameworks like React, Vue, and Svelte via **components**.  
While they have been able to use components for quite a while, server-side frameworks have been relegated to mostly servicing apis to support them.

Using components allows modular development, because they can be easily pieced together to make bigger things. 

Recently several new technologies have come about recently which, combined together, can reshape how components can be created on the server.

## htmx

Htmx is one of the most exciting new tools for web development with HTML. To read more about htmx, see the following links:

- [htmx.org](https://htmx.org/) - htmx website
- [htmx Examples](https://htmx.org/examples/) - examples for using htmx 
- [SPA Alternative](https://htmx.org/essays/spa-alternative/) - how passing back html over the wire can be simpler than json
- [Hypermedia Apis](https://htmx.org/essays/hypermedia-apis-vs-data-apis/) - front end apis on the server-side

Still, it can be challenging designing HTML markup in templates via traditional means using template libraries like Jinja or Django to return small amounts of html to update a part of the DOM without requiring a full page refresh on the client.  

## Tailwind CSS

[Tailwind CSS](https://tailwindcss.com/) has taken off and completely turned web development on its head by including utility style classes directly in html markup, instead of separate css files. This makes consistent styling very easy, but can lead to a nasty soup of attributes littered across the html templates.   

## Alpine.js 

[Alpine.js](https://alpinejs.dev/) helps to radically simplify adding basic logic for client side state with a minimum of js code. If we are adding css directly to html markup, why not js also? 

## JinjaX

JinjaX provides a simple format to compose components, with markup very similar to ones created for React or Vue, only rendered via Jinja templates on the server instead of the client.

## shadcn/ui

[shadcn/ui](https://ui.shadcn.com/) has taken React components to a whole new level, creating well designed and attractive components that you can copy/paste into your project. 

## FastAPI

[FastAPI](https://fastapi.tiangolo.com/) is one of many Python backend API frameworks. It stands out because it is very fast, lightweight and easy to use. 


## AI 

All of these can now be combined via AI Power Tools. 
New LLMs like ChatGPT-4 and Claude understand how to use all of these tools really well. 
Now, instead of having to start from scratch to combine all of these new technologies, one can use AI to perform a lot of the heavy lifting.

For example, it's trivial to port shadcn/ui React code to JinjaX after describing how JinjaX works to the LLM. It can also add behavior and styles using Alpine.js and Tailwind CSS. 
Thanks to the great work of these project creators, it's possible to combine the best parts of each and create something really cool:

- Server-side rendered web components (JinjaX)
- Easy accessibility (via shadcn/ui)
- With client side logic (Alpine.js)
- Uniform styling (Tailwind CSS)
- With hypertext superpowers (htmx)
- On a modern api framework (FastAPI)



</Prose>
