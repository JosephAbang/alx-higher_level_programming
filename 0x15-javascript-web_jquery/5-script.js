// add <li> element to UL.my_list when DIV#add_item is clicked
$(document).ready(function() {
	$("DIV#add_item").click(function() {
		var newItem = $("<li></li>").text("Item");
		$("UL.my_list").append(newItem);
	});
});
