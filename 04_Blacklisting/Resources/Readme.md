# Proof of Concept

In the bottom of the pages there is a section for the comment, so we test some XSS (Cross-Site Scripting) attack and we find that:

- if we put `<script>test</script>` or `test script` or `<scr<script>ipt>` or `h1` or another similar test in the comment and we find a normal behavior.
- But when we put "script", "a", "href", "p" , there is a flag : 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e

So we can say that there a blacklist for some HTML key word. 

# Explanation 

To prevent XSS attacks, the developer attempted to explicitly ban tags or attributes deemed dangerous (script, a, href, p). Whenever a user submits a comment, the server analyzes the text: if any of these forbidden words are detected, the filter reacts. But sometimes, these word are a simple comment.

# Solutions

To work around this error, the developer must stop using blacklisting and instead prioritize these methods: 

## Output Encoding

Before displaying a comment or any other user-supplied data within HTML code, the server must convert special characters into harmless HTML entities. For example, the symbols < and > become &lt; and &gt;. (For example in PHP, for instance, this is easily implemented using htmlspecialchars($text, ENT_QUOTES, 'UTF-8')). The browser then displays the text visually without ever interpreting it as executable code.

## Use CSP (Content Security Policy)

Configure the CSP HTTP header to strictly restrict the origin of scripts executed by the browser (for example, by disallowing the execution of inline scripts via `unsafe-inline`). Even if an XSS vulnerability remains in the code, a strict CSP will prevent the browser from executing a malicious payload.