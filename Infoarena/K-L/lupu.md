# The Big Bad Wolf and the Sheep

The big bad wolf wants to play with his little fluffy sheep friends. However, shepherd Eduard decides not to let the wolf play with all of his sheep and allows him to choose only a few. The wolf is fixed at a point in the meadow, while the sheep are at different distances from him. The selection of sheep is done in several stages. The big bad wolf chooses a sheep located at a distance of up to $X$, and at that moment all the other sheep will move away (at the request of shepherd Eduard) by distance $L$ from the wolf. For each sheep, the amount of wool it has is known, and the wolf wants the sum of the wool amounts for the chosen sheep to be as large as possible (so they are as fluffy as possible).

## Task

Help the big bad wolf to choose the sheep so that he gets as much wool as possible.

## Input data

The first line of the input file `lupu.in` contains three integers $N$, $X$ and $L$ representing the number of sheep, the maximum distance from which the wolf can choose sheep, and the distance by which the sheep move away from the wolf after each selection. The following $N$ lines contain two integers $D$ and $A$ representing the initial distance and the amount of wool of each sheep.

## Output data

The file `lupu.out` will contain a single integer $S$, representing the maximum amount of wool the wolf can gather from the chosen sheep.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

For 40% of the tests $N \leq 1\ 000$

All numbers in the input file are integers in the range $[0, 2^{31}-1]$

## Example

`lupu.in`
```
10 6 2
1 13
4 14
4 3
6 7
0 7
5 16
3 16
4 10
4 18
3 16
```

`lupu.out`
```
54
```