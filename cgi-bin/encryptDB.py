#!/usr/bin/env python3

import pickle
import json

path = "/home/dima/Рабочий стол/ИБ(1-я лаба)"

with open(path + "/admin.json") as db:
	adminData = json.load(db)

with open(path + "/users.json") as db:
	usersData = json.load(db)

with open(path + "/admin.pickle", 'wb') as binary:
	pickle.dump(adminData, binary)

with open(path + "/users.pickle", 'wb') as binary:
	pickle.dump(usersData, binary)

""" getDump
with open(path + "/dump", 'w') as dump:
	json.dump(usersData, dump)"""


