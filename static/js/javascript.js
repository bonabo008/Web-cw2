// Change galley image function
function changeimage(image){
	
	// fades out main image, chages the image, then fades in.
	$("#focusimage").stop().fadeOut(function(){
		document.getElementById("focusimage").src = image;
		fadeIn();
	});
	function fadeIn() {
		$("#focusimage").stop().fadeIn("fast");
	}
}

$(function() {
	$( "#dateStart" ).datepicker({ minDate: new Date() });
	$( "#dateEnd" ).datepicker({ minDate: new Date() });
});