Let's consider a rectangle in the plane with sides $a$ and $b$. According to Pythagoras' theorem, the length of the diagonal $d$ adheres to the equation $d^2 = a^2 + b^2$. The lengths of the sides $a$ and $b$ can be chosen from the set of natural numbers such that the length of the diagonal is also a natural number. For example, for a rectangle with sides $5$ and $12$, the diagonal will have a length of $13$.

This property can be generalized to space as well. If we have a rectangular parallelepiped with three edges $a$, $b$, and $c$, then the length of the diagonal and the lengths of the edges adhere to the equation: $d^2 = a^2 + b^2 + c^2$. We can also find lengths from the set of natural numbers for the edges so that the diagonal is also a natural number. For example, if the edges of the rectangular parallelepiped are $4$, $4$, and $2$, then the diagonal will have a length of $6$.

In general, if we have a rectangular parallelepiped in a $k$-dimensional space, whose edges have lengths $a_1, a_2, \dots, a_k$, the length of the diagonal and the lengths of the edges will adhere to the equation $d^2 = a_1^2 + a_2^2 + \dots + a_k^2$.

# Task

Given the dimension $k$ of the space, find a $k$-dimensional parallelepiped where both the diagonal $d$ and the lengths of the edges $a_1, a_2, \dots, a_k$ are natural numbers.

# Input data

The file `pitagora.in` will contain on the first line the value of $k$ as mentioned above.

# Output data

The file `pitagora.out` will contain several lines. The first line will contain the value of $d$, the second line will contain the value $p$ (the number of distinct numbers in the sequence $a_1, a_2, \dots, a_k$), and on the next $p$ lines, two natural numbers separated by a space: on line $i + 2$ the numbers $f_i$ and $c_i$ will be found, with the meaning that a number $f_i$ of edges of the $k$-dimensional parallelepiped are equal to the value $c_i$.

# Constraints and clarifications

* $2 \leq k \leq 100\ 000\ 000$
* $0 < d_2 \leq 2\ 000\ 000\ 000$
* $0 < c_1, c_2, \dots, c_p, f_1, f_2, \cdot, f_p$
* $d_2 = f_1 \cdot c_1^2 + f_2 \cdot c_2^2 + \dots + f_p \cdot c_p^2$
* $k = f_1 + f_2 +\ \dots + f_p$
* The problem solution is not unique. Any correct solution will be accepted

# Example 1

`pitagora.in`
```
4
```

`pitagora.out`
```
2
1
4 1
```

## Explanation

In a $4$-dimensional space $(k=4)$, a diagonal of length $2$ is obtained with $4$ edges of length $1$, because $2^2 = 1^2 + 1^2 + 1^2 + 1^2$.

# Example 2

`pitagora.in`
```
3
```

`pitagora.out`
```
6
2
1 2
2 4
```

## Explanation

In a three-dimensional space $(k=3)$, a diagonal of length $6$ is obtained with one edge of length $2$ and two other edges of length $4$. $(6^2 = 2^2 + 4^2 + 4^2)$