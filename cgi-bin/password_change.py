#!/usr/bin/env python3

""" 
	password_change.py -- изменение пароля
	пользователь или админ входит в систему,
	если пользователь/админ входит первый раз
	ему предлагается сменить пароль
"""

import sys
import json
import fileinput
import cgi

fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"
result['keys'] = ",".join(fs.keys())

receive = {}
for k in fs.keys():
    receive[k] = fs.getvalue(k)

address = ""
if receive["address"] == "admin":
	address = "/home/dima/Рабочий стол/ИБ(1-я лаба)/admin.json"
else:
	address = "/home/dima/Рабочий стол/ИБ(1-я лаба)/users.json"

with open(address) as db:
	data = json.load(db)

data[receive["login"]][0] = receive["password"]

with open(address, 'w') as db:
	json.dump(data, db)

# сформировать ответ
result['data'] = receive

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()