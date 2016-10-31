#!/usr/bin/env python3

"""
	saveUsers.py -- добавление списка пользоваетелей 
	в бд
"""

import sys, json, cgi
from encryptDB import path
import shelve

fs = cgi.FieldStorage()

receive = {}
try:	
	for k in fs.keys():
		receive[k] = fs.getvalue(k)
except TypeError:
	pass

data = shelve.open(path + "/users", 'w')
for key in receive:
	data[key] = receive[key]

data.close()

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

