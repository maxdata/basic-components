---
title: Using AI to create components
description: LLMs are great at writing boilerplate code for you
---
<Prose>

## The AI code intern

The components in this repo have been ported from React to JinjaX implementations primarily using AI LLMs, including ChatGPT-4 and Claude.

The following guide outlines the process for porting React components from **shadcn/ui** to **JinjaX** templates using
an LLM.

## Porting Process

1. **Select** a component from [shadcn/ui](https://ui.shadcn.com/) to port.
2. **Gather** information about the component (name, description, React code, usage examples).
3. **Use AI** to assist with the initial port (see Part 2 for AI prompting guidelines).
4. **Implement** the AI-provided JinjaX version in your project.
5. **Test and iterate** on the implementation.
6. **Refine** the component based on testing results.
7. **Document** the component's usage and any differences from the React version.
8. **Review** to ensure [adherence to project guidelines](/docs/components) and consistency with other components.
9. **Contribute** your change back to the project if you like. 

## AI Prompting

The following section can be used as a reference for prompting AI models when porting components to explain their structure and give context.. 

</Prose>

<IncludeTemplate template="examples/ai/ai_prompt.md"/>

<Prose>
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
</Prose>
