<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Header Color</title>
    <script>
        // Wait for the DOM content to load before running the script
        document.addEventListener("DOMContentLoaded", function() {
            // Selecting the <header> element
            var headerElement = document.querySelector("header");

            // Updating the text color to red
            headerElement.style.color = "#FF0000";
        });
    </script>
</head>
<body>
    <header>This is a header</header>
</body>
</html>

