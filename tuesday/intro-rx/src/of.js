import { of } from "rxjs";

const $stream = of(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
$stream.subscribe(
    next => { console.log(`Next ${next}`) }
);