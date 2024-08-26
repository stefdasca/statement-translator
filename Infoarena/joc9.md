# Game9

Three children invented a new game. They drew an equilateral triangle $ABC$ on the pavement and divided it into $N*N$ congruent equilateral triangles. Starting from vertex $A$ of triangle $ABC$ towards the opposite side $BC$, they drew identical circles, one at each vertex of the smaller triangles, and inside each circle, they wrote a non-zero natural number representing the value of the circle, as shown in the accompanying figure drawn for $N = 3$. The children established the game rules: the game can only be played by three contestants; each contestant sits in one of the initial circles located at vertices $A$, $B$, or $C$ of the triangle, called initial circles; each contestant must reach one of the $n + 1$ circles located on the side opposite to the vertex from which they started, in the triangle $ABC$, and can only move in the direction of this side; for example, if a contestant is in the initial circle at vertex $C$, they must reach one of the circles with values: $x1$, $x2$, $x4$, or $x7$ on the opposite side, $AB$; contestants will move by jumping from one circle to another without passing through the same circle more than once; it is allowed for multiple contestants to be in the same circle; each second, simultaneously, contestants must jump into one of the circles located at the shortest distance from the one they are in, towards the corresponding opposite side; for example, a contestant who started from the initial circle at vertex $B$ and is now in the circle with value $x5$ can only jump into one of the circles with values $x3$ or $x6$; contestants are not allowed to jump into a circle that is not in the direction of the corresponding opposite side; the game ends when the contestants reach one of the $n + 1$ circles on the required side of the triangle $ABC$ by making $n$ jumps each; for each contestant, the score will be calculated by adding the value of the initial circle to the values of the $N$ circles they jumped to during the movement; the winner of the game is the contestant with the highest score; there can be multiple winners if multiple contestants achieve the highest score obtained at the end of the game.

## Task

Write a program to determine:
- the maximum score a contestant can achieve at the end of the game;
- the value of the initial circle from which a contestant should start to achieve the maximum score.

## Input data

The input file `joc9.in` contains two lines:
- The first line contains the non-zero natural number $N$.
- The second line contains non-zero natural numbers: $x1$, $x2$, $\dots$, $x \frac{(n+1)*(n+2)}{2}$ separated by a space, representing the values of the circles in the game, in the order given in the statement.

## Output data

The output file `joc9.out` will contain two lines:
- The first line will contain a natural number representing the maximum score a contestant can achieve at the end of the game.
- The second line will contain a natural number representing the value of the initial circle from which a contestant should start to achieve the maximum score.

## Constraints and clarifications

$2 \leq N \leq 135$

$1 \leq x1, x2, \dots, x \frac{(n+1)*(n+2)}{2} \leq 215$

If there are multiple choices for the initial circle, write the smallest value among these initial circles from which the maximum score is achieved.

For solving task 1, you get 30% of the points, and for task 2, 70% of the points.

## Example

`joc9.in`
```
3
10 4 3 11 14 2 9 6 5 7
```

`joc9.out`
```
37
7
```

## Explanation

If the contestant starts from the initial circle at vertex:
- $A$, the highest score they can achieve is $34 (= 10 + 4 + 11 + 9)$
- $B$, the highest score they can achieve is $37 (= 9 + 11 + 14 + 3)$
- $C$, the highest score they can achieve is $37 (= 7 + 5 + 14 + 11)$.

Thus, the maximum score is $37$ and can be achieved if the contestant starts from the initial circles at $B$ and $C$. The circle at $B$ has a value of $9$, while the one at $C$ has a value of $7 < 9$.

On the first line of the file `joc9.out`, the value $37$ (the maximum score) will be written, and on the second line, the value $7$ (the initial circle from $C$ has a smaller value than the one from $B$).