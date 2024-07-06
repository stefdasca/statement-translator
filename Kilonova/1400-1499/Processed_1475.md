Sandu studied various applications with arrays of natural numbers in computer science class, and now he has an interesting problem to solve.

Given is an array $X= \\left(X_1, X_2, \\ldots, X_n\\right)$ of non-zero natural numbers and two natural numbers $p_1$ and $p_2$, where $p_1 < p_2$.

Sandu needs to construct a new array $Y=\\left( Y_1, Y_2, \\ldots,Y_{n \\cdot n}\\right)$ with $n \cdot n$ elements obtained from all products of two elements from the array $X$ (each element in the array $Y$ is of the form $X_i \\cdot X_j$, $1 \\leq i$, $j \\leq n$).

Sandu has to calculate two natural values $d_1$ and $d_2$ obtained from the array $Y$. The value $d_1$ is equal to the maximum possible difference between two values of the array $Y$. To obtain the value $d_2$, Sandu needs to consider the array $Y$ with elements ordered in __descending__ order, and $d_2$ will be the difference between the values located at positions $p_1$ and $p_2$ in the descending ordered array. Sandu quickly found the values $d_1$ and $d_2$ and, to verify them, he asks for your help to determine them as well.

# Task

Given the array $X$ with $n$ elements and values $p_1$ and $p_2$, determine the values $d_1$ and $d_2$.

# Input data

The input file `dif2.in` will contain on the first line a natural number $C$ which can only be $1$ or $2$. If $C = 1$, then the second line will contain the natural number $n$. If $C = 2$, then the second line will contain the natural numbers $n$, $p_1$, and $p_2$ separated by a space. In both cases, the following $n$ lines will contain the elements of the array $X$, one natural number per line.

# Output data

In the case $C = 1$, the output file `dif2.out` will contain on the first line the value $d_1$ equal to the maximum difference between any two values from the array $Y$. In the case $C = 2$, the output file will contain on the first line a natural number $d_2$ representing the difference between the values located at positions $p_1$ and $p_2$ in the array $Y$, assuming it is ordered in descending order.

# Constraints and clarifications

* $3 < n < 300 \ 000$
* $1 \\leq p_1 < p_2 \\leq n^2$
* $1 \\leq X_i < 300 \ 000$, $i = \\{ 1 \\ldots n \\}$
* For tests worth 30 points, $C = 1$, and for tests worth 70 points, $C = 2$
* For tests worth 10 points, $C = 2$ and $n \\leq 100$

# Example 1

`dif2.in`
```
1
4
3
5
2
6
```

`dif2.out`
```
32
```

# Explanation

Attention, $C = 1$, so only task $1$ is solved!

The maximum value $d_1$ will be $32$ and is obtained by calculating the difference between $6 \\cdot 6$ and $2 \\cdot 2$.

# Example 2

`dif2.in`
```
2
4 5 11
3
5
2
6
```

`dif2.out`
```
8
```

# Explanation

Attention, $C = 2$, so only task $2$ is solved!
The following $16$ values are obtained in $Y$: $3 \\cdot 3$, $3 \\cdot 5$, $3 \\cdot 2$, $3 \\cdot 6$, $5 \\cdot 3$, $5 \\cdot 5$, $5 \\cdot 2$, $5 \\cdot 6$, $2 \\cdot 3$, $2 \\cdot 5$, $2 \\cdot 2$, $2 \\cdot 6$, $6 \\cdot 3$, $6 \\cdot 5$, $6 \\cdot 2$, $6 \\cdot 6$. The value $d_2$ will be $8$, because if we consider the array $Y$ ordered in descending order ($36, 30, 30, 25, 18, 18, 15, 15, 12, 12, 10, 10, 9, 6, 6, 4$), then $Y[5] - Y[11] = 18 - 10 = 8$