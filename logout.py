#!/usr/bin/python

import cgi, Cookie, datetime, uuid

form = cgi.FieldStorage()
user = form.getvalue("user")
print("Content-Type: text/html; Set-Cookie:User=none;expires=0; path=/; domain=blakestiller.com;")
print("")

html = """
<!DOCTYPE html>
<html lang='en'>
<head><title>Logout</title></head>
<body>
<h3>Logging you out</h3>
<img src='loader.gif' alt='Loading' />
<script>location.href = 'index.py'</script>
</body</html>"""
print(html)
