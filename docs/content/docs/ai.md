---
title: Using AI to create components
description: LLMs are great at writing boilerplate code for you
---
<Prose>

## The AI code intern

The components in this repo have been ported from React to JinjaX implementations primarily using AI LLMs, including ChatGPT-4 and Claude.

The following guide outlines the process for porting React components from **shadcn/ui** to **JinjaX** templates using
an LLM.

## AI Prompting

The [llms.md](https://github.com/basicmachines-co/basic-components/blob/main/llms.md) file contains an overview of the project and detailed information that can be provided to an LLM 
to aid with creating components and porting components from React.   

</Prose>

<IncludeFile dir="." file_name="llms.md"/>

<Prose>

## Porting Process

0. **Add** the [llms.md](https://github.com/basicmachines-co/basic-components/blob/main/llms.md) file as context to your chat.
1. **Select** a component from [shadcn/ui](https://ui.shadcn.com/) to port.
2. **Gather** information about the component (name, description, React code, usage examples).
3. **Use AI** to assist with the initial port (see below).
4. **Implement** the AI-provided JinjaX version in your project.
5. **Test and iterate** on the implementation.
6. **Refine** the component based on testing results.
7. **Document** the component's usage and any differences from the React version.
8. **Review** to ensure [adherence to project guidelines](/docs/components) and consistency with other components.
9. **Contribute** your change back to the project if you like.


## AI Prompt Template

When porting a component you can use this prompt template:

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

1. Uses the same Tailwind styles
2. Implements interactivity using Alpine.js
3. Follows the project guidelines for component creation (as detailed in the llms.md doc)
4. Maintains the same functionality and accessibility features as the original
5. Follows the same naming patterns for components and sub-components
6. Match the behavior and composition of react versions as possible unless there is a reason not to. Then please bring that up and we will discuss how to handle it.

```
</Prose>
