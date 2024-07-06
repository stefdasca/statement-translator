Freshly relieved from his conflicts with the police, Gigel wants to organize a trip to the mountains. He discovered a rectangular area of $N$ meters wide and $M$ meters long, divided into $N \cdot M$ elementary square surfaces of side $1$ and with sides parallel to the sides of the surface. For simplicity, we will refer to it as a matrix denoted by $A$ having $N$ rows (numbered from $1$ to $N$) and $M$ columns (numbered from $1$ to $M$). For each square $(i, j)$, the height $A_{ij}$ is known.

From a square $(i, j)$, Gigel can move, within the surface, to any of the squares: $(i, j+1)$, $(i, j-1)$, $(i-1, j)$, $(i+1, j)$, if they exist. A valid path in Gigel's view is a path that starts from any square $(x, y)$ and has the following properties:
* The height of each square $(i, j)$ through which it passes satisfies the relation: $A_{ij} \geq A_{xy} - D$ (where $D$ is a given constant);
* The square $(x_f, y_f)$ where the path ends (called final destination), has a height greater than or equal to the height of the square $(x, y) \ A_{x_f, y_f} \geq A_{xy}$.

# Task

Write a program to help Gigel find out, for each initial square, how many distinct final destinations exist for valid paths that start from that square.

# Input data

The input file `mexc.in` contains on the first line three natural numbers $N \ M \ D$, separated by a space, with the meaning from the statement. Each of the following $N$ lines will contain $M$ natural numbers, separated by a space, representing the values of the elements of matrix $A$.

# Output data

The output file `mexc.out` will contain $N$ lines containing $M$ natural numbers each, separated by a space, the $i$-th number on the $j$-th line in the `mexc.out` file representing the number of distinct final destinations that can be reached by valid paths starting from the square $(i, j)$.

# Constraints and clarifications

* $1 \leq N, M \leq 800$
* $0 \leq D \leq 100\ 000$
* $0 \leq A_{ij} \leq 100\ 000$
* The final destination can coincide with the starting point. A path consisting of a single square is considered valid.

# Example

`mexc.in`
```
5 6 2
7 7 7 7 7 7
7 3 3 3 3 7
7 3 5 6 3 7
7 3 3 3 3 7
7 7 7 7 7 10
```

`mexc.out`
```
18 18 18 18 18 18
18 30 30 30 30 18
18 30 20 1 30 18
18 30 30 30 30 18
18 18 18 18 18 1
```

## Explanation

For the squares of height $7$, the final destination can be any square of height $7$ and the square of height $10$. 
For the squares of height $3$, the final destination can be any square.
For the square of height $5$, the final destination can be any square except those of height $3$.
For the square of height $6$, the final destination can only be itself (it cannot pass through squares of height $3$ due to the first restriction).
For the square of height $10$, the final destination can only be itself.