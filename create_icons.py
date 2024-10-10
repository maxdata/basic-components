import os
import re

# Template for the JinjaX component
component_template = """{{# def
    id: str = "",
    className: str = "h-4 w-4",
    color: str = ""
#}}

<svg
    id="{{{{ id }}}}"
    class="{{{{ className }}}} {{{{ color }}}}"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    aria-hidden="true"
    {{{{ attrs.render() }}}}
>
{svg_content}
</svg>
"""

def extract_svg_content(svg_text):
    """
    Extracts the content inside the SVG tags.
    """
    # Match the opening <svg> tag and its attributes
    svg_open_tag_pattern = re.compile(r'<svg[^>]*>', re.IGNORECASE)
    # Find and remove the opening <svg> tag
    svg_text = svg_open_tag_pattern.sub('', svg_text)
    # Remove the closing </svg> tag
    svg_text = svg_text.replace('</svg>', '').strip()
    return svg_text

def create_jinjax_components(svg_dir, output_dir):
    # Iterate over each SVG file in the directory
    for filename in os.listdir(svg_dir):
        if filename.endswith('.svg'):
            # Read the SVG content
            with open(os.path.join(svg_dir, filename), 'r') as file:
                svg_content = file.read()

            # Extract the name of the component by converting the filename (e.g., 'a-arrow-down.svg' -> 'AArrowDown')
            name_parts = filename.replace('.svg', '').split('-')
            component_name = ''.join(part.capitalize() for part in name_parts)

            # Extract the inner SVG content (e.g., paths, groups, etc.)
            svg_inner_content = extract_svg_content(svg_content)

            # Replace placeholder in the template with the actual SVG content
            component_content = component_template.format(svg_content=svg_inner_content)

            # Define the output file path for the component
            output_path = os.path.join(output_dir, f"{component_name}.jinja")

            # Write the component content to the output file
            with open(output_path, 'w') as output_file:
                output_file.write(component_content)

            print(f"Component {component_name}.jinja created.")

if __name__ == "__main__":
    svg_dir = './node_modules/lucide-static/icons'  # Update this to your SVG files directory
    output_dir = './components/icons'  # Update this to your desired output directory

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    create_jinjax_components(svg_dir, output_dir)
