#!/usr/bin/node

function fetch_data() {
    const uri = "https://hellosalut.stefanbohacek.dev/?lang=" + $("input#language_code").val();

    $.ajax({
        url: uri,
        type: "GET",
        dataType: "json"
    })
    .done(function(json) {
        $("div#hello").text(json.hello);
    });
}

$(function() {
    $("input#language_code").on("keypress", fetch_data);
    $("input#btn_translate").on("click", fetch_data)
});
