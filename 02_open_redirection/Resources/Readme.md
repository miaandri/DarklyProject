# Proof of Concept

In the bottom of the site we can see that there is a redirection to "facebook, X, Instagram"
If we wanna go to {somewhere}, the redirection request is that **http://XXX.XXX.XXX.XXX/index.php?page=redirect&site="{somewhere}"**. And of course the server allowed the redirection anywhere {somewhere} is.
And we have the flag: b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3

# Explanation

The problem is that the server-side script takes the value of the `site` parameter and redirects the user there without verifying whether the address is legitimate.

# Solution
## Using whitelist
Instead of trusting every value of the query `site`, the developer should use a whitelist approach.

A whitelist defines exclusively what is permitted. Everything else even if it does not appear dangerous is blocked by default.
