#!/usr/bin/env python3

import cgi

form = cgi.FieldStorage()
login = form.getfirst("login")
password = form.getfirst("password")
conf_pwd = form.getfirst("confirm_pwd")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработчик формы</title>
        </head>
        <body>""")

print("<p>login: {}</p>".format(login))
print("<p>password: {}</p>".format(password))
print("<p>conf_pwd: {}</p>".format(conf_pwd))

print("""</body>
        </html>""")
