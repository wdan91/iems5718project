function submitKey() {
    $.ajax('/dom_injection',{
	    type: 'POST',
	    data: {
	    },
	    dataType: 'html'
    }).done(function(msg){
	    $('<p style=\'color:red\'>Congratulations!!!</p>').appendTo('#lessonContent'); 
	    console.log("congratulations!!");
    }).fail(function( jqXRH, textStatus ){
	    console.log("fail");
    });
}
$( document ).ready(function(){
	$("#warning").hide();
    /*function callback() {
        if (req.readyState == 4) {
            if (req.status == 200) {
                var message = req.responseText;
		console.log(message);
                var messageDiv = document.getElementById('MessageDiv');
                try {
                    eval(message);
                    messageDiv.innerHTML = 'Correct licence Key.'
                } catch (err) {
                    messageDiv.innerHTML = 'Wrong license key.'
                }
            }
        }
    }
    */
$('#key').keyup(function validate() {
    //var url = url + "&from=ajax&key=' + encodeURIComponent(keyField.value)";
    //var url = url + "?from=ajax&key=" + $('#key').val();
    var url = '/dom_injection/check' + "?from=ajax&key=" + $('#key').val();
    var key = $('#key').val();
    /*if (typeof XMLHttpRequest != 'undefined') {
        req = new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        req = new ActiveXObject('Microsoft.XMLHTTP');
    }
    req.open('GET', url, true);
    req.onreadystatechange = callback;
    req.send(null);
    */
    $.ajax('/dom_injection/check',{
	    type: 'GET',
	    data: {
		    'from':'ajax',
		    'key':key
	    },
	    dataType: 'html'
    }).done(function(msg){
	    console.log(msg);
	    eval(msg);
    }).fail(function( jqXRH, textStatus ){
	    console.log(jqXRH.responseText);
	    eval(jqXRH.responseText);
	    //$("#SUBMIT").attr("disabled",true);
	    
    });
});
$('#SUBMIT').on('click',submitKey);

})
