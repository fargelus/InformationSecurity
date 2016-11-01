#!/usr/bin/env python3

"""
 	form_handler.py -- обработчик входа в систему
 	скрипт генерит статику в зависимости от 
 	от кол-ва входов в систему пользователя/админа
"""

import cgi
import json

def list_of_users_win():
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработчик формы</title>
            <script src="../js/CryptoJS v3.1.2/rollups/aes.js"></script>
            <script src="../js/jQuery.js"></script>
            <script src="../js/addUser.js"></script>
            <link href="../css/usersList.css" rel="stylesheet">
        </head>
        <body>""")

	print("""<div class="main">
				<form name="admin" class="adminInput" method="post" action="somescript">
					<table border="1">
						<caption> Список пользователей </caption>
						<tr>
							<th> Логин </th>
							<th> Пароль </th>
							<th> Блокировка </th>
							<th> Ограничение </th>
							<th> Кол-во входов в систему </th>
						</tr>
					</table>

					<p>
						<input type="button" value="Добавить нового пользователя" onclick="add();">
						<input type="button" value="Изменить" onclick="change();">
					</p>

					<div id="add_form">
						<div class="labels">
							<div class="rows">
								<p> Имя нового пользователя: </p>
								<input type="text" name="add_login" required id="loginData">
							</div>
							<div class="rows">
								<p> Задайте пароль: </p>
								<input type="password" name="add_password" required id="passwordData">
							</div>
						</div>	
						<div class="others">					
							<p> Блокировка <input type="checkbox" id="block"> </p>
							<p> Парольное ограничение <input type="checkbox" id="limitation"> </p> 
							<p>
								<input type="button" value="Добавить" class="finally_add" onclick="addUser();">
							</p>
						</div>
					</div>

					<div id="change_form">
						<div id="login_select">
							<div class="labels">
								<div class="rows">
									<p> Логин: </p>
									<input type="text" id="login_for_change">
								</div>
							</div>
							<p>
								<input type="button" value="Дальше" id="next" onclick="go_next();">		
							</p>
						</div>
						<div id="change_select">
							<div class="others">							
								<p> Блокировка <input type="checkbox" id="change_block"> </p>
								<p> Парольное ограничение <input type="checkbox" id="change_limit"> </p>
								<p>
									<input type="button" value="Удалить пользователя" onclick="del();">
								</p>
								<p>
									<input type="button" value="Сохранить изменения" onclick="saveChanges();">	
								</p>
							</div>
						</div>
					</div>

					<p>
						<input type="button" value="Сохранить" id="save_btn">
						<input type="button" value="Выход" id="exit_btn">
         			</p>
				</form>
			</div>""")

	print("""</body>
        </html>""")

def change_pwd():
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Смена пароля</title>
            <link href="../css/entrance.css" rel="stylesheet">
            <link href="../css/change_password.css" rel="stylesheet">
            <script src="../js/jQuery.js"></script>
            <script src="../js/savePassword.js"></script>
        </head>
        <body>""")

	print("""</body>
        </html>""")

if __name__ == '__main__':
	form = cgi.FieldStorage()
	login = form.getfirst("login")

	addedPath = str()
	if login.lower() == "admin":
		login = login.lower()
		addedPath = "/admin.json"
	else:
		addedPath = "/users.json"

	path = "/home/dima/Рабочий стол/ИБ(1-я лаба)"
	with open(path + addedPath, 'r') as db:
		data = json.load(db)

	if login == "admin" and data["admin"][1] > 0:
		list_of_users_win()
	else:
		change_pwd()