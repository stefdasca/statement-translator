# Collisions

Alinuţa has to compose a poem about ants for school. Yes, it's true, I'm not lying... Therefore, she came up with the idea that it would be good to study these social insects before completing this very important assignment. So, Alinuţa bought $M$ ants and placed them all in a matrix of dimensions $N \times N$. Each ant thus occupies exactly one cell in the matrix. Alinuţa assigned each ant an initial direction (each ant is facing one of the 4 directions (N, S, E, W), coded (^, v, >, <). I hope everything is clear so far. And now, Alinuţa began studying these ants and observed that every second, all the ants take a step in the direction they are facing. However, being algorithmic insects, they know that they should not leave the matrix. So, in the second they are about to step out, they prefer to turn $180$ degrees instead. I don't think that was very well understood... Let's take an example. The rows and columns of the matrix are numbered from $1$ to $N$. If at second $T$ an ant is on the cell $(1, N)$ and is facing EAST (>), then at second $T + 1$ it will still be on the cell $(1, N)$ but will be facing WEST (<). And now, ## task. Alinuţa wants to know after how many seconds two ants will meet for the first time in this matrix. She considers that two ants meet if they step on the same cell of the matrix in the same second. If there are no two ants that ever meet, display only $-1$. Does it make any sense to help Alinuţa find the answer to this ## task?

## Input data

The input file `coliziuni.in` contains the number of tests, $T$, on the first line. Each test has the following structure: the first line contains the numbers $N$ and $M$, as described in the problem statement. On each of the following $M$ lines, you will find the direction of the ant (represented by a character ^, v, >, <), and two natural numbers $X$ and $Y$, representing the initial position of the ant.

## Output data

The output file `coliziuni.out` will contain $T$ lines with one integer each, representing the number of seconds after which two ants will meet for the first time, or $-1$ if this never happens, for each test.

## Constraints and clarifications

$1 \leq N \leq 1000000$

$1 \leq M \leq 50000$

$1 \leq T \leq 1000$

The sum of all $M$ values within the same input file will not exceed $250000$.

For $40\%$ of the score: $T = 10$, $N \leq 2000$, $M \leq 500$

## Example

`coliziuni.in`
```
3
3 2
> 1 1
< 1 3
2 2
^ 1 2
< 2 2
2 2
> 1 1
< 2 2
```

`coliziuni.out`
```
1
3
-1
```