#!/usr/bin/python

import Cookie, os

print("Content-Type: text/html;charset=utf-8;")
print("")

html = """
<title>Python Auth</title>
<h3>Welcome</h3>
<hr />
<p>%s</p>
<hr />"""

form = """
<title>Python Auth</title>
<h3>Login</h3>
<form method='post' action='login.py'>
<label for='uname'>User:<input type='text' name='uname' required/></label>
<label for='pass'>Pass:<input type='text' name='pass' required/></label>
<input type='submit' value='submit' />
</form>
<br /><a href='register.py' title='Register'>Register</a>
"""

# make cookie_string variable to check cookie
cookie_string = os.environ.get('HTTP_COOKIE')

# check for cookie
if "User" in cookie_string:
	print(html % "User Cookie found")
	# if cookie found check for user
	if "user1" in cookie_string:
		print("User:user1 was found")
else:
	# if cookie not found, show login form
	print(form)
#	print("Location: test.py\r\n")
