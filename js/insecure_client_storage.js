function updateTotals(){
    $('#tot1').val($('#prc1').val()*$('#qty1').val());
    $('#tot2').val($('#prc2').val()*$('#qty2').val());
    $('#SUBTOT').val(parseFloat($('#tot1').val())+parseFloat($('#tot2').val()));
    $('#GRANDTOT').val(parseFloat($('#tot1').val())+parseFloat($('#tot2').val()));
}
 var coupons = ["nvojubmq",
 "emph",
 "sfwmjt",
 "faopsc",
 "fopttfsq",
 "pxuttfsq"];



function decrypt(code){
	code = code.toUpperCase();
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	caesar = '';
	for (i = code.length ;i >= 0;i--){			
		for (j = 0;j<alpha.length;j++){		
			if(code.charAt(i) == alpha.charAt(j)){
				caesar = caesar + alpha.charAt((j+(alpha.length-1))%alpha.length);
			}
		}	
	}
	return caesar;
}


function isValidCoupon(coupon) {
     coupon = coupon.toUpperCase();
     for(var i=0; i<coupons.length; i++) {
	     decrypted = decrypt(coupons[i]);
	     if(coupon == decrypted){
		     $("#GRANDTOT").val(parseFloat($("#SUBTOT").val())*0.8);
		     return true;
	     }
     }
     return false;     
}

function submitKey() {
    console.log("submit");
    if (isValidCoupon($("#codeInput").val())){
	    console.log("correct");
    $.ajax('/insecure_client_storage',{
	    type: 'POST',
	    data: {
		 'subtot':$('#SUBTOT').val(),
		 'grandtot':$('#GRANDTOT').val()
	    },
	    dataType: 'html'
    }).done(function(msg){
	    $('<p style=\'color:red\'>Congratulations!!!</p>').appendTo('#lessonContent'); 
	    console.log("congratulations!!");
    }).fail(function( jqXRH, textStatus ){
	    console.log("fail");
    });
    }
}
$( document ).ready( function(){
	$("#submitBtn").on('click',submitKey);
})
