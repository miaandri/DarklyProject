# Proof of Concept
robots.txt revealed the **/.hidden/** directory. The directory contained many nested paths with publicly accessible README files. A recursive script was used to enumerate these paths and retrieve the files, one of which contained the flag: **d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466**.

# Explanation
The vulnerability is sensitive information disclosure caused by publicly accessible files and directories. robots.txt exposed the location, while the web server allowed unauthenticated access to the contents.

# Solutions
- Remove sensitive files from the web-accessible directory.
- Restrict private resources with authentication/authorization.
- Disable directory listing where unnecessary.
- Do not rely on robots.txt to protect sensitive files.