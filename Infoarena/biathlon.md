## Task

Piggy has decided to organize a biathlon race in which participants will compete in two disciplines. She invited $N$ competitors, each possessing the following characteristics: Each competitor has speeds $V_1$ and $V_2$ for the two disciplines, respectively. Competitors have constant speeds ($V_1$ and $V_2$) throughout the entire respective courses. The distance covered by the competitor in time $t_1$ in the first discipline is $S_1 = V_1 * t_1$, and the distance covered in the second discipline in time $t_2$ is $S_2 = V_2 * t_2$. A competitor wins if their total time is the unique smallest sum of the times of all competitors (in other words, it is strictly smaller than all other sums). As the organizer, Piggy can choose any distances she wants (non-negative real numbers $S_1$ and $S_2$) for each of the two disciplines. Now she wonders which competitors are potential winners to determine if there exist $S_1$ and $S_2$ that ensure their victory. Determine which competitors can win.

## Input data

The first line of the input file `biathlon.in` contains the number $N$. The next $N$ lines contain two positive integers $V_1$ and $V_2$, separated by a space: the speeds of the $i$-th competitor (for $i = 0, 1, \dots, N - 1$). 

## Output data

The first line of the output file `biathlon.out` will contain the indices of the competitors who can win. Indices will be ordered in ascending order, separated by spaces. Indices are numbered from $0$. This line must contain the number $-1$ if there is no competitor who can win.

## Constraints and clarifications
Subtask 1 ( $20$ points) :
\[
2 \leq N \leq 100, 1 \leq V_1, V_2 \leq 100
\]

Subtask 2 ( $40$ points) :
\[
2 \leq N \leq 5\,000, 1 \leq V_1, V_2 \leq 10\,000
\]

Subtask 3 ( $40$ points) :
\[
2 \leq N \leq 100\,000, 1 \leq V_1, V_2 \leq 10\,000
\]

## Example

`biathlon.in`

```
4
1 4
2 2
4 1
3 3
```

`biathlon.out`

```
0 2 3
```

`biathlon.in`

```
3
3 3
3 3
2 2
```

`biathlon.out`

```
-1
```

## Explanation

In the first example, competitors $0$, $2$, and $3$ can win. The competitor with index $0$ wins, for example, for distances $S_1 = 0$ and $S_2 = 10$; the competitor with index $2$ wins for $S_1 = 10$ and $S_2 = 0$; the one with index $3$ wins at distances $S_1 = 10$ and $S_2 = 10$. The competitor with index $1$ cannot win: they will always be defeated by the competitor with index $3$. In the second example, only competitors $0$ and $1$ can achieve minimal time, but neither of their times will be unique.