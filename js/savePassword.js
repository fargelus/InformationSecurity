function save() {
	/* save.js - отправляет пароль 
	на сервер совместно с метаданными */
	/*console.log(localStorage.getItem("login"));
	console.log(localStorage.getItem("address"));*/

	var new_password = document.getElementById('pwd');
	if (new_password.value.length != 0){
		if (!is_limit(new_password.value)){
			var login_val = localStorage.getItem("login");
			var addr_val = localStorage.getItem("address");
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
