“Arrows� is a game played on a rectangular board whose surface is divided into $N \\cdot M$ cells, arranged in $N$ rows and $M$ columns. Each cell contains an arrow (up, down, left, or right), as shown in the figure below:

~[arrows.png]

When it’s a player's turn, they can choose a starting position where they place a token, then move the token to the adjacent cell indicated by the arrow's direction. The movement continues until the token leaves the game board, in which case the player gets a score equal to the number of cells traversed by their token. However, there are certain starting positions called favorable, where the token will **never** leave the game board. For example, all positions in the figure with a gray background are favorable. The player who chooses a favorable starting position gets a score equal to the number of distinct cells visited multiplied by $1000$.

Write a program that, given the game board configuration, solves one of the following tasks:

1. Determine the score a player gets when placing their token on a specified starting position.
2. Determine the number of favorable cells on the game board.
3. Determine the maximum score a player can get in one turn by conveniently choosing the starting position.

# Input data

The input file `arrows.in` contains:
- On the first line, the task that needs to be solved ($1, 2$ or $3$).
- The second line contains the natural numbers $N \\ M$, representing the number of rows and columns of the game board respectively.
- On the next $N$ lines, there are $M$ numbers from the set {$1,2,3,4$} representing the arrows in the cells of the game board ($1$ signifies right arrow, $2$ up arrow, $3$ left arrow, and $4$ down arrow).
- The last line contains the natural numbers $lin \\ col$, representing the row and column of the specified starting position. Values on the same line in the input file are separated by spaces.

# Output data

The output file `arrows.out` will contain a single line with a natural number representing the answer for the task specified on the first line of the input file.

# Constraints and clarifications

* $1 \\leq N, M \\leq 500$;
* Rows are numbered from $1$ to $N$, and columns from $1$ to $M$.
* For tests worth $20$ points the task is $1$. For tests worth $40$ points the task is $2$. For the remaining tests, also worth $40$ points, the task is $3$.

# Example 1

`arrows.in`
```
1
6 5
3 1 1 4 2
1 2 4 3 1
4 2 1 1 4
1 2 3 3 3
3 1 4 4 4
2 2 3 4 2
5 5
```

`arrows.out`
```
2000
```

## Explanation

The example corresponds to the game board in the figure. The scores for each position are:
```
1 14000 14000 14000 1
15000 14000 14000 14000 1
16000 14000 14000 14000 14000
15000 14000 14000 14000 14000
1 4000 4000 2 2000
2 4000 4000 1 2000
```
The task is $1$: the score obtained starting from the position on row $5$ and column $5$ is $2000$.

# Example 2

`arrows.in`
```
2
6 5
3 1 1 4 2
1 2 4 3 1
4 2 1 1 4
1 2 3 3 3
3 1 4 4 4
2 2 3 4 2
5 5
```

`arrows.out`
```
23
```

## Explanation

The task is $2$: there are $23$ favorable positions.

# Example 3

`arrows.in`
```
3
6 5
3 1 1 4 2
1 2 4 3 1
4 2 1 1 4
1 2 3 3 3
3 1 4 4 4
2 2 3 4 2
5 5
```

`arrows.out`
```
16000
```

## Explanation

The task is $3$: the maximum score can be obtained by placing the token at the starting point on row $3$ and column $1$.