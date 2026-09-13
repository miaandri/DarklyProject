# Proof of Concept

By inspecting the cookies stored in the browser, we can identify a key-value pair named **I_am_admin**. Its value is an MD5 hash:

**68934a3e9455fa72420237eb05902327**


After cracking the hash, we find that it corresponds to the value false. This suggests that the current session does not have administrator privileges.

Since the application appears to determine admin access based on this cookie value, we can test whether changing it to the MD5 hash of true grants administrative access.

The MD5 hash of true is:

**b326b5062b2f0e69046810717534cb09**


Replacing the existing cookie value with this hash and reloading the page successfully grants us admin access.

A prompt then appears, providing the flag:

**df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3**

# Explanation

The application trusts a client-controlled cookie to determine whether the user is an administrator. Because the cookie value is only an MD5 hash of a predictable boolean value, it can be easily modified to bypass the intended access control.



# Solution

## Perform authorization checks server-side 
The server should determine whether a user has admin privileges based on their authenticated account/session. And do not store privilege information directly in client-controlled cookies.
