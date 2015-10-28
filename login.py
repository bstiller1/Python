#!/usr/bin/python

import sqlite3, cgi, Cookie, datetime, uuid

# Print necessary headers.
print("Content-Type: text/html")
print('')

print('<html lang="en">')
print('<head><title>Sqlite Test</title></head>')
print('<body>')

form = cgi.FieldStorage()
user = form["uname"].value
pword = form["pass"].value
#user = form.getvalue("uname")
#pword = form.getvalue("pass")

# Connect to the database.
conn = sqlite3.connect('../../db/auth.db')
c = conn.cursor()

#query DB put data in vars
for row in c.execute('SELECT uname, pass FROM users WHERE uname = "'+user+'" AND pass = "'+pword+'"'):
    #print(row[0])
    #print(row[1])
	userCon = row[0]
	passCon = row[1]

if user in userCon:

# username and password found redirect to cookie.py
	print("<form name='login' action='cookie.py' method='post'><input type='hidden' name='user' value='"+user+"'/></form>")
	print("<script>login.submit();</script>")
else:
	print("Wrong Username and or Password.")
	

# close connection to Database
conn.close()



#print('</body>')
#print('</html>')