<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List Manipulation</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            // Add item to the list
            $("DIV#add_item").click(function() {
                $("UL.my_list").append("<li>Item</li>");
            });

            // Remove last item from the list
            $("DIV#remove_item").click(function() {
                $("UL.my_list li:last-child").remove();
            });

            // Clear the list
            $("DIV#clear_list").click(function() {
                $("UL.my_list").empty();
            });
        });
    </script>
</head>
<body>
    <div id="add_item">Add Item</div>
    <div id="remove_item">Remove Last Item</div>
    <div id="clear_list">Clear List</div>
    <ul class="my_list">
        <!-- List items will be added dynamically here -->
    </ul>
</body>
</html>

