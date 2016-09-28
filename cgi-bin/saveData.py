#!/usr/bin/env python3

""" 
	saveData.py -- изменение пароля
	пользователь или админ входит в систему,
	если пользователь/админ входит первый раз
	ему предлагается сменить пароль
"""

import cgi
from form_handler import path_db
import json

if __name__ == '__main__':
	form = cgi.FieldStorage()
	newPasswd = form.getfirst("newPasswd")

	# открыть бд
	with open(path_db) as db:
		data = json.load(db)

	# проверить зн-ия полей
	for attr in data.values():
		if "true" in attr:
			attr[0] = newPasswd

	# записать новое значение
	with open(path_db, 'w') as outfile:
		json.dump(data, outfile)
	
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
        <html>
        	<head>
            	<meta charset="utf-8">
        	</head>
        	<body>
        		<h1> Пароль успешно изменён </h1>
        		<!-- сделать здесь анимацию -->
        		<p> <a href="../index.html"> </a> </p>
        	</body>
        </html>""")