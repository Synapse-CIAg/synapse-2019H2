import { of } from "rxjs";
import { filter } from "rxjs/operators";

const $source = of(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

const $stream = $source.pipe(
    filter(it => it % 2 === 0)
);

$stream.subscribe(
    next => { console.log(`Next ${next}`) }
);