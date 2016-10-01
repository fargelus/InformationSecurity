#!/usr/bin/env python3

"""
	saveUsers.py -- добавление списка пользоваетелей 
	в бд
"""

import sys, json
# from form_handler import path_db

receive_json = json.load(sys.stdin)

with open("/home/dima/Рабочий стол/ИБ(1-я лаба)/users.json", 'w') as outfile:
	json.dump(receive_json, outfile)

"""data.update(receive_json)

with open(path_db, 'w') as outfile:
	json.dump(outfile, data)"""










