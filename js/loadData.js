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
    var input_login = document.getElementById("input_for_login").value;
    localStorage.setItem("login", input_login);

    var xhr = new XMLHttpRequest();
    if (input_login.toLowerCase() == "admin")
    {
        localStorage.setItem("address", "admin");
        input_login = input_login.toLowerCase();
        console.log(input_login);
        xhr.open('GET', '../admin.json', false);        
    }
    else
    {
        localStorage.setItem("address", "users");
        xhr.open('GET', '../users.json', false);
    }
    xhr.send();

    if (xhr.status != 200) {
      // обработать ошибку
      alert('Ошибка ' + xhr.status + ': ' + xhr.statusText);
    } else {
        // вывести результат
        var data = xhr.responseText;
        var jsonResponse = JSON.parse(data);
        
        // переделать здесь ошибка
        var pwd = document.securityCheck.password.value;
        try{
            if (jsonResponse[input_login][0] == pwd)
            {
                if (jsonResponse[input_login][1] == "Yes")
                  alert("Данный логин заблокирован администратором");
                else
                  document.securityCheck.submit();
            }
            else
                alert("Bad");  
        }
        catch(err){
          alert("Такого логина нет в базе данных");
        }
    }
}
