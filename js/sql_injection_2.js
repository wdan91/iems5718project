function searchtest(){
	var url = "/sql_injection_1?query="+$("#query").val();
	console.log(url);
	window.location.href=url;
}
function search(){
	var query = $('#query').val();
	var para = "select * from reviews where content like '%"+query+"%';";
	console.log(para);
	$.ajax('/sql_injection_2',{
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
		$('#review_div').empty();
		for (x in results){
			$("#review_div").append("<h4>"+results[x]['review_title']+"</h4><h5>"
					+results[x]['name']+"</h5><p>"+results[x]['content']
					+"</p><p>&nbsp</p>");
		}

	}).fail(function(jqXRH, textStatus ){
		console.log("fail");
	});
}
function submit_result(){
	$.ajax('/sql_injection_2/check',{
		type: 'POST',
		data: {
			'result': $('#result').val()
		},
		dataType: 'html'
	}).done(function(msg){
		eval(msg);
	}).fail(function(jqXRH, textStatus ){
		console.log("fail");
	});
}
$( document ).ready( function(){
	$("#search").on('click',search);
	$("#submit_result").on('click',submit_result);
})
