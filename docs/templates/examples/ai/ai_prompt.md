## Rules for Creating Components

1. **Props Definition**:
    - Use `{{ '{#def ... #}' }}` to declare props.
    - Include `id`, `className`, and other relevant attributes.
2. **Dynamic Attributes**:
    - Always include `{{ '{{ attrs.render() }}' }}` for additional attributes.

3. **Content Slots**:
    - Use `{{ '{{ content }}' }}` as the default slot for main content.
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
    - Always include `{{ '{{ attrs.render() }}' }}` for attributes that might be passed dynamically when the component is
      declared (including `id`).

7. **Conditional Classes and States**:
    - Use Alpine.js for managing conditional classes and states.
    - Limit the scope of Alpine `x-data` to the component.

8. **Component Structure**:
    - Components should be standalone units without relying on includes or macros.

9. **Logic**
    - Components can use Jinja logic, conditionals and macros internally when needed.
    - Components should not have any external jinja template dependencies (extends, includes).

