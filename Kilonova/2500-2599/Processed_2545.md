```markdown
# Task

Aquilla's beetle helps us solve the following problem:

If we have an $N$-dimensional chessboard, meaning we have only black and white colored squares, and no $2$ adjacent squares are of the same color, and on each square there is a beetle with a certain orientation (if $N=2$, this can be: up, down, left, right, so it can move towards an adjacent square).

Can we choose an orientation of the beetles such that if they all move at once, no $2$ or more beetles end up on the same square (the orientation must be chosen so that the beetles do not go off the board)? Answer $T$ test cases.

# Input data

The first line contains $T$, followed by $T$ lines, each containing one $N$.

# Output data

Print $N$ rows, the answer can be `DA` or `NU`.

# Constraints and clarifications

* $1 \leq T \leq 10^5$;
* $2 \leq N \leq 10^5$;
* Attention, the answer is `DA` or `NU`, not `YES` or `NO` :)
* An $N$-dimensional chessboard also has sides of length $N$. (A $5$-dimensional board is $5 \times 5 \times 5 \times 5 \times 5$).
* To be even clearer, for example, in a $3$-dimensional board, a beetle can move: up, down, front, back, left, right. And for $N=4$ there are $8$ directions of movement.

# Example 1

`stdin`
```
1
2
```

`stdout`
```
DA
```

## Explanation

$T=1$.
We have a $2 \times 2$ board.
Orientations can be chosen:
The beetle on $(1,1)$ moves down.
The beetle on $(1,2)$ moves left.
The beetle on $(2,1)$ moves right.
The beetle on $(2,2)$ moves up.
The beetles move simultaneously, after moving, there will not be a square with $2$ or more beetles on it.

# Example 2

`stdin`
```
2
3
16
```

`stdout`
```
NU
DA
```

## Explanation

The board is a cube of $3 \times 3 \times 3$, it can be shown that there is no solution.
The board is a cube of $16 \times 16 \times 16 \times 16 \times 16$..., there is a solution.
```