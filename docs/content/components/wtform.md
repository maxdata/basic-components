---
title: WTForm
description: Render a WTForm with declarative validation, error handling and csrf protection.
component: wtform
templates:
  - WTForm.jinja
---

<Card className="m-10">
  <CardHeader>
    <CardTitle>User Profile</CardTitle>
    <CardDescription>Enter your profile information</CardDescription>
  </CardHeader>
  <CardContent>
    <div
        id="wtform"
        hx-get="/demo/wtform"
        hx-trigger="load"
    >
    </div>
  </CardContent>
</Card>



<Prose>

## Usage

</Prose>

<IncludeFiles :files="[
{'name': 'wtform.html', 'file': 'docs/templates/examples/wtform.html', 'lang':'html'},
{'name': 'wtform.py', 'file': 'docs/demo/wtform.py', 'lang':'python'}]"/>

<Prose>

The WTForm component makes it very easy to render, validate and handle form processing when using a form instance from  the [startlette-wtf](https://github.com/kubetail-org/starlette-wtf) lib. 
`Starlette-WTF` adds CSRF protection and declarative validation to your forms.

With the [htmx Response Targets Extension](https://htmx.org/extensions/response-targets/) you can direct error respones to targets in the DOM. 
The server can return a response with an error code to display errors inline on the page. For more info, see [htmx](/docs/htmx). 

## Code
</Prose>

<IncludeComponents dir="extras" :components="{{ metadata.templates }}" />

