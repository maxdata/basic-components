
## Vendoring Components

The components in this project can be copied (vendored) directly into your project and customized further using [Copier](https://copier.readthedocs.io/en/stable/).
You can then customize them as needed.

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

### Versioning and Updates

When you vendor these components into your project, a `components/components-version.txt` file will be created.
This file contains the version number of the basic-components library that you've vendored.

**Notes:**
- If updating, copier will preserve your existing files. It will show diffs for any conflicts and allow you to choose how to handle them.
- You can specify a specific branch, tag, or commit by appending it to the repository URL, e.g., `...basic-components.git@v1.0.0 ./path/to/destination`
- You can also fork this repo and use your own git url with copier or use a local copy of the repository.
- Using a local repository is particularly useful during development or when you've made custom modifications.

For more detailed information on Copier usage, refer to the [Copier documentation](https://copier.readthedocs.io/).





# Testing Strategy for JinjaX Component Library

## Overview

Our testing strategy focuses on ensuring the reliability, functionality, and consistency of our JinjaX components. We use Playwright for end-to-end testing, leveraging server-side endpoints to test components in a real-world-like environment.

## Key Aspects of Our Testing Approach

1. **Server-side Endpoints for Components:**
    - Create endpoints that serve individual components with various props and states.
    - This allows testing components in their intended server-side rendered context.

2. **Real-world Examples:**
    - Use practical, real-world scenarios in tests to uncover potential issues.

3. **Playwright for E2E Testing:**
    - Utilize Playwright's cross-browser support and powerful API for comprehensive testing.
    - Simulate user interactions to test component behavior thoroughly.

## Testing Enhancements

1. **Component Isolation Tests:**
    - Implement isolated tests for quick identification of component-specific issues.

2. **Visual Regression Testing:**
    - Use Playwright's visual comparison features to ensure UI consistency across changes.

3. **Accessibility Testing:**
    - Incorporate WCAG compliance checks into component tests.

4. **Performance Metrics:**
    - Gather and analyze performance metrics for components using Playwright.

5. **Interactivity Coverage:**
    - Ensure thorough testing of all interactive aspects, especially Alpine.js functionality.

6. **Parameterized Tests:**
    - Create tests with various prop combinations to cover different component states.

7. **Error State Testing:**
    - Include tests for error states and edge cases in components.

8. **Documentation Generation:**
    - Use test cases to automatically generate or update component documentation.

9. **CI/CD Integration:**
    - Integrate tests into the CI/CD pipeline for automated testing on each commit or PR.

10. **Test Helpers:**
    - Develop utilities specific to component testing to streamline test writing and maintenance.

## Implementation Approach

1. Create a dedicated `tests` directory for component tests.
2. Set up a simple server (e.g., using FastAPI) to serve individual components.
3. Write Playwright tests that interact with these component endpoints.
4. Include both "happy path" and edge case scenarios in tests.
5. Utilize Playwright's assertions and add custom assertions as needed.

## Example Test Structure

```python
from playwright.sync_api import Page, expect

def test_button_component(page: Page):
    # Navigate to the button component test page
    page.goto("/test/components/button")

    # Test default state
    button = page.locator("button")
    expect(button).to_be_visible()
    expect(button).to_have_text("Click me")

    # Test click behavior
    button.click()
    expect(page.locator(".clicked-state")).to_be_visible()

    # Test disabled state
    page.goto("/test/components/button?state=disabled")
    expect(button).to_be_disabled()

# Additional tests for other components and their variations
```

## Next Steps

1. Set up the testing environment with Playwright and necessary dependencies.
2. Create initial test endpoints for core components.
3. Develop a set of base tests that can be applied to most components.
4. Gradually expand test coverage to include all components and their variations.
5. Integrate testing into the development workflow and CI/CD pipeline.

By following this testing strategy, we aim to ensure the reliability and quality of our JinjaX component library, facilitating its integration into the basic-foundation project and its adoption by other developers.
