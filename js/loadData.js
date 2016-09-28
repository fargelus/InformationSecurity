/*
  loadData.js -- клиентский скрипт,
  проверяет пароли на соотвествие друг с другом,
  загружает данные из бд и позволяет войти в систему
*/

function validatePassword() {
		var password = document.getElementById("pwd");
  		var confirm_password = document.getElementById("conf_pwd");

  		if(password.value != confirm_password.value) {
    		confirm_password.setCustomValidity("Пароли не совпадают");
  		} 
  		else 
  		{
    		confirm_password.setCustomValidity('');
  		}
}


function loadData() {
	  var xhr = new XMLHttpRequest();
    xhr.open('GET', '../db.json', false);
    xhr.send();

    if (xhr.status != 200) {
      // обработать ошибку
      alert('Ошибка ' + xhr.status + ': ' + xhr.statusText);
    } else {
        // вывести результат
        var data = xhr.responseText;
        var jsonResponse = JSON.parse(data);
        var pwd = document.securityCheck.password.value;
        var pwd = pwd.toLowerCase();
        if (jsonResponse["admin"][0] == pwd)
        	document.securityCheck.submit();
    }
}
