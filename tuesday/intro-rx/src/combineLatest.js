import { interval, combineLatest } from "rxjs";
import { scan, filter, tap } from "rxjs/operators";

let $input1 = interval(100).pipe(
    scan((acc, v) => acc + "b" + v, "a"),
    filter(it => it.length > 10),
    tap(it => console.log("Input 1 emitiu ", it)),
);

let $input2 = interval(100).pipe(
    scan((acc, v) => acc + "t" + v, "y"),
    filter(it => it.length > 20),
    tap(it => console.log("Input 2 emitiu ", it)),
);

let $combined = combineLatest(
    $input1,
    $input2,
);

$combined.subscribe(
    next => { console.log("Downstream recebeu ", next); },
    err => { console.error(err) },
    () => { console.log("Terminei!") }
);