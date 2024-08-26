## Task

Felix, rejected by the black cat to go to the ChatNoir club with him, decided to take revenge. The black cat is in a rectangular room of size $N \cdot M$. She is positioned at the cell in row $X$ column $Y$ and wants to exit the room, being able to move only left, right, up, or down. Felix, with every step the black cat takes, places a wall on one side of a cell on the edge of the room. The black cat can exit through any side of an edge cell in the room that has no wall. Knowing that the black cat moves intelligently based on where Felix places walls and Felix also places walls intelligently based on how the black cat moves, we need to determine whether the black cat will be able to exit the room or not, and respond with "DA" (YES) or "NU" (NO).

## Input data

The input file `chatnoir.in` will contain on the first line a natural number $T$ representing the number of tests, and on the following $T$ lines, $4$ natural numbers $N$, $M$, $X$, $Y$ as described in the statement.

## Output data

The output file `chatnoir.out` will contain $T$ lines. Line $i$ will contain the answer for test $i$.

## Constraints and clarifications

2 $\leq$ $N$, $M$ $\leq$ 100

1 $\leq$ $X$ $\leq$ $N$

1 $\leq$ $Y$ $\leq$ $M$

1 $\leq$ $T$ $\leq$ 100000

## Example

`chatnoir.in`
```
5
2 2 1 2
20 20 10 10
20 15 14 6
13 13 10 11
5 7 1 7
```

`chatnoir.out`
```
DA
NU
NU
DA
DA
```