## Task

In a skiing competition, a time trial event is taking place, where competitors must finish the course in the shortest possible time. They will compete consecutively and, after finishing, they will be informed of their position in the interim ranking. Specifically, after the $p$-th competitor finishes, they will know their position in the ranking formed by the first $p$ competitors. Given the interim positions, you are required to determine the final ranking of the competition.

## Input data

The first line of the input file `schi.in` contains $N$, representing the number of competitors lined up at the start of the competition. The next $N$ lines each contain an integer value indicating the position occupied by each competitor in the interim ranking, updated after their performance.

## Output data

The output file `schi.out` will contain $N$ lines. On line $i$, print the starting number of the competitor who occupies the $i$-th position in the final ranking.

## Constraints and clarifications

$1 \leq N \leq 30000$

## Example

`schi.in`
```
8
1
1
3
4
4
2
1
3
```

`schi.out`
```
7
2
8
6
1
3
5
4
```