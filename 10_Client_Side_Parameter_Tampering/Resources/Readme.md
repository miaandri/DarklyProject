# Proof of Concept
In the "/?page=recover" URL, we found that there an option to recover password. Usually, when we recover password, we need an email address (or something like). So we inspect the page and found 
**<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">**

So we change **hideen** to **test**. And we can change the mail value and find the flag cause the server trust us: "1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0" 

# Explanation

The fundamental problem here lies in a basic security principle: never trust the client. Instead of querying its database to find the admin's email, the server code thought: "I'll look at the email submitted via the form (in the 'mail' field) and send the reset link to that address."

# Solutions

- Never trust the client : Everything originating from the browser (forms, URL parameters, HTTP headers, cookies) must be considered potentially corrupted or manipulated by an attacker. The server must always validate and re-evaluate the data independently.
- Do not rely solely on hiding an important field to protect it.