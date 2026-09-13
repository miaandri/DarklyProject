# Data URI-Based XSS

## The Vulnerable URL

The application normally loads an image using the `src` parameter:

```text
http://x.x.x.x/?page=media&src=images/nsa_prism.jpg
```

The application likely inserts the parameter into an HTML element such as:

```html
<img src="images/nsa_prism.jpg">
```

Since the application does not properly validate the `src` parameter, it accepts more than just image files.

---

## The `data:` URI Scheme

Browsers support several URI schemes besides `http://` and `https://`.

One of them is the **data URI**, which allows an entire file to be embedded directly inside a URL.

General syntax:

```text
data:[MIME type][;encoding],data
```

Examples:

```text
data:text/plain,Hello
```

```text
data:text/html,<h1>Hello</h1>
```

When using HTML, it is common to Base64 encode the content to avoid problems with special characters.

---

## The Payload

The challenge payload is:

```text
?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgyKTs8L3NjcmlwdD4=
```

Breaking it down:

- `data:` → Use a data URI.
- `text/html` → Treat the content as an HTML page.
- `base64` → The content is Base64 encoded.
- `PHNjcmlwdD5hbGVydCgyKTs8L3NjcmlwdD4=` → Encoded HTML.

Decoding the Base64 produces:

```html
<script>alert(2)</script>
```

The browser therefore loads:

```text
data:text/html,<script>alert(2)</script>
```

which creates a small HTML page and immediately executes the JavaScript.

---

## Why It Works

If the application loads the `src` value inside an element capable of rendering HTML (for example an `<iframe>`), the browser interprets the data URI as a complete HTML document instead of an image.

As soon as the HTML is loaded, the `<script>` tag executes.

The `alert()` is simply a proof-of-concept showing that arbitrary JavaScript can run.

---

## Flag

The flag is **928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d**
