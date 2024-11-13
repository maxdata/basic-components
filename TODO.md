- components
- [x] mode toggle dropdown link whole item
- [x] toast min width
- [x] dialog scroll 
- [-] only add example if examples
- [x] center demo h/v
- [x] copy/paste button position
- [x] component tab scroll 
- [x] site heading
- [-] smaller font for code blocks
- [x] code blocks scroll above nav
- [x] component arg descriptions
- [x] toc indent
- [x] mobile nav
- [x] mobile content width

- examples
- [x] example names
- [x] card example - select is wonky on content example
- [x] popover content demo - compare to shadcn
- [x] select - dropdown width in example
- [x] checkbox disabled example
- [x] text area examples - spacing
- [x] icons
- [x] wtform demo
- [-] table sorting example -> htmx
- [x] fastapi 

- docs
- [x] Introduction
- [x] Installation
- [x] JinjaX
- [x] HTMX
- [x] Dark Mode
- [x] CLI
- [x] Typography
- [x] About
- [x] Contribution
- [x] GitHub link
- [x] site footer
- [x] favicon
- [x] copy/paste button on code blocks is sometimes off
- [x] AI - llms.txt
- [ ] Changelog - tagging and conventional commits
- [ ] package components in sub dirs?
- [ ] monetization strategy
- [ ] tool to install component via copier



# Basic Components Project Roadmap


## 2. Component Completion Strategy

### Priority Components to Complete Next
1. **Navigation Core**
    - Navigation-menu
    - Menubar
    - Breadcrumb
      These form the foundation of site navigation and are commonly needed.

2. **Essential UI Components**
    - Tabs
    - Progress
    - Separator
      These provide basic UI functionality most applications need.

3. **Enhancement Components**
    - Hover-card
    - Tooltip
    - Toggle
      These add polish and improve UX.


## 3. Documentation & Examples

### Front Page Examples
Create compelling examples showcasing:
1. **Basic Form Processing**
```html
<Form hx-post="/submit">
  <Input name="email" label="Email" required />
  <Button type="submit">Subscribe</Button>
</Form>
```

2. **Interactive Dialog**
```html
<Dialog x-data="{ open: false }">
  <Button x-on:click="open = true">Open Settings</Button>
  <DialogContent x-show="open">
    <h2>Settings</h2>
    <Button x-on:click="open = false">Close</Button>
  </DialogContent>
</Dialog>
```

3. **Data Table with Sorting**
```html
<Table hx-get="/api/users" hx-trigger="sort">
  <TableHeader>
    <TableColumn sortable>Name</TableColumn>
    <TableColumn sortable>Email</TableColumn>
  </TableHeader>
</Table>
```

## 4. Project Management
### Changelog & Version Control
1. **Implement Conventional Commits**
    - feat: New features
    - fix: Bug fixes
    - docs: Documentation changes
    - style: Code style changes
    - refactor: Code refactoring
    - test: Test updates
    - chore: Maintenance tasks

2. **Version Tagging Strategy**
    - Major (x.0.0): Breaking changes
    - Minor (0.x.0): New features
    - Patch (0.0.x): Bug fixes
    - Example: v1.2.3

### Release Strategy
- Regular releases (bi-weekly/monthly)
- Clear changelogs
- Migration guides for breaking changes
- Component status updates

## 5. Monetization Strategy
### Tiered Approach
1. **Open Source Core**
    - All basic components
    - Documentation
    - Examples
    - Community support

2. **Premium Components**
    - Advanced components (Calendar, Chart, Carousel)
    - Complex integrations
    - Premium themes
    - Priority support

3. **Enterprise Support**
    - Custom component development
    - Implementation consulting
    - Priority bug fixes
    - Direct support channel

### Additional Revenue Streams
1. **Documentation & Training**
    - Advanced tutorials
    - Video courses
    - Best practices guides
    - Implementation patterns

2. **Themes & Templates**
    - Premium design systems
    - Industry-specific templates
    - Custom variants
    - Dark mode optimizations

3. **Integration Services**
    - FastAPI/Django setup
    - Component customization
    - Performance optimization
    - Security hardening


## Success Metrics
- Component adoption rate
- GitHub stars/forks
- Documentation usage
- Community contributions
- Premium subscriptions
- Support ticket resolution
- Implementation examples