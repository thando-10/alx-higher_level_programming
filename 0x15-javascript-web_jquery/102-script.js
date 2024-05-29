<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Translate Hello</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            // Function to fetch and print the translation
            function fetchTranslation() {
                var languageCode = $("INPUT#language_code").val();
                $.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: languageCode }, function(data) {
                    $("DIV#hello").text(data.hello);
                });
            }

            // Fetch translation when the button is clicked
            $("INPUT#btn_translate").click(function() {
                fetchTranslation();
            });
        });
    </script>
</head>
<body>
    <input type="text" id="language_code" placeholder="Language Code">
    <input type="button" id="btn_translate" value="Translate">
    <div id="hello"></div>
</body>
</html>

