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
