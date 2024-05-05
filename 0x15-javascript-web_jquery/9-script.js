// fetch and display translation of "hello" in DIV#hello
$(document).ready(function() {
	$.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
		var helloTranslation = data.hello;
		$("DIV#hello").text(helloTranslation);
	});
});
