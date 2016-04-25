$( document ).ready( function(){
	$(function () {
		  $('[data-toggle="popover"]').popover()
	});
	$("#start_lesson").click(function () {
		 $(".guide_section").hide();
		 $(".lesson_section").show();
	});

	function show_modal () {
		$(".modal").modal('show'); 
	};

	if($("#welcome_hidden").val()=="welcome"){
		console.log("dsafsdfafa");
		$(".lesson_section").show();
	};
		
	

	// show_modal();
	


})
