In Macarie's garden, there are $N^2$ fruit trees of different heights, planted in the form of a grid of $N$ rows and $N$ columns, numbered from $1$ to $N$. Since there are birds that eat their fruits, Macarie thought to place surveillance systems that provide some degree of protection to the trees situated on the row and column where it is placed, in all four directions of movement: North, South, East, and West, i.e., left and right within the row and up and down within the column. In any of these four directions of movement, the surveillance provided by a system is interrupted when it encounters a tree of height strictly greater than the tree in which it was placed.

# Task

Knowing the heights of all $N^2$ trees, write a program that:

1. Assuming that Macarie has a single surveillance system, determine for a given row $L$ which column of the tree should be placed the surveillance system so that a maximum number of trees are protected. If there are multiple solutions, the smallest column will be displayed.
2. Assuming that Macarie placed a surveillance system in each tree of his garden, determine the row and column of the tree protected by the most surveillance systems. If there are multiple solutions, the smallest row solution will be displayed, and in case the rows are equal, the smallest column will be displayed.

# Input data

The input file `pasari.in` will contain on the first line a natural number $C$ which can have the values $1$ or $2$ and represents the number of the task that needs to be solved. If $C$ = $1$ then the second line contains the pair of natural numbers $N$ and $L$ separated by a space, and if $C = 2$, the second line contains a natural number $N$ having the significance from the statement. On the following $N$ lines, $N$ natural numbers separated by a space representing in order, the heights of the trees on each row, starting from the first to the last.

# Output data

The output file `pasari.out` will contain on the first line:

* if $C = 1$ a single natural number representing the smallest column determined according to the task
* if $C = 2$ two natural numbers representing the row and column determined according to the task

# Constraints and clarifications

* $5 \leq N \leq 1\ 000$
* $1 \leq$ the height of any tree $\leq 100\ 000$
* For correctly solving the first task, you can obtain $30$ points, and for correctly solving the second task, you can obtain $70$ points.

# Example 1

`pasari.in`
```
1
5 2
8 4 3 9 1
5 1 4 2 1
6 7 2 3 1
7 6 4 1 1
1 1 1 1 1
```

`pasari.out`
```
3
```

## Explanation

On row $2$ the optimal placement is in column $3$, thereby protecting $8$ trees.

# Example 2

`pasari.in`
```
2
5
1 2 3 2 1
2 2 3 2 2
3 2 3 2 3
2 2 3 2 2
1 2 3 2 1
```

`pasari.out`
```
3 2
```

## Explanation

The tree located at positions $(3,2)$, i.e., on row $3$ and column $2$, is surveilled by eight systems. These are located at positions $(1,2)$, $(2,2)$, $(3,2)$, $(4,2)$, $(5,2)$, $(3,1)$, $(3,3)$, and $(3,5)$. The tree located at positions $(3,4)$ is also protected by eight surveillance systems, but according to the rules in the statement, the one on the smaller row, respectively $3\ 2$, will be displayed.
