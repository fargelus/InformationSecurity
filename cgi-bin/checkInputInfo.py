#!/usr/bin/env python3

import sys, json, cgi, shelve
import os

fs = cgi.FieldStorage()
path = "/home/dima/Рабочий стол/ИБ(1-я лаба)"

# расшифровыем наши базы во временные файлы
adminData = {}
usersData = {}

# если базы данных ещё не расшифрованы
# расшифровываем их
if not os.path.isfile(path + "/admin" + ".json"):
	adminDb = shelve.open(path + "/admin", 'r')
	adminData = dict(adminDb)
	adminDb.close()
	with open(path + "/admin" + ".json", 'w') as db:
		json.dump(adminData, db)
else:
	with open(path + "/admin" + ".json", 'r') as db:
		adminData = json.load(db)

if not os.path.isfile(path + "/users" + ".json"):
	usersDb = shelve.open(path + "/users", 'r')
	usersData = dict(usersDb)
	usersDb.close()
	with open(path + "/users" + ".json", 'w') as db:
		json.dump(usersData, db)
else:
	with open(path + "/users" + ".json", 'r') as db:
		usersData = json.load(db)

# ------------------------------------------

# кто входит пользователь или админ?
username = "".join(fs.keys())
offset = int()		# индекс кол-ва входов в систему
data = {}
if username == "admin":
	data = adminData
	offset = 1
else:
	data = usersData
	offset = 3

# ответ - это данные о пользователе
response = {}
for key in data:
	if key == username:
		response[key] = data[key]
		value = int(response[key][offset])
		value += 1
		response[key][offset] = str(value)
		break

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

sys.stdout.write(json.dumps(response, indent=1))
sys.stdout.write("\n")

sys.stdout.close()
