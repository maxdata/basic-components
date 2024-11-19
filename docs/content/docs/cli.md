---
title: CLI
description: Adding components to your project
---

<Prose>

Be sure you have read the [installation](/docs/installation) docs and set up your project first. 

## Vendoring Components

The components in this project can be copied (vendored) directly into your project using the `components` tool 
in the `basic-components` package via `uv`. You can then customize them as needed. This is the recommendedd way to 
install components because it will also include any dependencies (other referenced components) required.

To vendor a component into your project using the `components` tool, run

<Tabs defaultValue="uv">
    <TabsList className="grid grid-cols-2">
        <TabsTrigger value="uv">uv</TabsTrigger>
        <TabsTrigger value="pipx">pipx</TabsTrigger>
    </TabsList>
    <TabsContent value="uv">
        <div class="relative" x-data><CopyPasteButton/>
            <pre class="language-bash bg-zinc-50 dark:bg-zinc-900 rounded-md"><code x-ref="code" class="language-bash">uvx --from basic-components components add [component_name] </code></pre>
        </div>
    </TabsContent>
    <TabsContent value="pipx">
        <div class="relative" x-data><CopyPasteButton/>
            <pre class="language-bash bg-zinc-50 dark:bg-zinc-900 rounded-md"><code x-ref="code" class="language-bash">pipx install basic-components && components add [component_name]</code></pre>
        </div>
    </TabsContent>
</Tabs>

The components will be added to your project in the `components/ui/<component_name>` directory. 

### Example

```bash
✗ uvx --from basic-components components add button       
button (will be installed)
Installing button...

Copying from template version 0.2.0
    create  button/Button.jinja


╭────────────────────────────────────────────────────────── Installation Complete ───────────────────────────────────────────────────────────╮
│ ✓ Added button component                                                                                                                   │
│                                                                                                                                            │
│ components-dir=components/ui                                                                                                               │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
View the results
```bash
➜ tree components 
components
└── ui
    └── button
        └── Button.jinja

2 directories, 1 file

```

### Dependencies

Some components have dependencies on other components. When using the `components` command, any required components 
will also be installed. 

```bash
 ✗ uvx --from basic-components components add dropdown_menu
dropdown_menu (will be installed)
└── Dependencies
    ├── checkbox
    ├── icons/ChevronRight
    └── radio
Installing checkbox...

Copying from template version 0.2.0
    create  checkbox/Checkbox.jinja


Installing dropdown_menu...

Copying from template version 0.2.0
    create  dropdown_menu/DropdownMenuItem.jinja
    create  dropdown_menu/DropdownMenu.jinja
    create  dropdown_menu/DropdownMenuSubTrigger.jinja
    create  dropdown_menu/DropdownMenuTrigger.jinja
    create  dropdown_menu/DropdownMenuRadioItem.jinja
    create  dropdown_menu/DropdownMenuGroup.jinja
    create  dropdown_menu/DropdownMenuSub.jinja
    create  dropdown_menu/DropdownMenuSeparator.jinja
    create  dropdown_menu/DropdownMenuContent.jinja
    create  dropdown_menu/DropdownMenuSubContent.jinja
    create  dropdown_menu/DropdownMenuLabel.jinja
    create  dropdown_menu/DropdownMenuCheckboxItem.jinja


Installing icons/ChevronRight...

Copying from template version 0.2.0
    create  icons/ChevronRightIcon.jinja


Installing radio...

Copying from template version 0.2.0
    create  radio/RadioGroupItem.jinja
    create  radio/RadioGroup.jinja


╭────────────────────────────────────────────────────────── Installation Complete ───────────────────────────────────────────────────────────╮
│ ✓ Added dropdown_menu component                                                                                                            │
│ Installed dependencies:                                                                                                                    │
│   - dropdown_menu                                                                                                                          │
│   - icons/ChevronRight                                                                                                                     │
│   - radio                                                                                                                                  │
│                                                                                                                                            │
│ components-dir=components/ui                                                                                                               │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Components cli tool

The `components` cli tool has several options. 

Add a component
```bash
uvx --from basic-components add button
```

Add a component, specifying the repo
```bash
uvx --from basic-components add button --repo-url https://github.com/basicmachines-co/basic-components.git
```

Add a component, specifying the repo and branch or tag
```bash
uvx --from basic-components add button --repo-url https://github.com/basicmachines-co/basic-components.git --branch main
```

The `repo-url` arg can also point to a local directory if you have the project checked out. You can also pass the components 
destination directory via the `components-dir` arg.

## Copy/Paste

Code for components can also be copy/pasted directly from the example pages via the `Code` tabs. You can install components
anywhere in you project. The rest of the information in these docs assume they are located in the `components/ui` dir in
your project. See the [JinjaX](/docs/utilities#jinjax) docs for more info on how to set up components in your project.

## Next steps

See the [utilities](/docs/utilities) docs for more information about setting up your project to use the components. 

</Prose>