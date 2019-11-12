const { fromEvent, from } = rxjs;
const { tap, debounceTime, filter, map, distinctUntilChanged, subscribe, switchMap } = rxjs.operators;

const $input = document.querySelector('#textInput');
const $results = $('#results');

fromEvent($input, 'keyup').pipe(
    map(e => e.target.value),
    filter(text => text.length > 2),
    debounceTime(500),
    distinctUntilChanged(),
    switchMap(query => searchCountries(query)),
).subscribe(
    countries => { displayCountries(countries) },
    error => $results.empty().append($('<li>')).text('Error:' + error)
);

function queryMatches(countries, query) {
  const lowerQuery = query.toLowerCase();
  return countries.filter(country => {
    const lowerName = country.nome.toLowerCase();
    return lowerName.indexOf(lowerQuery) != -1;
  });
}

function searchCountries (query) {
  return from($.getJSON( "paises.json")).pipe(
    map(countries => queryMatches(countries, query))
  );
}

function displayCountries(countries) {
  const countryNames = countries.map(country => country.nome); 
  $results.empty().append(countryNames.map(v => $('<li>').text(v)))
}