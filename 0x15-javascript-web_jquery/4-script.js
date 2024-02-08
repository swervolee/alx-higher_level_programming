#!/usr/bin/node

$( "div#toggle_header" ).on( "click", function () {
    $( "header" ).toggleClass( "red" );
    $( "header" ).toggleClass( "green" );
});
