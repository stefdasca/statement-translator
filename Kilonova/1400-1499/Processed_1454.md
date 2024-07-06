## Bunny Coconaș Wants to Reach the Carrot Garden

Bunny Coconaș wants to reach the carrot garden. To do this, he must hop through an area with special properties. The area consists of $N$ numbered cells from $1$ to $N$, arranged sequentially, and each cell contains a natural number representing the amount of energy needed for the bunny to hop to another cell.

The bunny starts in a specified cell and moves from left to right towards the carrot garden according to the following rules:

* The number written in the cell where the bunny is located represents the number of cells he will hop over.
* If the number written in the cell where the bunny is located is a prime number, then his energy doubles and he will jump over twice the number of cells.
* The counting of cells to hop over is done from left to right, starting with the immediate next cell. For instance, if the bunny is in the third cell and the number written in this cell is $5$, the bunny will land in the cell numbered $13$ ($13 = 3 + 2 \cdot 5$).
* If the bunny lands in a cell that contains the number $0$, he will stay there because he no longer has the energy to hop further. Otherwise, he continues to hop following the above rules.
* The bunny reaches the carrot garden if the last hop he makes exceeds cell $N$.

# Task

Write a program that reads three natural numbers $P$, $N$, and $K$ and then $N$ natural numbers and determines:

1) Whether the bunny can reach the carrot garden starting from cell $K$, and the number of hops the bunny makes starting from cell $K$.
2) The starting cell of the bunny so that the path he takes crosses a maximum number of cells. To determine the number of cells, the starting cell, all cells the bunny hopped over, and all cells he landed in as a result of the hops will be taken into account. The bunny can start from any cell. If there are two or more starting cells that lead to the same maximum number of crossed cells, the starting cell with the smallest order number will be considered.

# Input Data

The input file `iepuras.in` contains on the first line a natural number $P$. For all test inputs, the number $P$ can only have the value $1$ or $2$. The second line of the `iepuras.in` file contains, in this order, the natural numbers $N$ and $K$, separated by a space. The third line contains $N$ natural numbers separated by a space, representing the values in each cell in order from $1$ to $N$.

# Output Data

If the value of $P$ is $1$, only point $1)$ of the tasks will be solved. In this case, the output file `iepuras.out` will contain on the first line the word *YES* if the bunny has reached the carrot garden, or the word *NO* otherwise, and on the second line will contain a natural number representing the number of hops the bunny makes starting from cell $K$.
If the value of $P$ is $2$, only point $2)$ of the tasks will be solved. In this case, the output file `iepuras.out` will contain on the first line two natural numbers separated by a space representing, in order, the starting cell and the maximum number of cells determined, and on the second line, a sequence of natural numbers separated by a space representing the numbers from the cells the bunny did not land in or hop over during his path, from left to right, starting with cell $1$. If the maximum number of cells crossed is exactly $N$, the second line will not contain any number.

# Constraints and Clarifications

* $1 \leq N \leq 7\ 000$
* $1 \leq K \leq N$
* $0 \leq$ the numbers contained in the cells $\leq 100$
* Correct resolution of the first task is awarded $30$ points
* Correct resolution of the second task is awarded $70$ points.

# Example 1

`iepuras.in`
```
1
14 3
2 3 4 0 1 1 2 1 4 0 0 2 1 1
```

`iepuras.out`
```
NO
2
```

## Explanation

$P = 1$, for this test, point $1)$ is solved.
The bunny starts from cell $3$, hops to cell $7$ and then to cell $11$, where finding the number $0$, he stops.

# Example 2

`iepuras.in`
```
2
14 3
2 3 6 0 1 1 2 1 4 0 0 2 3 1
```

`iepuras.out`
```
2 13
1 3 4 5 6 7 10 11 12 14
```

## Explanation

$P = 2$, for this test, point $2)$ is solved.
To cross the maximum number of cells, the bunny starts from cell $2$ and hops, sequentially, to cells $8$, $9$, $13$, and then to the garden, thus crossing $13$ cells (from cell $2$ to cell $14$).
The bunny did not land in or hop over the cells position $1$, $3$, $4$, $5$, $6$, $7$, $10$, $11$, $12$, and $14$.