// Fetching data from the URL and updating the character name in DIV#character
$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
    // Updating the character name in DIV#character
    $("DIV#character").text(data.name);
});

