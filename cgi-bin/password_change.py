#!/usr/bin/env python3

""" 
	password_change.py -- изменение пароля
	пользователь или админ входит в систему,
	если пользователь/админ входит первый раз
	ему предлагается сменить пароль
"""

import sys
from form_handler import path_db
import json

receive_password = json.load(sys.stdin)

with open("/home/dima/Рабочий стол/ИБ(1-я лаба)/buffer") as buf:
	data = buf.readlines()

login = data[0].rstrip()
address = data[1].rstrip()

with open(address) as db:
	data = json.load(db)

data[login][0] = receive_password["password"]

with open(address, 'w') as db:
	json.dump(data, db)

"""with open(path_db) as db:
	data = json.load(db)

data[login] = receive_password

with open(path_db, 'w') as db:
	json.dump(data)"""
	
		


