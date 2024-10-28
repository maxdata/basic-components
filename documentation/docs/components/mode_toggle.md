# ModeToggle

A dropdown menu with options to switch between light and dark modes.

## Preview

<iframe
src="{{ preview_url}}/components/mode_toggle"
style="width: 100%; height: 400px; border: none;">
</iframe>

## Components

=== "ModeToggle.jinja"
{% raw %}
```jinja
{% include '../../../components/ui/ModeToggle.jinja' %}
```
{% endraw %}

## Usage

The mode is toggled by setting a 'mode' value in localStorage. Add the following logic to the `html` element on the page
to perform toggling logic. Any component can call the `toggleMode` function to switch the mode. 
```html
<html
    class="h-full"
    lang="en"
    x-data="{
        mode: localStorage.getItem('mode') || 'system',
        init() {
            this.applyMode();
        },
        applyMode() {
            if (this.mode === 'dark') {
                document.documentElement.classList.add('dark');
            } else if (this.mode === 'light') {
                document.documentElement.classList.remove('dark');
            } else {
                // System preference
                const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                if (prefersDark) {
                    document.documentElement.classList.add('dark');
                } else {
                    document.documentElement.classList.remove('dark');
                }
            }
        },
        toggleMode(mode) {
            this.mode = mode;
            localStorage.setItem('mode', mode);
            this.applyMode();
        }
    }"
    x-init="init()"
>
```

## Examples

### Button

=== "Preview"
    <iframe
    src="{{ preview_url}}/components/mode_toggle?option=button"
    style="width: 100%; height: 100px; border: none;">
    </iframe>

=== "Code"
    ```html
    {% include-markdown "../../backend/templates/mode_toggle_button.html" %}
    ```
