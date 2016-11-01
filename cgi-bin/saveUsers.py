#!/usr/bin/env python3

"""
	saveUsers.py -- добавление списка пользоваетелей 
	в бд
"""

import sys, json, cgi

fs = cgi.FieldStorage()
path = "/home/dima/Рабочий стол/ИБ(1-я лаба)"

receive = {}
try:	
	for k in fs.keys():
		receive[k] = fs.getvalue(k)
except TypeError:
	pass

with open(path + "/users.json", 'w') as db:
	json.dump(receive, db)

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

# сформировать ответ
result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()

