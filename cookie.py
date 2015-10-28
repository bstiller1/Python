#!/usr/bin/python

import cgi, Cookie, os

form = cgi.FieldStorage()
user = form["uname"].value

print("Content-Type: text/html;charset=utf-8;")
print("Set-Cookie:User="+user+";expires=Thurs, Oct 29 2015 13:00:00 GMT;path=/;domain=blakestiller.com;")
print("")

html = """
<!DOCTYPE html>
<html lang='en'>
<head><title>Login</title>
<meta http-equiv='cookie' content='user=%s; expires=Thursday, 29-Oct-15 23:59:59 GMT;' />
</head>
<body>
<h3>Logging you in</h3>
<img src='../python/loader.gif' alt='Loading' />
<script>location.href = 'index.py'</script>
</body</html>"""
#print(html)

print(html % user)
cookie_string = os.environ.get('HTTP_COOKIE')
print("Cookies found: ", cookie_string)




