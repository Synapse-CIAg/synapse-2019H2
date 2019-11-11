const { fromEvent } = rxjs;
const { tap, debounceTime, filter, map, distinctUntilChanged, subscribe, switchMap } = rxjs.operators;

function searchCountries () {
    return $.getJSON( "paises.json")
    // return $.ajax({
    //     url: '',
    //     dataType: 'json',
    //     data: {
    //         action: 'search',
    //         format: 'json',
    //         search: term
    //     }
    // }).promise();
}
const $input = document.querySelector('#textInput');
const $results = $('#results');

fromEvent($input, 'keyup').pipe(
    map(e => e.target.value),
    filter(text => text.length > 2),
    debounceTime(500),
    distinctUntilChanged(),
    switchMap(searchCountries),
    tap(a => console.log('after switch', a))
).subscribe(
    next => { console.log(next) },
    // ([,data]) => $results.empty().append(data.map(v => $('<li>').text(v))),
    error => $results.empty().append($('<li>')).text('Error:' + error)
    
    
);

$("button").click(function(){
    $.getJSON("paises.json", function(result){
      $.each(result, function(i, field){
        $("p").append(field.nome + " ");
      });
    });
  });