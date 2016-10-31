#!/usr/bin/env python3

""" 
	password_change.py -- изменение пароля
	пользователь или админ входит в систему,
	если пользователь/админ входит первый раз
	ему предлагается сменить пароль
"""

import sys
import json
import cgi
import shelve

path = "/home/dima/Рабочий стол/ИБ(1-я лаба)"

fs = cgi.FieldStorage()
addedPath = str()
username = "".join(fs.keys())
if username == "admin":
	addedPath = "/admin"
else:
	addedPath = "/users"

# считываем сериализованные данные из файла
data = shelve.open(path + addedPath, 'w')

data[username] = fs.getvalue(username)

with open(path + "/dump", 'w') as db:
	json.dump(dict(data), db)

data.close()

# сформировать ответ
result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()