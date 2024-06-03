// Attaching a click event handler to DIV#add_item
$("DIV#add_item").click(function() {
    // Creating a new <li> element
    var newItem = $("<li>Item</li>");
    
    // Appending the new <li> element to UL.my_list
    $("UL.my_list").append(newItem);
});

