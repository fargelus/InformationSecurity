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
			$('table').append('<tr><td>' + login + '</td><td>' + password + '</td><td>No</td><td>No</td></tr>');
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
	for (var i = 0; i < login_list.length; i++) {
		var login = login_list[i];
		var attr = [];
		for (var j = 3 * i; j <= 3 * i + 2; j++) {
			attr.push(attr_list[j]);		
		}
		data[login] = attr;
	}
	
	return data;
}

$(document).ready(function(){
	$.getJSON('../users.json', function(json){
		$.each(json, function(key, value){
        	var tr = $('<tr>');
        	tr.append("<td>" + key + "</td>");
        	for (var i = 0; i < value.length; i++) {
        		tr.append("<td>" + value[i] + "</td>");
        	}
        	tr.append('</tr>');
        	$('table').append(tr);
		});
	});
});

$(document).ready(function() {
	$("#add_btn").click(function() {
		var data = tableToJson();

		$.ajax({
			type: "post",
			data: JSON.stringify(data),
			url: "../cgi-bin/saveUsers.py",
			datatype: "json",
			async: false,
			success: function(response){
				console.log(response.message);
	        	console.log(response.keys);
	        	console.log(response.data);
			},
			error: function(response){
				console.log(response.message);
	        	console.log(response.keys);
	        	console.log(response.data);
			}
		});
	});
});

