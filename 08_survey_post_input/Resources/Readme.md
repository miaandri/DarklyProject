# Exploit

On the survey page, the grade is selected using an HTML <option> element. However, the value submitted by the client is not properly validated by the server.

Using the browser's Developer Tools, we can modify the value of the grade directly in the HTML.

For example, the original option:

`<option value="5">5</option>`

can be changed to:

`<option value="5000">500</option>`

After submitting the modified value, the server accepts the tampered input and redirects us to the flag:

`03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa`


The important point is that modifying the HTML in the browser should not be enough to bypass the application's restrictions. The browser is fully controlled by the user, so any client-side value must be considered untrusted.

# Solution

The vulnerability occurs because the server does not properly validate the submitted grade.

The application relies on the values defined in the HTML form, but these values can be modified by the client before the request is sent.

A secure implementation should validate the submitted value server-side, ensuring that it matches the allowed range or set of valid grades.
