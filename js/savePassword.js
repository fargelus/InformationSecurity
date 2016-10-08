function save(log) {
	/* save.js - отправляет пароль 
	на сервер совместно с метаданными */
	alert('Ok');

	/*var new_password = document.getElementById('pwd');
	if (new_password.value.length != 0){
		var data_to_send = {};
		if (addr.name == "admin")
			log.name = log.name.toLowerCase();
		data_to_send['login'] = log.name;
		data_to_send['address'] = addr.name;
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
	/*else
		new_password.setCustomValidity("Вы должны ввести пароль");*/
}


