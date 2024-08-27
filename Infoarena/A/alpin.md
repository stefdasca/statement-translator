# Alpine

A mountain climber is in a mountainous region encoded as a square matrix of size $N$, where each element of the matrix represents the altitude of the corresponding portion of land. The climber can start their route from any point of the region (i.e., from any element of the matrix) and can end this route anywhere. They can move in any of the directions {N, S, E, W} provided that they do not leave the region. Additionally, they must continuously ascend, meaning that the altitude of the current region must be strictly less than the altitude of the next region on the route.

## Task

Determine the longest route the climber can take.

## Input data

The input file `alpin.in` will contain on its first line the number $N$, the size of the region. The next $N$ lines contain $N$ positive natural numbers each, separated by exactly one space, describing the matrix encoding of the region.

## Output data

The output file `alpin.out` will contain on its first line $LMAX$, the maximum length of the traversed route. It will be followed by $LMAX$ lines, describing the route by its cells, in order, from the first to the last, inclusive.

## Constraints and clarifications

$1 \leq N \leq 1024$

The maximum altitude does not exceed $16\ 384$

If there are multiple solutions of maximum length, any of them can be displayed.

If you correctly determine only the maximum length, you will receive 50% of the points for the respective test.

## Example

`alpin.in`
```
6
29 10 8 9 8 10
22 11 7 3 7 20
17 15 3 14 45 30
19 5 2 41 19 17
23 8 90 39 20 18
27 30 32 35 70 19
```

`alpin.out`
```
16
4 3
3 3
2 3
1 3
1 2
1 1
2 1
3 1
4 1
5 1
6 1
6 2
6 3
6 4
5 4
4 4
```