# Proof of Concept

In the home page there's a redirection named BornToSec 

An attacker can bypass the restrictions imposed by the server by manually forging the required HTTP headers (Referer and User-Agent) using a command-line tool like curl.

So we do : **curl -H "Referer: https://www.nsa.gov/" -H "User-Agent: ft_bornToSec" "http://X.X.X.X/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | grep "flag"**

And get the flag : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

# Explanation
This vulnerability stems from insecure access control logic that relies entirely on client-controlled metadata. Specifically, the application evaluates two standard HTTP request headers:

- Referer: Intended to indicate the address of the web page that linked to the currently requested resource. However, since the browser (or any HTTP client) generates this header, it can be altered arbitrarily.

- User-Agent: Intended to identify the client software, operating system, or browser vendor. Like the Referer, it is completely controlled by the client and trivial to spoof.

# Solutions

## Enforce Proper Authentication and Authorization

Replace header checks with secure session management. Users should be authenticated via secure, cryptographically signed session cookies or tokens (such as JWTs) stored securely on the server side or validated against a database.


## Treat Headers as Untrusted Metadata

If Referer or User-Agent data must be collected for logging, analytics, or debugging, treat them strictly as untrusted inputs. They should never dictate application logic or security permissions.