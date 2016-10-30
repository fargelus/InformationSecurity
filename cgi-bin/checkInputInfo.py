#!/usr/bin/env python3

import sys, json, cgi, pickle
from encryptDB import path
import os

fs = cgi.FieldStorage()

here = os.path.dirname(os.path.abspath(__file__))

addedPath = str()
username = "".join(fs.keys())
offset = int()		# индекс кол-ва входов в систему
if username == "admin":
	addedPath = "/admin.pickle"
	offset = 1
else:
	addedPath = "/users.pickle"
	offset = 3
	# fs.getvalue(username)

with open(os.path.join(here, addedPath[1:]), 'rb') as db:
	selectedDb = pickle.load(db)
	with open(path + "/dump", 'w') as dump:
		json.dump(selectedDb, dump)

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

"""with open(path + addedPath, 'wb') as db:
	pickle.dump(selectedDb, db)"""
