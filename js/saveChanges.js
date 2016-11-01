$(window).bind("beforeunload", function(){
	var emptyRequest = {};
    $.ajax({
      type: "POST",
      data: emptyRequest,
      url: "../cgi-bin/dump.py",
      datatype: "json",
      traditional: true,
      success: function(response){
      	window.open('', '_self', ''); 
        window.close();
      },
      error: function(response){
      	alert("Что-то пошло не так");
      }
  });
});
