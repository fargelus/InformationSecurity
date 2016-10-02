$(document).ready(function() {
	$("#save_btn").click(function() {
		var new_password = $("#pwd").val();
		var data_to_send = {}
		data_to_send['password'] = new_password
		$.ajax({
			type: "post",
			data: JSON.stringify(data_to_send),
			url: "../cgi-bin/password_change.py",
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

