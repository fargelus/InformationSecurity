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

path = "/home/dima/Рабочий стол/ИБ(1-я лаба)"

fs = cgi.FieldStorage()
addedPath = str()
username = "".join(fs.keys())
if username == "admin":
	addedPath = "/admin.json"
else:
	addedPath = "/users.json"

with open(path + addedPath, 'r') as db:
	data = json.load(db)

# меняем пароль
data[username] = fs.getvalue(username)

# записываем изменения
with open(path + addedPath, 'w') as db:
	json.dump(data, db)

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