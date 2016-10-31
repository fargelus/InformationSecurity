#!/usr/bin/env python3

import sys, json, cgi, shelve
from encryptDB import path

fs = cgi.FieldStorage()

data = shelve.open(path + "/users")
path_to_write = path + "/users"
with open(path + "/dump", 'w') as dump:
	dump.write(path_to_write)

response = dict(data)
data.close()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

sys.stdout.write(json.dumps(response, indent=1))
sys.stdout.write("\n")

sys.stdout.close()

