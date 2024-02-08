#!/usr/bin/node

$(function () {
    $( "input#btn_translate" ).on("click", function () {
	const uri = "https://hellosalut.stefanbohacek.dev/?lang=" + $("input#language_code" ).val();

	$.ajax({
	    url: uri,
	    type: "GET",
	    datatype: "json"
	})
	    .done(function (json) {
		$("div#hello").text(json.hello);
	    });
    });
});
