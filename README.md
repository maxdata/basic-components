# JinjaX Component Library

## Part 1: For Developers

### Project Purpose

This project creates a library of UI components using [JinjaX](https://jinjax.scaletti.dev/guide/), an extension of
Jinja templates to create components. It directly ports components from [shadcn/ui](https://ui.shadcn.com/) to JinjaX,
maintaining compatibility in usage and style, using Alpine.js for interactivity

The goal is to provide developers using server-side rendering frameworks (like FastAPI or Flask) with access to
high-quality, accessible components similar or identical to those available in shadcn/ui.

### Overview

- **Framework**: JinjaX (Jinja2 extension)
- **Styling**: Tailwind CSS
- **Interactivity**: Alpine.js
- **Compatibility**: Direct port of shadcn/ui components
- **Purpose**: Enable use of shadcn/ui-style components in server-side rendered applications

### Porting Process

1. **Select** a component from shadcn/ui to port.
2. **Gather** information about the component (name, description, React code, usage examples).
3. **Use AI** to assist with the initial port (see Part 2 for AI prompting guidelines).
4. **Implement** the AI-provided JinjaX version in your project.
5. **Test and iterate** on the implementation.
6. **Refine** the component based on testing results.
7. **Document** the component's usage and any differences from the React version.
8. **Review** to ensure adherence to project guidelines and consistency with other components.

### Using This Library

[Include instructions on how to install and use the library in a project]

### Contributing

[Guidelines for contributing to the project, including how to submit new component ports or improvements]

## Part 2: AI Assistance Guidelines

The following section is designed to be used as a reference for AI models when porting components. It includes rules,
guidelines, and example prompts to ensure consistent and effective component creation.

### Rules for Creating Components

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

### Example Component Structure

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

## Usage Example: Using the `Button` Component

Within a template or another component, declare the component as SGML, passing attributes as needed.

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

## Porting Components with AI

The components in this repo have been ported primarily using AI from React to JinjaX implementations.

The following guide outlines the process for porting React components from **shadcn/ui** to **JinjaX** templates using
AI. Follow these steps to ensure consistency and compatibility between the React and JinjaX versions.

### Effective AI Prompting

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

## Step 3: Implement Locally and Iterate

Once the component is created:

1. Implement the JinjaX component in your project template.
2. Test the component in context, verifying that it matches the behavior, styles, and layout from the React version.
3. If issues arise, iterate on the component definition until it aligns with the expected usage and styling.

## Step 4: Validate Against Established Rules

Check the component against our established rules:

1. Ensure that `class` is used for HTML elements, and `className` remains for component props.
2. Make sure dynamic attributes (`{{ attrs.render() }}`) are correctly included for all components.
3. Confirm that Alpine.js is used for any dynamic behaviors, such as visibility toggles or event handling.
4. Validate that `id` is optional but behaves correctly when omitted.
5. Avoid empty slots and prefer creating new components for additional parts rather than using multiple slots.

## Step 5: Final Testing and Documentation

1. Test the component within the project in various scenarios to ensure it behaves consistently across different usages.
2. Document the component usage, attributes, and any custom behavior directly in the template's documentation or README
   file.

---

# TODO

- [x] table
- [x] Dialog
- [x] alert dialog
- [x] popover
- [x] toast
- [x] darkmode
- [x] Form
- [-] skeleton
- [-] pagination
- [x] badge
- [x] alert

https://ui.shadcn.com/blocks

- [ ] responsive header - dashboard-04/01
- [ ] stats - dashboard-01
- [ ] login form - authentication-02

https://ui.shadcn.com/examples/tasks

- [ ] table layout

- [ ] claude
- [ ] new note app - hn
- [ ] uv
- [ ] copier - https://copier.readthedocs.io/en/stable/
