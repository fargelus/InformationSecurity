$(document).ready(function(){
	var object = localStorage.getItem("object");
	object = JSON.parse(object);

	var $htmlToBuilt = $(generateHtml());
	var offset = 0;
	for (key in object){
		if (key == "admin")
			offset = 1;
		else
			offset = 3;

		if (offset == 3 && object[key][2] == "Yes")
			alert("На ваш пароль установлено ограничение");
			
		else if (object[key][offset] > 1)
				$htmlToBuilt = $("<p class='changeBtn'>\
										<input type='button' value='Изменить пароль' onclick='change();'>\
										<input type='button' value='Выход' onclick='exit();'>\
								  </p>");

	}

	$("body").append($htmlToBuilt);
});

function generateHtml() {
	return "<div class='main'> \
				<h1> Смена пароля </h1>\
					<form name='admin' action='saveData.py' method='post'>\
						<div class='firstRow'>\
							<p> Старый пароль: </p>\
							<input type='password' name='oldPasswd' required id='oldPwd'> \
						</div>\
						<div class='secondRow'> \
							<p> Новый пароль: </p> \
								<input type='password' name='newPasswd' required id='pwd' onchange='validatePassword();'>\
						</div>\
						<div class='thirdRow'>\
							<p> Повтор нового пароля: </p>\
							<input type='password' name='verification' required id='conf_pwd' onkeyup='validatePassword();'>\
						</div>\
						<p>\
							<input type='button' value='Поменять' id='save_btn' onclick='save();'>\
						</p>\
					</form> \
			</div>";
}

function change() {
	$(".changeBtn").remove();
	$("body").append(generateHtml());
}

function exit() {
	if (confirm("Вы действительно хотите выйти?")) {
			window.location.replace('http://localhost:8000');
    }
}

/* save.js - отправляет пароль 
   на сервер совместно с метаданными */
function save() {
	if (!isOldPasswordCorrect()){	
		alert('Введён неверный пароль подтверждения');
		document.getElementById('oldPwd').value = '';
		document.getElementById('pwd').value = '';
		document.getElementById('conf_pwd').value = '';
		return;
	}

	if (!isPasswordsMatch()){
		document.getElementById('pwd').setCustomValidity('Пароли не совпадают или вы не ввели новый пароль');
		document.getElementById('pwd').value = '';
		document.getElementById('conf_pwd').value = '';
		return;	
	}
	
	var object = localStorage.getItem("object");
	object = JSON.parse(object);

	for (key in object){
		if (!hasLimit()){
			object[key][0] = document.getElementById('pwd').value;
			object[key][2] = "No";
			console.log(key);
		}
		else{
			alert("Введённый пароль не удовлетворяет ограничениям!");
			document.getElementById('oldPwd').value = '';
			document.getElementById('pwd').value = '';
			document.getElementById('conf_pwd').value = '';
			return;
		}
	}

	// отправляем нашу изменённую структуру для записи в сериализованную 
	// бд
	$.ajax({
		type: "POST",
		data: object,
		url: "../cgi-bin/password_change.py",
		datatype: "json",
		traditional: true,
		success: function(response){
			alert('Пароль успешно изменён');
			window.location.replace('http://localhost:8000');
		},
		error: function(response) {
		  	console.log(response.status + ': ' + response.statusText);
		}
	});
}

// правильно ли введён старый пароль
function isOldPasswordCorrect() {
	var answer = true;
	var oldPwd = document.getElementById('oldPwd').value;
	var object = localStorage.getItem("object");
	object = JSON.parse(object);
	for (key in object){
		if (object[key][0] != oldPwd)
			answer = false; 
	}

	return answer;
}

// проверка подтверждения пароля
function isPasswordsMatch() {
	var answer = false;
	var newPwd = document.getElementById('pwd').value;
	var confirmedPwd = document.getElementById('conf_pwd').value;
	if (newPwd == confirmedPwd && newPwd != '')
			answer = true;

	return answer;
}

// проверка пароля на ограничение
function hasLimit() {
	var answer = false;
	var object = localStorage.getItem("object");
	object = JSON.parse(object);
	for (key in object){
		if (object[key][2] == "Yes"){
			var newPwd = document.getElementById('pwd').value;
			var matched = newPwd.match(/^[A-Za-z\/\+\-\*.,\/#!$%\^&\*;:{}=\-_`~()]+$/ig);
			if (matched == null)
				answer = true; 
		}
	}

	return answer;
}

// валидация в режиме реального времени
function validatePassword() {
	var password = document.getElementById("pwd");
  	var confirm_password = document.getElementById("conf_pwd");

  	if(password.value != confirm_password.value) {
    	confirm_password.setCustomValidity("Пароли не совпадают");
  	} 
  	else {
    	confirm_password.setCustomValidity('');
  	}
}