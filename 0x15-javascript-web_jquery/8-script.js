#!/usr/bin/node

$.get( "https://swapi-api.alx-tools.com/api/films/?format=json", function ( data ) {
    const data_list = data.results.map( x => x.title);
    data_list.map(title => {
	const tag = document.createElement("li");
	tag.textContent = title;
	$( "ul#list_movies" ).append(tag);
    });
});
