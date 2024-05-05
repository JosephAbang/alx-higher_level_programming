// update text of <header> element when DIV#update_header is clicked
$(document).ready(function() {
	 $("DIV#update_header").click(function() {
		 var header = $("header");
		 header.text("New Header!!!");
	 });
});
