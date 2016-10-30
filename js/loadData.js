/*
  loadData.js -- клиентский скрипт,
  загружает данные из бд и позволяет войти в систему
*/

var countError = 0;

function isEmpty(obj) {
    for(var prop in obj) {
        if(obj.hasOwnProperty(prop))
            return false;
    }

    return true;
}

function loadData() {
    var inputLogin = document.getElementById("input_for_login").value;
    if (inputLogin.toLowerCase() == "admin")
      inputLogin = inputLogin.toLowerCase();
    
    var password = document.getElementById("pwd").value;
    var objectToSend = {};
    objectToSend[inputLogin] = password;
    $.ajax({
      type: "POST",
      data: objectToSend,
      url: "../cgi-bin/checkInputInfo.py",
      datatype: "json",
      traditional: true,

      success: function(response){
        alert(JSON.stringify(response));
        if (!isEmpty(response)){
          if (password == response[inputLogin][0]){
            if (inputLogin.toLowerCase() != "admin" && response[inputLogin][1] == "Yes")
                alert("Данный логин заблокирован администратором");
            else{
              localStorage.setItem("object", JSON.stringify(response));
              document.securityCheck.submit();
            }
          }
          else{
              if (countError == 3){
                window.open('', '_self', ''); 
                window.close();
              }
              else{
                alert("Пароль введён неправильно");
                countError = countError + 1;
                console.log(countError);
              }
          }
        }
        else
          alert("Такого логина нет в базе данных");
      },

      error: function(response){
        alert("It's bad for ya");
      }
    });
}

    // setMetaObject(inputLogin);
    
    /*var address = "";
    if (inputLogin.toLowerCase() == "admin"){
		address = "../admin.json";
		inputLogin = inputLogin.toLowerCase();
		localStorage.setItem("address", "admin");
	}
	else{
		address = "../users.json";
		localStorage.setItem("address", "users");	
	}
	localStorage.setItem("login", inputLogin);    

    var xhr = new XMLHttpRequest();
    xhr.open('GET', address, false);
    xhr.send();

    if (xhr.status != 200) {
      // обработать ошибку
      alert('Ошибка ' + xhr.status + ': ' + xhr.statusText);
    } 
    else {
        // вывести результат
        var data = xhr.responseText;
        var jsonResponse = JSON.parse(data);
        
        var pwd = document.securityCheck.password.value;
        try{
            if (jsonResponse[inputLogin][0] == pwd) {
            	if (jsonResponse[inputLogin][2] == "Yes")
            		localStorage.setItem("isLimit", "true");
            	
                if (jsonResponse[inputLogin][1] == "Yes")
                  alert("Данный логин заблокирован администратором");
                else
                  document.securityCheck.submit();
            }
            else {
                if (countError == 3){
                  window.open('', '_self', ''); 
                  window.close();
                }
                else{
                  alert("Пароль введён неправильно");
                  countError = countError + 1;
                  console.log(countError);
                }
            }
        }
        catch(err){
          alert("Такого логина нет в базе данных");
        }
    }*/

/* метаобъект - информация, хранящая информацию о кол-ве входов
   каждого пользователя в систему 
function setMetaObject(login) {
	var meta = localStorage.getItem("metaobject");
    meta = JSON.parse(meta);

    if (meta == null){
    	meta = {};
    	meta[login] = 0;
    }
    else{
    	if (login in meta){
    		meta[login]++;
    	}
    	else
    		meta[login] = 0;
    }

    localStorage.setItem("metaobject", JSON.stringify(meta));
} */