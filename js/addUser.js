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
		var login_pwd = login + password;
		var items = [];

		$('table td:nth-child(-n+2)').each(function() {
			items.push( $(this).text() );
		});

		// проверяем на повторяющийся логин
		var is_duplicate = false;

		var table_login_pwd = '';
		var count = -1;
		for (var i = 0; i < items.length; i++) {
			table_login_pwd = table_login_pwd + items[i];
			count = count + 1;

			if (count == 1)
			{
				if (login_pwd == $.trim(table_login_pwd)){	
					is_duplicate = true;
					break;
				}
				table_login_pwd = '';
				count = -1;
			}
		}

		if (!is_duplicate)
			$('table').append('<tr><td>' + login + '</td><td>' + password + '</td><td>Нет</td><td>Нет</td></tr>');
	}
}