// fetch and list movie titles in UL#list_movies
$(document).ready(function() {
	$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
		var movies = data.results;
		var list = $("ul#list_movies");
		$.each(movies, function(index, movie) {
			list.append("<li>" + movie.title + "</li>");
		});
	});
});
