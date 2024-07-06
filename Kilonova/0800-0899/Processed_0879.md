A child is constructing a triangle with natural numbers as follows:

* At the top of the triangle, the value $1$ is written;
* The lines of the triangle are filled from top to bottom, and the boxes on the same line from left to right with consecutive natural numbers, as in the following figures.

~[numere.png]

In the figure on the left, a triangle with $5$ lines is illustrated, containing natural numbers from $1$ to $15$. In this triangle, the child starts to construct paths, respecting the following rules:

* Any path starts from $1$;
* From any box, one can move either to the box situated on the next line to its left (movement coded with $1$) or to the box situated on the next line to its right (movement coded with $2$);
* Any path will be described by the sequence of movements made.

For example, the path illustrated in the figure on the right can be described as follows: $1$, $2$, $2$, $2$.

# Task

Write a program that solves the following two tasks:

* Read the description of a path and display the number at which the path ends;
* Read a positive natural number $K$, determine a path ending with the number $K$ for which the sum of the numbers through which the path passes is maximum, and display this sum.

# Input data

The input file `numere.in` contains on the first line a natural number $C$ representing the task to be solved ($1$ or $2$).

* If $C$ equals $1$, the second line in the file contains a natural number $N$, representing the length of the path, and the third line in the file contains the path description in the form of $N$ values, $1$ or $2$, separated by spaces.
* If $C$ equals $2$, the second line in the file contains the natural number $K$.

# Output data

The output file `numere.out` will contain a single line with a single natural number. If $C = 1$, it will contain the number at which the described path ends as recorded in the input file. If $C = 2$, it will contain the maximum sum of the numbers on a path that ends with the number $K$.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000$;
* $1 \leq K \leq 100\ 000$;
* For correctly solving task $1$, $40$ points are awarded; for correctly solving task $2$, $50$ points are awarded. $10$ points are awarded by default.

# Example 1

`numere.in`
```
1
4
1 2 1 2
```

`numere.out`
```
13
```

## Explanation

The task is $1$. The described path has a length of $4$ and passes through the numbers $1$, $2$, $5$, $8$, $13$.

# Example 2

`numere.in`
```
2
9
```

`numere.out`
```
19
```

## Explanation

The task is $2$. The maximum sum is obtained on the path that passes through the numbers $1$, $3$, $6$, $9$ ($1$ + $3$ + $6$ + $9$ = $19$).