


function login() {
    console.log("login");
    $.ajax('/insecure_communication',{
	    type: 'POST',
	    data: {
		 'username':$('#inputUserName').val(),
		 'password':$('#inputPassword').val()
	    },
	    dataType: 'html'
    }).done(function(msg){
	    console.log(msg);
	    eval(msg);
	    $("#submit_result").on('click',submitKey);

	    console.log("congratulations!!");
    }).fail(function( jqXRH, textStatus ){
	    console.log("fail");
    });
}

function submitKey() {
    console.log("submit");
    $.ajax('/insecure_communication/check',{
	    type: 'POST',
	    data: {
		 'password':$('#result').val(),
	    },
	    dataType: 'html'
    }).done(function(msg){
	    $('<p style=\'color:red\'>Congratulations!!!</p>').appendTo('#lessonContent'); 
	    console.log("congratulations!!");
    }).fail(function( jqXRH, textStatus ){
	    console.log("fail");
    });
}
$( document ).ready( function(){
	$("#login").on('click',login);
})
