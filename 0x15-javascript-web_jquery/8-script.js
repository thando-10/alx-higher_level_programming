// Fetching data from the URL and listing movie titles in UL#list_movies
$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    // Looping through the results to extract movie titles
    $.each(data.results, function(index, movie) {
        // Creating a new <li> element for each movie title and appending it to UL#list_movies
        $("UL#list_movies").append("<li>" + movie.title + "</li>");
    });
});

