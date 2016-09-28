#!/usr/bin/env python3

"""
 	form_handler.py -- обработчик входа в систему
 	скрипт генерит статику в зависимости от 
 	от кол-ва входов в систему пользователя/админа
"""

import cgi
import json

path_db = "/home/dima/Рабочий стол/ИБ(1-я лаба)/db.json"

def list_of_users_win():
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработчик формы</title>
        </head>
        <body>""")

	print("""<div class="main">
				<h1> Список пользователей </h1>
				<form name="admin" class="adminInput" method="post" action="somescript">
					<textarea placeholder="Список пользователей" name="Список пользователей"></textarea>
					<p> Блокировка <input type="checkbox"> </p>
					<p> Парольное ограничение <input type="checkbox"> </p>
					<p>
						<input type="submit" value="Добавить нового пользователя">
					</p>
					<p>
						<p> Имя нового пользователя: </p>
						<input type="text" name="login">
						<p> Задайте пароль: </p>
						<input type="text" name="login">
					<p>
						<input type="submit" value="Ок">
						<input type="submit" value="Отмена">
					</p>
					<p>
						<input type="submit" value="Сохранить">
						<input type="submit" value="Отмена">
					</p>
				</form>
			</div>""")

	print("""</body>
        </html>""")

def change_pwd(login):
	with open(path_db) as db:
		data = json.load(db)

	if login == "admin":
		data[login][2] += 1
	data[login][1] = "true"

	with open(path_db, 'w') as outfile:
		json.dump(data, outfile)

	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Смена пароля</title>
            <link href="../css/entrance.css" rel="stylesheet">
            <link href="../css/change_password.css" rel="stylesheet">
            <script type="text/javascript" src="../js/loadData.js"></script>
            <script type="text/javascript" src="../js/test.js"></script>
        </head>
        <body>""")

	print("""<div class="main">
				<h1> Смена пароля </h1>
				<form name="admin" action="saveData.py" method="post">
					<div class="firstRow">
						<p> Новый пароль: </p>
						<input type="password" name="newPasswd" required id="pwd" onchange=validatePassword();>
					</div>
					<div class="secondRow">
						<p> Подтверждение: </p>
						<input type="password" name="verification" required id="conf_pwd" onkeyup="validatePassword()">
					</div>
					<p>
						<input type="submit" value="Поменять">
					</p>
				</form>
			</div>""")

	print("""</body>
        </html>""")

if __name__ == '__main__':
	form = cgi.FieldStorage()
	login = form.getfirst("login")

	with open(path_db) as db:
		data = json.load(db)
	if login == "admin" and data["admin"][2] > 0:
		list_of_users_win()
	else:
		change_pwd(login)
	

