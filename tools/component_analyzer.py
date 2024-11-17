# component_analyzer.py

from pathlib import Path
import json
from typing import Dict, List, Set, Tuple
import re
from collections import defaultdict

import tomli_w
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    help="Analyze component dependencies and optionally output to TOML and JSON",
    add_completion=False,
)
console = Console()


def find_component_references(content: str) -> Set[str]:
    """Find all PascalCase component references in template content."""
    pattern = r'<([A-Z][a-zA-Z0-9]*)[^>]*/?>'
    return set(re.findall(pattern, content))


def get_components(components_dir: Path) -> Tuple[Set[str], Dict[str, str]]:
    """Get all component names and create a mapping for integration components."""
    core_components = set()
    integration_mapping = {}

    for d in components_dir.iterdir():
        if d.is_dir():
            if d.name == 'integrations':
                for integration_dir in d.iterdir():
                    if integration_dir.is_dir():
                        integration_name = f"integrations/{integration_dir.name}"
                        integration_mapping[integration_dir.name] = integration_name
            else:
                core_components.add(d.name)

    return core_components, integration_mapping


def normalize_component_name(
    name: str,
    core_components: Set[str],
    integration_mapping: Dict[str, str]
) -> Tuple[str, bool]:
    """Convert component name to its normalized form. Returns (name, is_valid)."""
    # Handle icon components - keep PascalCase
    if name.endswith('Icon'):
        # Just strip "Icon" suffix but maintain PascalCase
        base_name = name[:-4]
        icon_ref = f"icons/{base_name}"
        is_valid = True  # We assume all Icon references are valid since they're direct class names
        return icon_ref, is_valid

    # Handle special cases for moon/sun icons - now in PascalCase
    if name.lower() in {'moon', 'sun'}:
        return f"icons/{name.title()}", True

    name_lower = name.lower()

    # Check integration components
    for integration_key, integration_name in integration_mapping.items():
        if name_lower.startswith(integration_key.lower()):
            return integration_name, True

    # Special case mappings based on your dependencies
    if name_lower in {'checkbox', 'radio', 'form', 'button'}:
        return name_lower, True

    # Find component in core components
    for component in core_components:
        if name_lower.startswith(component.replace('_', '')):
            return component, component in core_components

    return name_lower, False


def analyze_components(
    components_dir: Path,
) -> Tuple[Dict[str, List[str]], List[str]]:
    """Analyze components and return (dependencies, warnings)."""
    core_components, integration_mapping = get_components(components_dir)
    raw_dependencies = defaultdict(set)
    warnings = []

    for template_file in components_dir.rglob("*.jinja"):
        rel_path = template_file.relative_to(components_dir)
        parts = rel_path.parts

        if parts[0] == 'integrations':
            if len(parts) > 1:
                component_name = f"integrations/{parts[1]}"
            else:
                continue
        else:
            component_name = parts[0]

        if component_name in {'ui', 'integrations'}:
            continue

        content = template_file.read_text()
        refs = find_component_references(content)

        for ref in refs:
            normalized_ref, is_valid = normalize_component_name(
                ref, core_components, integration_mapping
            )
            if not is_valid and not normalized_ref.startswith('icons/'):
                warnings.append(
                    f"Unresolved component reference: '{ref}' in {template_file}"
                )
            if normalized_ref != component_name:
                raw_dependencies[component_name].add(normalized_ref)

    dependencies = {
        k: sorted(list(v))
        for k, v in raw_dependencies.items()
        if v
    }

    return dict(sorted(dependencies.items())), warnings


def display_results(
    dependencies: Dict[str, List[str]],
    warnings: List[str],
    known_dependencies: Dict[str, List[str]],
) -> None:
    """Display analysis results in a formatted table."""
    if warnings:
        console.print("\n[yellow]Warnings:[/yellow]")
        for warning in warnings:
            console.print(f"[yellow]⚠ {warning}[/yellow]")

    table = Table(title="Component Dependencies")
    table.add_column("Component", style="cyan")
    table.add_column("Dependencies", style="green")
    table.add_column("Status", style="yellow")

    for component, deps in dependencies.items():
        known_deps = set(known_dependencies.get(component, []))
        found_deps = set(deps)

        if component not in known_dependencies:
            status = "⚠ New component"
        elif known_deps != found_deps:
            status = "⚠ Dependencies changed"
        else:
            status = "✓ No changes"

        table.add_row(component, "\n".join(deps), status)

    console.print("\n", table)


@app.command()
def analyze(
    components_dir: Path = typer.Option(
        Path("components/ui"),
        "--components-dir",
        "-d",
        help="Directory containing the components",
    ),
    output_toml: bool = typer.Option(
        True,
        "--toml/--no-toml",
        "-t/-nt",
        help="Output dependencies to TOML file",
    ),
    output_json: bool = typer.Option(
        False,
        "--json/--no-json",
        "-j/-nj",
        help="Output dependencies to JSON file",
    ),
) -> None:
    """Analyze component dependencies and generate dependency map."""
    if not components_dir.exists():
        console.print(f"[red]Error: Components directory not found at {components_dir}[/red]")
        raise typer.Exit(1)

    try:
        # Load existing dependencies from component_dependencies.toml if it exists
        known_dependencies = {}
        toml_path = Path("basic_components/component_dependencies.toml")
        if toml_path.exists():
            import tomli
            with toml_path.open('rb') as f:
                toml_data = tomli.load(f)
                known_dependencies = toml_data.get('dependencies', {})

        # Analyze components
        dependencies, warnings = analyze_components(components_dir)

        # Display results
        display_results(dependencies, warnings, known_dependencies)

        # Write TOML output if requested
        if output_toml:
            output_file = Path("basic_components/component_dependencies.toml")
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with output_file.open('wb') as f:
                tomli_w.dump({'dependencies': dependencies}, f)
            console.print(f"\nDependencies written to {output_file}")

        # Write JSON output if requested
        if output_json:
            output_file = Path("component_dependencies.json")
            with output_file.open('w') as f:
                json.dump({'dependencies': dependencies}, f, indent=2)
            console.print(f"\nDependencies written to {output_file}")

        # Exit with warning status if there were warnings
        if warnings:
            raise typer.Exit(1)

    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()