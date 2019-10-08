import {RxHR} from "@akanass/rx-http-request";
import { map, tap, delay } from "rxjs/operators";
import { zip } from "rxjs";

const $squirtle = RxHR.get('https://pokeapi.co/api/v2/pokemon/7/', { json: true }).pipe(
    map(res => res.body.name),
    tap(() => console.log('squirtle emitiu'))
);

const $bulba = RxHR.get('https://pokeapi.co/api/v2/pokemon/1/', { json: true }).pipe(
    delay(2000),
    map(res => res.body.name),
    tap(() => console.log('bulba emitiu'))
);

zip(
    $bulba,
    $squirtle,
).subscribe(
    (res) => console.log("Chegou o poke", res),
    err => { console.error(`Falhou`) },
    () => console.log("Terminou geral")
);