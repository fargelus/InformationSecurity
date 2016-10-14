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
            <script type="text/javascript" src="../js/CryptoJS v3.1.2/rollups/aes.js"></script>
            <script type="text/javascript" src="../js/jQuery.js"></script>
            <script type="text/javascript" src="../js/addUser.js"></script>
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
								<input type="button" value="Добавить" class="finally_add" onclick="addUser()">
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
							<div class="labels">
								<div class="rows">
									<p> Изменить пароль: </p> <!-- пароль хранится в расшифрованном виде -->
									<input type="password" id="change_passwd" required>
								</div>
							</div>
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

def change_pwd(login):
	with open(path_db) as db:
		data = json.load(db)

	# если входит админ, то
	# увеличиваем кол-во входов на 1
	if login == "admin":
		# data[login][1] = 1 FIX ME
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

	main_part = """<div class="main">
				<h1> Смена пароля </h1>
				<form name="admin" action="saveData.py" method="post">

					
						<div class="firstRow">
							<p> Старый пароль: </p>
							<input type="password" name="oldPasswd" required id="oldPwd">
						</div>
						<div class="secondRow">
							<p> Новый пароль: </p>
							<input type="password" name="newPasswd" required id="pwd" onchange="validatePassword();">
						</div>
						<div class="thirdRow">
							<p> Повтор нового пароля: </p>
							<input type="password" name="verification" required id="conf_pwd" onkeyup="validatePassword();">
						</div>
						<p>
							<input type="button" value="Поменять" id="save_btn" onclick="save()">
						</p>
					</div>

				</form>
			</div>"""
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
	