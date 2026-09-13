# Proof of Concept

In the URL that contain a query "page=", we tested to do a **Path Transversal** (a web security flaw that lets attackers access restricted files and directories outside of an application's intended folder) with an **Overshooting**

So we found the flag "b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0"

# Explanation

If the web page loads files dynamically via the URL (e.g., ?page=accueil.php), an attacker can replace accueil.php with a sequence of ../ to escape the website directory and navigate the server's internal files.
The server developer took the value from the URL (such as the `$_GET['page']` parameter in PHP) and passed it directly—without any validation to a critical system function (like `include()`, `require()`, or `file_get_contents()`).
The developer assumed incorrectly that users would dutifully click on the links provided by the site (e.g., ?page=contact.php). He did not anticipate that an attacker would manually modify the URL.

# Solutions

## Sanitization

The developer must block or sanitize specific elements like :

- Directory traversal sequences: ../ or ..\

- Protocol wrappers: data://, http://, or php://

- Forward slashes (/), if the file must strictly remain within a single folder.

## Using whitelist

Instead of trying to anticipate and block every possible attack, the developer should use a whitelist approach.

A whitelist defines exclusively what is permitted. Everything else even if it does not appear dangerous is blocked by default.
