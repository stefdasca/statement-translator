## Task

In a matrix with obstacles, there is a snake of odd length $L$. Each position of the snake's body covers a cell of the matrix, consecutive positions of the snake cover adjacent cells in the matrix, and any two different positions of the snake cover different cells. The snake does not cover obstacles. Unfortunately, an ordinary mortal can only see the odd positions of the snake's body; even positions are seen as regular cells of the matrix, without obstacles. The matrix is given in the input file with each element having one of the following values:
- $-1$ - obstacle
- $0$ - free position or occupied by an even piece of the snake
- $x$ with $1 \leq x \leq L$ - position occupied by the $x$th piece of the snake

The task is to reconstruct a valid placement of the snake on the matrix. If there are multiple solutions, any of them can be displayed. It is guaranteed that there is at least one solution.

## Input data

The input file snake.in contains on the first line the numbers $N$, $M$, and $L$, representing the number of rows, the number of columns of the matrix, and the length of the snake. On the following $N$ lines, it contains $M$ numbers describing the matrix as specified in the task. All odd numbers from $1$ to $L$ appear exactly once. The Manhattan distance between any two consecutive odd positions of the snake is $2$.

## Output data

The output file snake.out must contain the matrix with the placement of the snake fully described.

## Constraints and clarifications

$1 \leq N, M \leq 100$

For 20 points,

$1 \leq N \times M \leq 20$

It is guaranteed that there is at least one solution.

## Example

`snake.in`

```
4 4 7
-1 3 0 0
1 0 5 0
0 0 0 0
0 0 7 0
```

`snake.out`

```
-1 3 4 0
1 2 5 0
0 0 0 6
0 0 7 0
```