Ionuț goes at the end of the week to relax in an amusement park. At the entrance of the park, there is a large square paved with marble tiles of the same size. Each tile has a single number written on it from $f(1), f(2), f(3), \dots, f(n)$, where $f(k)$ is the sum of the digits of $k$, for $k$ in the set $\{1, 2, \dots, n\}$. The square has the shape of a two-dimensional array with $n$ rows and $n$ columns. The tiles that make up the square are arranged as follows:

- on the first row, there are tiles with the numbers $f(1), f(2), \dots, f(n-2), f(n-1), f(n)$ (in this order from left to right);
- on the second row, there are tiles with the numbers $f(n), f(1),f(2), f(3), \dots, f(n-1)$ (in this order from left to right);
- on the third row, there are tiles with the numbers $f(n-1), f(n), f(1), f(2), f(3), \dots, f(n-2)$ (in this order from left to right);
- $\dots$
- on the last row, there are tiles with the numbers $f(2), \dots, f(n-2), f(n-1), f(n), f(1)$ (in this order from left to right).

Ionuț's parents want their son to solve at least one sum problem on this day. Thus, they propose that Ionuț determines the sum of the numbers located in the rectangular area of the square having the corners in the positions where they are standing. The father is on row $i_T$ and column $j_T$ (top-left corner), and the mother is on row $i_M$ and column $j_M$ (bottom-right corner). The area of the square for which the sum is desired is rectangular, with sides parallel to the edges of the square (see the filled area in the example). If Ionuț can calculate the required sum, he will be rewarded in the amusement park by his parents.

# Task
Determine the sum requested by Ionuț's parents.

# Input data

The input file `piata.in` contains on the first line the natural number $n$ representing the size of the square. The second line contains the natural numbers $i_T$ and $j_T$ separated by a space. The third line contains the natural numbers $i_M$ and $j_M$ separated by a space.

# Output data

The output file `piata.out` will contain on the first line the requested sum.

# Constraints and clarifications

* $2 \leq n \leq 40\ 000$
* $1 \leq i_T, j_T, i_M, j_M \leq n$
* $i_T \leq i_M$
* $j_T \leq j_M$
* The sum requested by Ionuț's parents never exceeds the value $2\ 100\ 000\ 000$.
* $20\%$ of the tests have $n \leq 250$
* $30\%$ of the tests have $250 \leq n \leq 10\ 000$
* $30\%$ of the tests have $10\ 001 \leq n \leq 28\ 000$
* $20\%$ of the tests have $28\ 001 \leq n \leq 40\ 000$

# Example

`piata.in`
```
6
2 3
6 5
```

`piata.out`
```
51
```

## Explanation

The square looks like this:

~[0889d8c392228b59432e5581ece783bc.png]

The sum of the numbers in the requested area (marked above) is $51$.