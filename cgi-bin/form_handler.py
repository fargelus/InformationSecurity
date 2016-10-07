#!/usr/bin/env python3

"""
 	form_handler.py -- обработчик входа в систему
 	скрипт генерит статику в зависимости от 
 	от кол-ва входов в систему пользователя/админа
"""

import cgi
import json

path_db = "/home/dima/Рабочий стол/ИБ(1-я лаба)"

def list_of_users_win():
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработчик формы</title>
            <script type="text/javascript" src="../js/jQuery.js"></script>
            <script type="text/javascript" src="../js/addUser.js"></script>
            <!-- <link href="../css/usersList.css" rel="stylesheet"> -->
        </head>
        <body>""")

	print("""<div class="main">
				<h1> Список пользователей </h1>
				<form name="admin" class="adminInput" method="post" action="somescript">

					<table border="1">
						<tr>
							<th> Логин </th>
							<th> Пароль </th>
							<th> Блокировка </th>
							<th> Ограничение </th>
						</tr>
					</table>

					<!-- <textarea disabled placeholder="Список пользователей" name="Список пользователей" id="usersList"></textarea>-->
					
					<!-- 
					<p> Блокировка <input type="checkbox"> </p>
					<p> Парольное ограничение <input type="checkbox"> </p>
					<p>
						<input type="button" value="Добавить нового пользователя">
					</p> -->

					<div class="add_form">
						<p> Имя нового пользователя: </p>
						<input type="text" name="add_login" required id="loginData">
						<p> Задайте пароль: </p>
						<input type="text" name="add_password" required id="passwordData">
						<p>
							<input type="button" value="Добавить" class="finally_add" onclick="addUser()">
						</p>
					</div>

					<!--
					<p>
						<input type="button" value="Сменить пароль">
					</p> -->
					<p>
						<input type="button" value="Сохранить" id="add_btn">
					</p>
				</form>
			</div>""")

	print("""</body>
        </html>""")

def change_pwd(login):
	with open(path_db) as db:
		data = json.load(db)

	# если входит админ, то
	# увеличиваем кол-во входов на 1
	if login == "admin":
		data[login][1] = 1
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
            <script type="text/javascript" src="../js/jQuery.js"></script>
            <script type="text/javascript" src="../js/loadData.js"></script>
            <script type="text/javascript" src="../js/savePassword.js"></script>
        </head>
        <body>""")

	first_index = path_db.rfind('/')
	last_index = path_db.rfind('.')
	address = path_db[first_index+1:last_index]

	main_part = """<div class="main">
				<h1> Смена пароля </h1>
				<form name="admin" action="saveData.py" method="post">
					<div class="firstRow">
						<p> Новый пароль: </p>
						<input type="password" name="newPasswd" required id="pwd" onchange="validatePassword();">
					</div>
					<div class="secondRow">
						<p> Подтверждение: </p>
						<input type="password" name="verification" required id="conf_pwd" onkeyup="validatePassword();">
					</div>
					<p>
						<input type="button" value="Поменять" id="save_btn" onclick="save({0}, {1});">
					</p>
				</form>
			</div>""".format(login, address)
	print(main_part)

	print("""</body>
        </html>""")

if __name__ == '__main__':
	form = cgi.FieldStorage()
	login = form.getfirst("login")

	if login.lower() == "admin":
		login = login.lower()
		path_db += "/admin.json"
	else:
		path_db += "/users.json"

	with open(path_db) as db:
		data = json.load(db)
	if login == "admin" and data["admin"][1] > 0:
		list_of_users_win()
	else:
		change_pwd(login)
	