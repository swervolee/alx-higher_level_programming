#!/usr/bin/node

$(function () {
    $( "div#add_item" ).on("click", () => {
        const item = document.createElement("li");
        item.textContent = "Item";
        $( "ul.my_list" ).append( item );
    });

    $( "div#remove_item" ).on("click", () => {
        $( "li" ).last().remove();
    });

    $( "div#clear_list" ).on("click", () => {
        $( "li" ).remove();
    });
});
