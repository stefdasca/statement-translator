# Task

Specify the side length and coordinates of the bottom-right corner for each slice of cake received, in the order specified above.

# Input data

The file `tort.in` contains on the first line the natural numbers $N$ and $M$, separated by a space, representing the length and width of the cake. On the next $N$ lines, there will be $M$ characters from the set `0`, ..., `9` representing the type of glaze covering the piece on line $i$ and column $j$ of the cake. The lines and columns are numbered from $1$ to $N$, respectively from $1$ to $M$. In a line, there is no space between any two adjacent characters.

# Output data

In the output file `tort.out`, print the slices of cake in the order **XORin** will receive them. For each slice, print the side length of the slice, as well as the coordinates of the bottom-right corner, values separated by a single space.

# Constraints and clarifications

* $1 \leq N,M \leq 500$
* The numbering of the lines and columns does not change after the elimination operations.
* For $30\%$ of the tests, it is guaranteed that $1 \leq N,M \leq 35$

# Example 1

`tort.in`
```
4 7
1111111
1112333
1112333
4444333
```

`tort.out`
```
3 3 3
3 4 7
1 1 4
1 1 5
1 1 6
1 1 7
1 2 4
1 3 4
1 4 1
1 4 2
1 4 3
1 4 4
```

## Explanation

The first slice received by **XORin** will be the one with the bottom-right corner $(3,3)$ and side $3$.

The second slice will be the one with the bottom-right corner $(4,7)$ and side $3$.

The next slice will be the one with the bottom-right corner $(1,4)$ and side $1$, and so on.