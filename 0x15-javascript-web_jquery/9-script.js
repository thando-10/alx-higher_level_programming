// Importing jQuery script from a CDN
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

// Script to fetch translation and display it in DIV#hello
<script>
    $(document).ready(function() {
        // Fetching data from the URL
        $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
            // Updating the content of DIV#hello with the fetched translation
            $("DIV#hello").text(data.hello);
        });
    });
</script>

