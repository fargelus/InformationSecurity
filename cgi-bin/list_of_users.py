#!/usr/bin/env python3

import cgi

form = cgi.FieldStorage()
login = form.getfirst("login")
password = form.getfirst("password")
conf_pwd = form.getfirst("confirm_pwd")

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
