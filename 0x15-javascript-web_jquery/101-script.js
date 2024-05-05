// JavaScript script to dynamically manipulate a list
$(document).ready(function() {
	$("DIV#add_item").click(function() {
		var newItem = $("<li>Item</li>");
		$("UL.my_list").append(newItem);
	});
	$("DIV#remove_item").click(function() {
		$("UL.my_list li:last-child").remove();
	});
	$("DIV#clear_list").click(function() {
		$("UL.my_list").empty();
	});
});
