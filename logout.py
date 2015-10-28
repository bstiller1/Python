#!/usr/bin/python

import cgi, Cookie, time, uuid

form = cgi.FieldStorage()
user = form.getvalue("user")
today = time.strftime("%H:%M:%S")
print("Content-Type: text/html;charset=utf-8;")
print("Set-Cookie:User=none;expires="+today+"; path=/; domain=blakestiller.com;")
print("")

html = """
<!DOCTYPE html>
<html lang='en'>
<head><title>Logout</title></head>
<body>
<h3>Logging you out</h3>
<img src='../python/loader.gif' alt='Loading' />
<script>location.href = 'index.py'</script>
</body</html>"""
print(html)
