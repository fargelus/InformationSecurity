#!/usr/bin/env python3

import sys, json, cgi, shelve

fs = cgi.FieldStorage()

path = "/home/dima/Рабочий стол/ИБ(1-я лаба)"

addedPath = str()
username = "".join(fs.keys())
offset = int()		# индекс кол-ва входов в систему
if username == "admin":
	addedPath = "/admin"
	offset = 1
else:
	addedPath = "/users"
	offset = 3
	# fs.getvalue(username)

selectedDb = shelve.open(path + addedPath, 'w')

with open(path + "/dump", 'w') as dump:
	json.dump(dict(selectedDb), dump)

response = {}
for key in selectedDb.keys():
	if key == username:
		response[key] = selectedDb[key]
		# selectedDb[key][offset] += 1
		break

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

sys.stdout.write(json.dumps(response, indent=1))
sys.stdout.write("\n")

sys.stdout.close()

selectedDb.close()

"""with open(path + addedPath, 'wb') as db:
	pickle.dump(selectedDb, db)"""
