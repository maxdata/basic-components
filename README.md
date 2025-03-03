# basic-components

Re-usable server-side components based on shadcn/ui.
Built with JinjaX, Alpine.js, and Tailwind CSS, with support for htmx.

## Installation & Usage

![demo](/docs/static/img/components-add-demo.gif)

### Quick Start with `uv`

JinjaX is required.

```bash
# install jinjax
uv add jinjax
````

You can use the CLI directly without installing the package.

```bash
# Add components
uv --from basic-components components add button
```

You will also need to configure your project to load components into the `jinjax.Catalog` and add a global `cn` function
to the Jinja environment. See [utilities](https://components.basicmachines.co/docs/utilities).

Helpers for these are packed in the `basic-components[utils]` package. 

### Package Installation Options

Install only the utility functions for JinjaX and tailwind.

```bash
# With utility functions
uv add --dev "basic-components[utils]"
```

Setup instructions and examples:
- [FastAPI](https://components.basicmachines.co/docs/fastapi)
- [Flask](https://components.basicmachines.co/docs/flask)
- [Django](https://components.basicmachines.co/docs/django)

## Example

Use components directly in your templates, similar to React. Use Tailwind CSS classes for styles, htmx friendly also!

```html
  <!-- Card component example -->
  <Card className="w-[350px] mb-4">
    <CardHeader className="pb-3">
      <CardTitle>Components!</CardTitle>
      <CardDescription className="max-w-lg text-balance leading-relaxed">
        Using components is fun.
      </CardDescription>
    </CardHeader>
    <CardContent>
      The button below is enabled with htmx. Click to update it.
    </CardContent>
    <CardFooter>
      <!-- use htmx -->
      <Button
        variant="outline"
        hx-get="/button"
        hx-trigger="click"
        hx-target="this"
        hx-swap="outerHTML">htmx is enabled</Button>
    </CardFooter>
  </Card>
</div>
```

Components are rendered on the server via JinjaX (a Jinja component library) and returned as html for the browser.

![demo](/docs/static/img/htmx-demo.gif)

## Installation Groups

- `utils`: Utility functions for JinjaX setup and `cn()` tailwind class helper
- `docs`: Requirements for the docs site
- `dev`: Development tools for contributing
- `full`: All features included

## Documentation

Visit [https://components.basicmachines.co](https://components.basicmachines.co) to view the documentation.

## Contributing

Please read the [contributing guide](https://components.basicmachines.co/docs/contribution).

## License

Licensed under the [MIT license](https://github.com/shadcn/ui/blob/main/LICENSE.md).

## Components

19/48

- [x] accordion
- [x] alert
- [x] alert-dialog 
- [ ] aspect-ratio
- [ ] avatar
- [x] badge
- [ ] breadcrumb
- [x] button
- [ ] calendar
- [x] card
- [ ] carousel
- [ ] chart
- [x] checkbox
- [ ] collapsible
- [ ] command
- [ ] context-menu
- [x] dialog 
- [ ] drawer
- [x] dropdown-menu
- [x] form
- [ ] hover-card
- [ ] input-otp
- [x] input
- [x] label
- [x] link
- [ ] menubar
- [ ] navigation-menu
- [ ] pagination
- [x] popover
- [ ] progress
- [x] radio-group
- [ ] resizable
- [ ] scroll-area
- [x] select
- [ ] separator
- [x] sheet
- [ ] sidebar
- [ ] skeleton
- [ ] slider
- [ ] sonner
- [ ] switch
- [x] table
- [x] tabs
- [x] textarea
- [x] toast
- [ ] toaster
- [ ] toggle-group
- [ ] toggle
- [ ] tooltip

Extended
- [ ] Prose 