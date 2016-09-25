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
        if (jsonResponse["admin"] == pwd)
        	document.securityCheck.submit();
    }
}
