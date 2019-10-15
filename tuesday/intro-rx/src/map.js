import { of } from "rxjs";
import { map } from "rxjs/operators";

const $source = of(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

const $stream = $source.pipe(
    map(it => it * 2)
);

$stream.subscribe(
    next => { console.log(`Next ${next}`) }
);