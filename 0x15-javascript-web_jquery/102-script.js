$(document).ready(function() {
	$("INPUT#btn_translate").click(function() {
		var languageCode = $("INPUT#language_code").val();
		$.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: languageCode }, function(data) {
			var helloTranslation = data.hello;
			$("DIV#hello").text(helloTranslation);
		});
	});
});
