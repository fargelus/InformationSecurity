function add() {
	document.getElementById('add_form').style.display = "block";

	// сброс всех настроек куки 
	document.getElementById('loginData').value = '';
	document.getElementById('passwordData').value = '';
	document.getElementById('block').checked = false;
	document.getElementById('limitation').checked = false;
}

function change() {
	if ($('table td:first-child').text().trim() == ""){
		alert('Таблица пуста');
		return;
	}

	document.getElementById('add_form').style.display = "none";	
	document.getElementById('change_form').style.display = "block";
	document.getElementById('login_select').style.display = "block";

	document.getElementById('login_for_change').value = '';
	document.getElementById('change_block').checked = false;
	document.getElementById('change_limit').checked = false;

	document.getElementById('change_select').style.display = 'none';
}

// переход на div с паролем и свойствами
function go_next() {
	var login_val = document.getElementById('login_for_change').value;
	if (checkInput(login_val)){
			document.getElementById('login_select').style.display = "none";
			document.getElementById('change_select').style.display = "block";

			var rowNumber = getNumberOfRow(login_val);
			var currEncryptedPassword = encryptedPasswords[rowNumber];
			document.getElementById('change_passwd').value = currEncryptedPassword;
			rowNumber++;

			var blockInTable = $('table tr:eq(' + rowNumber + ') td:eq(2)');
			var limitInTable = $('table tr:eq(' + rowNumber + ') td:eq(3)');
			if (blockInTable.text() == "Yes")
				document.getElementById("change_block").checked = true;
			if (limitInTable.text() == "Yes")
				document.getElementById("change_limit").checked = true;
			
	}
	else {
		document.getElementById('login_for_change').setCustomValidity("Введённый логин неверен");
		document.getElementById('login_for_change').value = '';
	}	
}

// найти номер строки в таблице, содержащий данный логин
function getNumberOfRow(login) {
	var count = 0;
	$('table td:first-child').each(function () {
		if ($(this).text() == login){
			return false;
		}
		count++;
	});
	return count;
}

function saveChanges() {
	var login_val = document.getElementById('login_for_change').value;
	var passwd_val = document.getElementById('change_passwd').value;
	var numberLoginInRow = getNumberOfRow(login_val);
	var encryptedValue = encryptedPasswords[numberLoginInRow];
	if (passwd_val != encryptedValue){
		var encryptedChangePassword = CryptoJS.AES.encrypt(passwd_val, 'password');
		encryptedPasswords[numberLoginInRow] = encryptedChangePassword;
	}

	var is_block = 'No';
	var is_limit = 'No';
	if ($('#change_block').prop("checked"))
		is_block = 'Yes';
	if ($('#change_limit').prop(":checked")){
		is_limit = 'Yes';
		console.log('Yes');
	}
	$('table td:first-child').each(function (){
		if ($(this).text() == login_val){
			var new_row = '<tr><td>' + login_val + '</td><td>' + encryptedPasswords[numberLoginInRow] 
			+ '</td><td>' + is_block + '</td><td>' + is_limit + '</td></tr>';
			$(this).parent().replaceWith(new_row); 
		}
	});
	
	document.getElementById('change_select').style.display = "none";
	document.getElementById('change_form').style.display = "none";
}

function del() {
	var row_to_del = $('#login_for_change').val();
	$('table td:first-child').each(function (){
		if ($(this).text() == row_to_del)
			 $(this).closest('tr').remove();
	});
	document.getElementById('change_select').style.display = "none";			
}

// проверка ввода логина 
// на форме изменить
function checkInput(login) {
	var checked = false;
	if (login.length != 0){
		$('table td:first-child').each(function (){
			if ($(this).text() == login)
			 	checked = true;
		});
	}
	
	return checked;
}

var encryptedPasswords = [];

function addUser() {
	var login = document.getElementById('loginData');
	var password = document.getElementById('passwordData');
	if (checkInput(login) && checkInput(password)){
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
		// var number_dupl_item = -1;

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
		{
			var is_block = 'No', is_limit = 'No';
			if ($('#block').is(":checked"))
				is_block = 'Yes';
			if ($('#limitation').is(":checked"))
				is_limit = 'Yes';

        	var encrypt_password = CryptoJS.AES.encrypt(password, 'password');
        	encryptedPasswords.push(encrypt_password);

			$('table').append('<tr><td>' + login + '</td><td>' + encrypt_password + '</td><td>' + is_block + '</td><td>'
				+ is_limit + '</td></tr>');
		}

		document.getElementById('add_form').style.display = "none";
	}
}

function tableToJson() {
	// преобразуем данные из таблицы в json
	// для ajax

	var login_list = [];
	$('table td:nth-child(-n+1)').each(function(){
		login_list.push( $(this).text() );
	});

	var attr_list = [];
	$('table td:nth-child(n+2)').each(function(){
		attr_list.push( $(this).text() );
	});	

	var data = {};
	var password_count = 0;
	for (var i = 0; i < login_list.length; i++) {
		var login = login_list[i];
		var attr = [];
		for (var j = 3 * i; j <= 3 * i + 2; j++) {
			if (j % 3 == 0){
				var password_to_decrypt = encryptedPasswords[password_count];
				var decrypted = CryptoJS.AES.decrypt(password_to_decrypt, 'password').toString(CryptoJS.enc.Utf8);
				console.log(decrypted);
				attr.push(decrypted);
				password_count++;
				// encryptedPasswords.splice(password_count);	 
			}
			else
				attr.push(attr_list[j]);		
		}
		data[login] = attr;
	}
	
	return data;
}

/* добавление данных в таблицу из базы данных */
$(document).ready(function(){
	$.getJSON('../users.json', function(json){
		$.each(json, function(key, value){
        	var tr = $('<tr>');
        	tr.append("<td>" + key + "</td>");
        	for (var i = 0; i < value.length; i++) {

        		// i == 0 - это пароль для каждого логина
        		if (i == 0){
        			var encrypt_password = CryptoJS.AES.encrypt(value[i], 'password');
        			encryptedPasswords.push(encrypt_password);
        			tr.append("<td>" + encrypt_password + "</td>");
        		} 			
        		else
        			tr.append("<td>" + value[i] + "</td>");
        	}

        	tr.append('</tr>');
        	$('table').append(tr);
		});
	});
});

/* сохранить данные в базе */
$(document).ready(function() {
	$("#save_btn").click(function() {
		var data = tableToJson();

		$.ajax({
			type: "POST",
			data: data,
			url: "../cgi-bin/saveUsers.py",
			datatype: "json",
			traditional: true,
			success: function(response){
				alert('Данные успешно сохранены');
			},
			error: function(response){
				console.log(response.status + ': ' + response.text);
			}
		});
	});
});

/* выйти при подтверждении */
$(document).ready(function(){
	$("#exit_btn").click(function() {
		if (confirm("Вы действительно хотите выйти?")) {
			window.location.replace('http://localhost:8000');
    	}
    });
});
