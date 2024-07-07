
Two groups of digits are given. Each group contains $n$ digits, not necessarily distinct from each other. By arranging all the digits of the first group in some order, we obtain a number denoted $n_1$. Similarly, by arranging all the digits of the second group in some order, we obtain another number, $n_2$.

# Task

Determine $n_1$ and $n_2$ such that the difference $n_1 - n_2$ is greater than or equal to $0$ and minimal. If there are multiple possibilities to form the two numbers to obtain the minimal difference, choose the variant where $n_1$ is minimal.

# Input data

The input file `2numere.in` contains on the first line a natural value representing $n$. On each of the next two lines contain $n$ digits separated by a space.

# Output data

The output file `2numere.out` will contain three lines. The first line will contain a natural number representing the determined value for $n_1$. The second line will contain a natural number representing the determined value for $n_2$. The third line will contain a value representing the difference between $n_1$ and $n_2$.

# Constraints and clarifications

* $2 \leq n \leq 9$; for $50\ \%$ of the tests, $n \leq 5$
* for all test data, a solution exists
* in each of the two groups, there is at least one non-zero digit
* if a program correctly determines the minimal difference, it earns $50\ \%$ of the points; if the program correctly determines the smallest value of $n_1$ for which this difference is obtained, it earns $100\ \%$ of the points.
* digits of $0$ at the beginning of the numbers $n_1$ or $n_2$ will not be displayed

# Example 1

`2numere.in`
```
2
2 4
9 1
```

`2numere.out`
```
24
19
5
```

# Example 2

`2numere.in`
```
4
3 4 2 4
9 0 1 5
```

`2numere.out`
```
2344
1950
394
```

# Example 3

`2numere.in`
```
3
4 0 0
0 4 0
```

`2numere.out`
```
4
4
0
```

## Explanation

There are other values for $n_1$ and $n_2$ that give the difference $0$, but $n_1$ is not minimal, for example $n_1 = 40$ and $n_2 = 40$.
