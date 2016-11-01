#!/usr/bin/env python3

import shelve
import json
import os
import cgi
import sys

fs = cgi.FieldStorage()

path = "/home/dima/Рабочий стол/ИБ(1-я лаба)"

adminData = {}
with open(path + "/admin.json") as db:
	adminData = json.load(db)
os.remove(path + "/admin.json")	
admin_shelve = shelve.open("/home/dima/Рабочий стол/ИБ(1-я лаба)/admin", 'c')
admin_shelve.clear()
admin_shelve.update(adminData)
admin_shelve.close()

usersData = {}
with open(path + "/users.json") as db:
	usersData = json.load(db)
os.remove(path + "/users.json")
users_shelve = shelve.open("/home/dima/Рабочий стол/ИБ(1-я лаба)/users", 'c')
users_shelve.clear()
users_shelve.update(usersData)
users_shelve.close()

response = {}
response["Success"] = True
sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

sys.stdout.write(json.dumps(response, indent=1))
sys.stdout.write("\n")

sys.stdout.close()
