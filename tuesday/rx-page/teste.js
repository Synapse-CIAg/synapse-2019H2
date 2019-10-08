import { fromEvent } from 'rxjs';
import { debounceTime, filter, map, distinctUntilChanged, subscribe } from 'rxjs/operators';



function searchCountries (term) {
    return $.ajax({
        url: '',
        dataType: 'json',
        data: {
            action: 'search',
            format: 'json',
            search: term
        }
    }).promise();
}
const $input = document.querySelector('#textInput');
const $results = $('#results');

fromEvent($input, 'keyup').pipe(
    map(e => e.target.value),
    filter(text => text.lenght > 2),
    debounceTime(500),
    distinctUntilChanged(),
    // switchMap(search),
).subscribe(
    next => { console.log(next) },
    // ([,data]) => $results.empty().append(data.map(v => $('<li>').text(v))),
    error => $results.empty().append($('<li>')).text('Error:' + error)
    
    
);