# Matrix3

Laura has a new matrix, this time binary, with $N$ rows and $M$ columns. As usual, being naturally curious, Laura asks $Q$ questions of the form: What is the maximum side of a square that contains only $0$s completely within the rectangle with the top-left corner at $(x_1, y_1)$ and the bottom-right corner at $(x_2, y_2)$?

## Task

Answer Laura's questions.

## Input data

The first line of the input file matrice3.in contains 3 integers $N$, $M$, and $Q$ as described in the statement. The next $N$ lines contain $M$ digits from the set $\{0, 1\}$, representing Laura's matrix. The following $Q$ lines contain 4 numbers $x_1$, $y_1$, $x_2$, $y_2$ representing the corners of the rectangle in each question.

## Output data

The output file matrice3.out will contain $Q$ lines, the $i$-th line $(1 \leq i \leq Q)$ will contain a single integer representing the answer to the $i$-th question.

## Constraints and clarifications

$1 \leq N, M \leq 250$

$1 \leq Q \leq 250\ 000$

$1 \leq x_1 \leq x_2 \leq N$

$1 \leq y_1 \leq y_2 \leq M$

For $30\%$ of the tests, $N, M \leq 40$ and $Q \leq 250$.

For another $30\%$ of the tests, $Q \leq 100\ 000$.

## Example

`matrice3.in`
```
5 6 4 
000101 
010100 
110001 
010001 
010000 
1 1 3 3 
1 1 5 6 
2 2 4 5 
4 2 5 2
```

`matrice3.out`
```
1 
3 
2 
0
```