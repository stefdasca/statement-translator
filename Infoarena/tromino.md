## Task

For a configuration $2^K \times 2^K$, explained in the statement, Bulbuka asks you $Q$ questions of the following type: how many 90-degree rotations are needed to move the missing square from position $(S_R, S_C)$ to $(F_R, F_C)$?

## Input data

The input file `tromino.in` contains on the first line two values $K$ and $Q$, where $2^K \times 2^K$ represents the size of the board and $Q$ represents the number of questions posed by Bulbuka. Each of the following $Q$ lines in the file represents a question and contains the values $(S_R, S_C, F_R, F_C)$ where $(S_R, S_C)$ represents the initial coordinates of the missing square and $(F_R, F_C)$ represents the final coordinates where the missing square will be placed.

## Output data

The output file `tromino.out` will contain $Q$ lines, representing the answers to the $Q$ questions.

## Constraints and clarifications

$1 \leq K \leq 60$;

$3 \leq Q \leq 5000$;

$0 \leq S_R, S_C, F_R, F_C < 2^K$

It is guaranteed that for any position of the missing square, there is a unique board configuration.

For 15% of the tests $K \leq 3$

## Example

`tromino.in`
```
2 1
1 3
0 0
4 3
5 0
0 0
0 1
0 0
1 1
0 0
3 3
0 0
2 4
1 0
1 0
1 2
6 8
0
```

`tromino.out`
```
3
5
1
0
```