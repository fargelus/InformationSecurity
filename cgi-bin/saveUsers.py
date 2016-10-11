#!/usr/bin/env python3

"""
	saveUsers.py -- добавление списка пользоваетелей 
	в бд
"""

import sys, json, cgi

users_path = "/home/dima/Рабочий стол/ИБ(1-я лаба)/users.json"

fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"

receive = {}
try:
	result['keys'] = ",".join(fs.keys())
	for k in fs.keys():
		receive[k] = fs.getvalue(k)
except TypeError:
	pass

with open(users_path, 'w') as buf:
	json.dump(receive, buf)

# сформировать ответ
result['data'] = receive

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()

