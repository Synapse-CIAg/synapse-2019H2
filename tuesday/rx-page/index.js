const { fromEvent, from, combineLatest } = rxjs;
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

const $name = document.querySelector('#nameInput');
const $password = document.querySelector('#passwordInput');

function getValidEvents(input, predicate) {
  return fromEvent(input, 'keyup').pipe(
    map(e => e.target.value),
    map(text => predicate(text)),
  );
}

const $validPassword = getValidEvents($password, text => text.length > 2)
const $validName = getValidEvents($name, text => text.length > 2 && text.indexOf('@') != -1)

combineLatest($validPassword, $validName).pipe(
  map(states => states.every(state => state === true)),
).subscribe(
  (state) => { changeButton(state); },
);

function changeButton(state) {
  document.getElementById('sendButton').disabled = !state
}