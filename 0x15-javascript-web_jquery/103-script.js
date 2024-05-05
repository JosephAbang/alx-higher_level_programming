// JavaScript script to fetch and display the translation of "Hello" 
// based on the language code entered by the user\
$(document).ready(function() {
	$("INPUT#btn_translate").click(fetchTranslation);
	$("INPUT#language_code").keypress(function(event) {
		if (event.keyCode === 13) {
			fetchTranslation();
		}
	});

	function fetchTranslation() {
		var languageCode = $("INPUT#language_code").val();
		$.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: languageCode }, function(data) {
			var helloTranslation = data.hello;
			$("DIV#hello").text(helloTranslation);
		});
	}
});
