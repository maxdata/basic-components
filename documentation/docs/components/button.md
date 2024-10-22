# Button Component

The Button component renders a clickable button using Tailwind CSS.


## Button 

<div class="preview-container mb-8">
  <div 
    hx-get="/backend/components/button" 
    hx-target="#button-preview" 
    hx-swap="outerHTML"
  >
    <button class="inline-flex items-center px-4 py-2 text-white bg-blue-500 rounded-md hover:bg-blue-700">
      Loading Preview...
    </button>
  </div>

  <div id="button-preview" class="mt-4"></div>
</div>


## Usage

```html
<Button variant="primary">Click Me</Button>
```
