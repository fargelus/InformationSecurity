function save(log, addr) {
	console.log(addr.name);
	console.log(log.name);
}


/*$(document).ready(function() {
	$("#save_btn").click(function() {
		var new_password = $("#pwd").val();
		var data_to_send = {};
		data_to_send['password'] = new_password;
		$.ajax({
			type: "POST",
			data: data_to_send,
			url: "../cgi-bin/password_change.py",
			datatype: "json",
			traditional: true,
			success: function(response){
	        	alert('Пароль успешно изменён');
	        	// window.location.replace('http://localhost:8000');
			},
			error: function(response) {
  					console.log(response.status + ': ' + response.statusText);
				}
		});
	});
});*/

