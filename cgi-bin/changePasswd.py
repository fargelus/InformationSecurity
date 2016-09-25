#!/usr/bin/env python3

import cgi

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработчик формы</title>
        </head>
        <body>""")

print("""<div class="main">
				<h1> Смена пароля </h1>
				<form name="admin" class="adminInput" method="post" action="somescript">
					<div class="firstRow">
						<p> Новый пароль: </p>
						<input type="text" name="newPasswd">
					</div>
					<div class="secondRow">
						<p> Подтверждение: </p>
						<input type="text" name="verification">
					</div>
					<p>
						<input type="submit" value="Ок">
						<input type="submit" value="Отмена">
					</p>
				</form>
			</div>""")

print("""</body>
        </html>""")
