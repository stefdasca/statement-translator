~[pascal.png|align=right|width=20em]

Pascal's Triangle is a geometric arrangement of numbers named after the famous French mathematician Blaise Pascal (June 19, 1623 – August 19, 1662), as he was the first person to discover the significance of all the patterns within it.

The triangle starts with the number $1$. This row is considered the $0$th row of the triangle. The rest of the numbers in this triangle are formed as the sum of the two numbers above (considering that all numbers outside the triangle are always zero). Therefore, the $1$st row will be formed from $1 = 0 + 1$, $1 = 1 + 0$, and the $2$nd row will be formed from $1 = 0 + 1$, $2 = 1 + 1$, $1 = 1 + 0$.

Let $n$ and $p$ be two non-zero natural numbers with the following properties:

* $p$ is a prime number;
* $n+1$ is a natural power of $p$.

We denote by $M(p)$ the number of multiples of $p$ in the first $n+1$ rows of Pascal's triangle.

# Task

Write a program that reads the natural numbers $n$ and $p$ and determines the number $M(p)$.

# Input data

The input file `pascal.in` contains on the first line the natural numbers $n$ and $p$ separated by a space.

# Output data

The output file `pascal.out` will contain on the first line the number $M(p)$ as described above.

# Constraints and clarifications

* $2 \leq n \leq 10^9$
* $2 \leq p \leq 10^3$
* $30\%$ of tests have $n \leq 10^4$.
* $50\%$ of tests have $n \leq 10^6$.

# Example 1

`pascal.in`
```
7 2
```

`pascal.out`
```
9
```

## Explanation

In the first $8$ rows of the triangle, there are $9$ multiples of $2$: $2$, $4$, $6$, $4$, $10$, $10$, $6$, $20$, $6$.

# Example 2

`pascal.in`
```
2196 13 
```

`pascal.out`
```
1660932
```

## Explanation

In the first $2\ 197$ rows of the triangle, there are $1\ 660\ 932$ multiples of $13$.

# Example 3

`pascal.in`
```
282475248 7
```

`pascal.out`
```
39599936523348201
```

## Explanation

In the first $282\ 475\ 249$ rows of the triangle, there are $39\ 599\ 936\ 523\ 348\ 201$ multiples of $7$.