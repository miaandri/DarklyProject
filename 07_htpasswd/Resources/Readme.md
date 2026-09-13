# Proof of Concept

We have find that there are a root /whatever and inside there is a **.htpasswd file**

The file has permission to be read and inside we have find **qwerty123@** in MD5 hash 

So we go to **/admin** and use the .htpasswd file information and find the flag : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

# Explanation

The **.htpasswd** file is a plain-text configuration file used by web servers (such as Nginx and Apache) to store usernames and encrypted passwords for Basic HTTP Authentication.

Normally, files with names starting with a dot (.) are hidden files that web servers are configured to block automatically for security reasons. Here we have a big information disclosure.

# Solutions 
## Restrict access rights 

Strictly configure the web server to deny external access to all files starting with a dot (.).

## Use a robust hashing algorithm like bycrypt for the <.htpasswd> file 