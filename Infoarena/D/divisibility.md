## Divisibility

Two players $X$ and $Y$, play the following game: The players are given a positive integer $P$ and a set $A$ consisting of $N$ non-negative, distinct integers $A = \{a_1, a_2, \dots, a_N \}$, such that each $a_i$ is less than $P$. Players move alternately. Each player on their turn removes a number from set $A$. If after exactly $K$ moves, the sum of the remaining numbers in $A$ is divisible by $P$ - player $X$ wins. Otherwise - player $Y$ wins. Determine who wins if both players play optimally.

## Task

The first line of the input file `divisibility.in` contains a positive integer $T$ - the number of games in the current test.
After this, for each $i = 0, 1, \dots, T-1$:
The $i$-th line contains the numbers $N, K, P$, separated by space;
The $i$-th line contains one of the symbols $X$ or $Y$, indicating which player takes the first move;
The $i$-th line contains the numbers $a_1, a_2, \dots, a_N$, separated by space.

## Input data

The first line of the input file `divisibility.in` contains a positive integer $T$ - the number of games in the current test.
After this, for each $i = 0, 1, \dots, T-1$:
The $i$-th line contains the numbers $N, K, P$, separated by space;
The $i$-th line contains one of the symbols $X$ or $Y$, indicating which player takes the first move;
The $i$-th line contains the numbers $a_1, a_2, \dots, a_N$, separated by space.

## Output data

The first line of the output file `divisibility.out` will contain $T$ symbols (without separators), one symbol for each game in the test. The $i$-th symbol will be $X$ if $X$ won in the $i$-th game, regardless of how $Y$ played; otherwise, the symbol must be $Y$.

## Constraints and clarifications

$1 \leq K \leq N \leq 5000$

$1 \leq P \leq 10^{18}$

$0 \leq a_i < P$ for each $0 \leq i < N$

$a_i \neq a_j$ for each $0 \leq i < j < N$

For $20\%$ of the tests $N \leq 25$

In another $20\%$ of the tests $P$ is a prime number.

## Example

`divisibility.in`
`
3
5 3 7 X
1 2 3 4 6
8 4 13 Y
5 10 6 11 2 8 9 3
6 1 12 X
1 4 5 7 9 11
`

`divisibility.out`
`
XYX
`