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

<IncludeTemplate template="examples/wtform.html"/>

<Prose>

The WTForm component makes it very easy to render, validate and handle form processing when using a form instance from  the [startlette-wtf](https://github.com/kubetail-org/starlette-wtf) lib. 
Using `starlette-wtf` you can add CSRF protection and declaritive validation to your forms.

## Code
</Prose>

<IncludeComponents :components="{{ metadata.templates }}" />

<Prose>
## Server Code
</Prose>
<IncludeTemplate dir="docs/demo" template="wtform.py" language="python" />
