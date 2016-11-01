#!/usr/bin/env python3

import sys, json, cgi

fs = cgi.FieldStorage()
path = "/home/dima/Рабочий стол/ИБ(1-я лаба)"

with open (path + "/users.json", 'r') as db:
	response = json.load(db)

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

sys.stdout.write(json.dumps(response, indent=1))
sys.stdout.write("\n")

sys.stdout.close()

