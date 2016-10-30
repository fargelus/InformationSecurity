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
import pickle
from encryptDB import path
import os

here = os.path.dirname(os.path.abspath(__file__))

fs = cgi.FieldStorage()
addedPath = str()
username = "".join(fs.keys())
if username == "admin":
	addedPath = "/admin.pickle"
else:
	addedPath = "/users.pickle"

# считываем сериализованные данные из файла
with open(path + addedPath, 'rb') as db:
	data = pickle.load(db)

data[username] = fs.getvalue(username)

with open(path + addedPath, 'wb') as db:
	pickle.dump(data, db)

with open(path + addedPath, 'rb') as db:
	new_data = pickle.load(db)

with open(path + "/dump", 'w') as db:
	json.dump(new_data, db)

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