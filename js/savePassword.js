/* save.js - отправляет пароль 
   на сервер совместно с метаданными */
function save() {
	// если пароли не совпадают известить об этом пользователя
	if (!isPasswordsMatch()){
		document.getElementById('pwd').setCustomValidity('Пароли не совпадают');
		return;
	}

	if (isOldPasswordCorrect()){
		var new_password = document.getElementById('pwd');
		var login_val = localStorage.getItem("login"); 
		var addr_val = localStorage.getItem("address");
		if (new_password.value.length != 0){
			if (!is_limit(new_password.value)){
				var data_to_send = {};
				if (addr_val == "admin")
					login_val = login_val.toLowerCase();
				data_to_send['login'] = login_val;
				data_to_send['address'] = addr_val;
				data_to_send['password'] = new_password.value;

				$.ajax({
					type: "POST",
					data: data_to_send,
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
			else
				alert("Введённый пароль не соотвествует ограничениям");
		}
		else
			new_password.setCustomValidity("Вы должны ввести пароль");
	}
	else{
		alert('Введён неверный пароль подтверждения');
		document.getElementById('oldPwd').value = '';
		document.getElementById('pwd').value = '';
		document.getElementById('conf_pwd').value = '';
	}
}

// проверка подтверждения пароля
function isPasswordsMatch() {
	var newPwd = document.getElementById('pwd').value;
	var confirmedPwd = document.getElementById('conf_pwd').value;
	if (newPwd == confirmedPwd)
		return true;
	return false;
}

// проверка старого пароля перед сохранением нового
function isOldPasswordCorrect() {
	var retVal = false;
	var oldPwd = document.getElementById('oldPwd').value;
	var login_val = localStorage.getItem("login");
	var checkOldPassword = new XMLHttpRequest();
	if (login_val.toLowerCase() == "admin")
		checkOldPassword.open('GET', '../admin.json', false);
	else
		checkOldPassword.open('GET', '../users.json', false);
	checkOldPassword.send();

	if (checkOldPassword.status != 200) {
      // обработать ошибку
      alert('Ошибка ' + checkOldPassword.status + ': ' + checkOldPassword.statusText);
    } else {
        // вывести результат
        var data = checkOldPassword.responseText;
        var jsonResponse = JSON.parse(data);

        if (jsonResponse[login_val][0] == oldPwd)
        	retVal = true;
    }

    return retVal;	
}

// проверка на ограничение
function is_limit(password) {
	var answer = false;
	var login = localStorage.getItem("login");
	var address = localStorage.getItem("address");
	var path = '../' + address + '.json';

	var xhr = new XMLHttpRequest();
	xhr.open('GET', path, false);
	xhr.send();

	if (xhr.status != 200) {
      // обработать ошибку
      alert('Ошибка ' + xhr.status + ': ' + xhr.statusText);
    } else {
        // вывести результат
        var data = xhr.responseText;
        var jsonResponse = JSON.parse(data);
    	if (jsonResponse[login][2] == "Yes"){
    		var matched = password.match(/^[A-Za-z\/\+\-\*.,\/#!$%\^&\*;:{}=\-_`~()]+$/ig); 
    		if (matched == null)
    			answer = true;
    	}
    }

	return answer;
}

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