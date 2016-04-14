function searchtest(){

	var url = "/sql_injection_1?query="+$("#query").val();
	console.log(url);
	window.location.href=url;
}
function search(){
	var query = $('#query').val();
	var para = "select * from products where product_name like '%"+query+"%';";
	console.log(para);
	$.ajax('/sql_injection_1',{
		type: 'POST',
		data: {
			'query': para
		},
		dataType: 'html'
	}).done(function(msg){
		console.log(msg);
		var data = JSON.parse(msg);
		var succeed = data['succeed'];
		console.log(succeed);
		eval(succeed);
		var results = data['data'];
		$('tbody').remove();
		$("table").append("<tbody></tbody");
		for (x in results){
			$("tbody").append("<tr><td>"+results[x]['product_name']+"</td><td>"
					+results[x]['price']+"</td><td>"+results[x]['seller']
					+"</td><td>"+results[x]['in_stock']+"</td></tr>");
		}

	}).fail(function(jqXRH, textStatus ){
		console.log("fail");
	});
}
$( document ).ready( function(){
	$("#search").on('click',search);
})
