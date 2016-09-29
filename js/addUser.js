function checkInput() {
	var login = document.getElementById('loginData');
	var checked = true;
	if (login.value.length == 0){
		login.setCustomValidity("Поле пусто");
		checked = false;
	}

	return checked;
}

function addUser() {
	if (checkInput()){
		var login = $('#loginData').val();
		var password = $('#passwordData').val();
		var login_pwd = login + ': ' + password + '\n';
		var lines = $('textarea').val().split('\n');
		var is_duplicate = false;

		var login_to_add = login_pwd.split(':')[0];

		// добавляем только уникальные значения
		for(var i = 0; i < lines.length; i++){
			if ($.trim(login_pwd) == lines[i]){
				is_duplicate = true;
				break;
			}

			// меняем пароль, доделать
			if (lines[i].split(':')[0] == login_to_add)
			{
				alert(login_pwd);
				$('textarea').replace(lines[i], login_pwd);	
			}
		}
		
		// добавляем в текстовый блок
		if (!is_duplicate){
			text = $('textarea');
			text.val(text.val() + login_pwd);
		}
	}
}