#!/usr/bin/env python3

"""
	test.py -- пробуем добавить данные в бд,
	используя ajax и jQuery
"""

import cgi, cgitb
from form_handler import path_db
import json

data = cgi.FieldStorage()
new_user = data["add_login"]
new_password = data["add_password"]

with open(path_db) as db:
	db_data = json.load(db)

db_data[new_user] = new_password

with open(path_db, 'w') as db:
	json.dump(db_data, db)










