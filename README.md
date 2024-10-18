# JinjaX Component Library

This project is a library of UI components which use [JinjaX](https://jinjax.scaletti.dev/guide/), an extension of
Jinja templates. It directly ports components from [shadcn/ui](https://ui.shadcn.com/) to JinjaX,
maintaining compatibility in usage and style, using [Alpine.js](https://alpinejs.dev/) for interactivity and [Tailwwind.css](https://tailwindcss.com/) for styling. 

The goal is to provide developers using server-side rendering frameworks (with FastAPI or Flask) access to
high-quality, accessible components similar or identical to those available in shadcn/ui. They can be easily extended
via [htmx](https://htmx.org/) to create dynamic html interfaces easily.

- **Framework**: JinjaX (Jinja2 extension)
- **Styling**: Tailwind CSS
- **Interactivity**: Alpine.js
- **Compatibility**: Direct port of shadcn/ui components
- **Purpose**: Enable use of shadcn/ui-style components in server-side rendered applications

## Example Component 

```jinja
{# def
    id: str = "",
    className: str = "",
    disabled: bool = False
#}

<div id="{{ id }}" class="{{ className }}" {{ attrs.render() }}>
    {{ content }}
</div>
```

## Usage: Using the `Button` Component

Within a template or another component, declare the component, passing attributes as needed.

```jinja
<Button variant="secondary">Secondary</Button>

<Button>
  <Mail className="mr-2 h-4 w-4" invert="True" />
  Login with Email
</Button>

<Button id="submitBtn" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onclick="alert('Button Clicked!')">
    Click Me
</Button>
```

- The `Button` component is inserted directly into the template without macros or includes.
- Props like `id`, `className`, and `onclick` are set directly, and any additional attributes can be passed as needed.

- **Props**: Props are declared using `{# def ... #}` and define attributes such as `id`, `className`, and any booleans
  like `disabled`.
- **Dynamic Attributes**: The `{{ attrs.render() }}` in the component allows passing additional
  attributes dynamically when the component is used.

## Adding htmx

Htmx attributes can be added to components when they are declared to add behavior. 

```jinja
<Button
  hx-get="/some/url"
  hx-target="this"
  hx-swap="outerHTML"
  type="button"
  variant="outline"
>Click me
</Button>
```

# Porting Components with AI

The components in this repo have been ported primarily using AI from React to JinjaX implementations.

The following guide outlines the process for porting React components from **shadcn/ui** to **JinjaX** templates using
an LLM.

## Porting Process

1. **Select** a component from shadcn/ui to port.
2. **Gather** information about the component (name, description, React code, usage examples).
3. **Use AI** to assist with the initial port (see Part 2 for AI prompting guidelines).
4. **Implement** the AI-provided JinjaX version in your project.
5. **Test and iterate** on the implementation.
6. **Refine** the component based on testing results.
7. **Document** the component's usage and any differences from the React version.
8. **Review** to ensure adherence to project guidelines and consistency with other components.

## AI Assistance Guidelines

The following section is a reference for prompting AI models when porting components. It includes rules,
guidelines, and example prompts to ensure consistent and effective component creation.

## Rules for Creating Components

1. **Props Definition**:
    - Use `{# def ... #}` to declare props.
    - Include `id`, `className`, and other relevant attributes.

2. **Dynamic Attributes**:
    - Always include `{{ attrs.render() }}` for additional attributes.

3. **Content Slots**:
    - Use `{{ content }}` as the default slot for main content.
    - Create separate components for additional slots instead of using multiple slots in a single component.

4. **Class Handling**:
    - Use `className` for component props.
    - Convert `className` to `class` for native HTML elements in the output.

5. **Event Handlers and Interactivity**:
    - Use Alpine.js for dynamic behaviors (e.g., `@click`, `x-show`).
    - Set attributes like `onclick` directly as props.

6. **ID Handling**:
    - Generally, an id may be passed as an extra arg when the component is declared.
    - The component should behave correctly if `id` is not provided, preventing any invalid HTML output.
    - Always include `{{ attrs.render() }}` for attributes that might be passed dynamically when the component is
      declared (including `id`).

7. **Conditional Classes and States**:
    - Use Alpine.js for managing conditional classes and states.
    - Limit the scope of Alpine `x-data` to the component.

8. **Component Structure**:
    - Components should be standalone units without relying on includes or macros.

9. **Logic**
    - Components can use Jinja logic, conditionals and macros internally when needed.
    - Components should not have any external jinja template dependencies (extends, includes).

   
## Effective AI Prompting

When providing a new component for porting, copy/paste this README into a chat to give context. Then, use the following
template to port a component:

```
I'm porting the [Component Name] from shadcn/ui to JinjaX. Here's the relevant information:

1. Component Name: [Name]
   Documentation: [Link to shadcn/ui docs]

2. Description:
   [Brief description of component functionality]

3. React Source Code:
   
   [Paste React component code here]
   
4. Example Usage:
   
   [Copy/paste shadnc component usage example]
   
Please create a JinjaX version of this component that:

1. Uses Tailwind CSS for styling
2. Implements interactivity using Alpine.js
3. Follows the project guidelines for component creation (as detailed in the Rules section)
4. Maintains the same functionality and accessibility features as the original

Explain any complex logic or Alpine.js implementations in your response.

```

## Vendoring Components

The components in this project can be copied (vendored) directly into your project and customized further. 
Using a tool like [Copier](https://copier.readthedocs.io/en/stable/), you can copy the components into your project
and then update them later if needed. 

To vendor these components into your project using copier:

1. Ensure you have Copier installed:
   ```
   pip install copier
   ```

2. Run the following command from your project directory, specifying the destination:
   ```
   copier copy https://github.com/basic-foundation/basic-components.git ./path/to/destination
   ```
   Replace `./path/to/destination` with the directory where you want the components to be vendored.

3. To preview the operation without making any changes, use the `--pretend` flag:
   ```
   copier copy --pretend https://github.com/basic-foundation/basic-components.git ./path/to/destination
   ```

**Notes:**
- If updating, copier will preserve your existing files. It will show diffs for any conflicts and allow you to choose how to handle them.
- You can specify a specific branch, tag, or commit by appending it to the repository URL, e.g., `...basic-components.git@v1.0.0 ./path/to/destination`
- You can also fork this repo and use your own git url with copier or use a local copy of the repository. 
- Using a local repository is particularly useful during development or when you've made custom modifications.

For more detailed information on Copier usage, refer to the [Copier documentation](https://copier.readthedocs.io/).

## Versioning and Updates

When you vendor these components into your project, a `components/components-version.txt` file will be created. 
This file contains the version number of the basic-components library that you've vendored.

### Updating Vendored Components

To update your vendored components to the latest version:

1. From your project root, run:
   ```
   copier update
   ```

2. Copier will detect the previous version used and prompt you about updates. It will show you the changes between your current version and the latest version.

3. Follow the prompts to complete the update process.

4. After updating, check the `components/version.txt` file to confirm the new version.

**Important Notes:**
- Before updating, make sure to commit any changes in your project to avoid losing work.
- If you've made modifications to the vendored components, Copier will ask how to handle conflicts. You may need to manually merge some changes.

When reporting issues or seeking support related to these components, always mention the version number found in your `components/components-version.txt` file.
