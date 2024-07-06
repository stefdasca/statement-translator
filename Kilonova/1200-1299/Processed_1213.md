# Task

Write a program that, knowing the number of shelves and the number of book volumes on each shelf, determines the maximum number of volumes that can be moved to the new room, knowing that the first shelf has already been moved and the others are chosen so that they are not placed next to each other. If there are shelves without books, they will not be moved to the second room.

# Input data

The input file `biblos.in` contains on the first line a value $n$, a natural number representing the number of shelves, the second line contains $n$ natural numbers, $x_1, x_2, \ldots, x_n$ separated by a space with the meaning $x_i =$ number of book volumes on each shelf.

# Output data

The output file `biblos.out` will contain a single line containing a natural number representing the maximum number of volumes that have been transferred.

# Constraints and clarifications

* $1 \leq n \leq 30\ 000$
* $0 \leq x_i \leq 32\ 767$, where $ i = 1 \ldots n$ and $x_i$ represents the number of books on shelf $i$
* For $70\%$ of the tests $n \leq 1\ 000$
* Each line of the input and output files ends with a newline character.

# Example 1

`biblos.in`
```
7
1 3 6 2 5 8 4
```

`biblos.out`
```
16
```

# Explanation

The maximum sum is obtained by moving shelves $1$(mandatory), 3, 5, 7 (adjacent shelves are not allowed)

# Example 2

`biblos.in`
```
15
3 1 84 9 89 55 135 49 176 238 69 112 28 175 142
```

`biblos.out`
```
836
```

# Explanation

The maximum sum is obtained by moving shelves $1, 3, 5, 7, 10, 12, 14$

# Example 3

`biblos.in`
```
8
7 1 4 12 9 9 12 4
```

`biblos.out`
```
32
```

# Explanation

The maximum sum is obtained by moving shelves $1, 3, 5, 7$, or by moving shelves $1, 4, 6, 8$