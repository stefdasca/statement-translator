Here is the competitive programming problem statement translated into English:

---

Given $k$, $n$, and $y$ as three natural numbers.
Let $X$ be a sequence formed from $n$ natural numbers: $x_1, x_2, x_3, \ldots, x_n$.
Let $P$ be the product of the numbers $y, x_1, x_2, x_3, \ldots, x_n$, that is: $P = y \cdot x_1 \cdot x_2 \cdot x_3 \cdots x_n$.

The number $P$ is a “**$k$-power**” if there exists a natural number $z$ such that $P = z^k$.

# Task

Write a program that reads the numbers $k$, $n$, $x_1$, $x_2$, $x_3$, $\ldots$, $x_n$ and determines:
1. **The smallest** number and **the largest number** in the array $X$, formed only from identical digits;
2. **The prime factorization of the smallest** natural number $y$ ($y \geq 2$) with the property that $P = y \cdot x_1 \cdot x_2 \cdot x_3 \cdots x_n$ is a "**$k$-power**".

# Input data

The input file `pyk.in` contains:
* The first line contains a natural number $C$ representing the task in the problem that must be solved ($1$ or $2$);
* The second line contains the natural numbers $k$ and $n$, separated by a single space;
* The third line contains the $n$ natural numbers $x_1$, $x_2$, $x_3$, $\ldots$, $x_n$, separated by a single space.

# Output data

If $C = 1$, then the first line of the output file `pyk.out` contains two natural numbers, separated by a single space, representing the answer to task $1$ of the problem. If such numbers do not exist, the first line of the file will contain the value $1$.

If $C = 2$, then the output file `pyk.out` contains:
* The first line contains a natural number $m$ representing the number of distinct prime factors in the prime factorization of the number $y$, determined when solving task $2$;
* Each of the next $m$ lines (one for each prime factor in the prime factorization of $y$) contains two values $F$ and $E$, separated by a single space, representing the prime factor $F$ and the exponent $E$ of this factor in the prime factorization of $y$.

The writing of these prime factors in the file will be done in ascending order of their value.

# Constraints and clarifications

* $2 \leq n \leq 50\ 000$;
* $2 \leq k \leq 100$;
* $2 \leq x_1, x_2, x_3, \ldots, x_n \leq 10\ 000$;
* $2 \leq y$;
* For the correct solving of task $1$, $10$ points are awarded;
* For the correct solving of task $2$, $90$ points are awarded.

# Example 1

`pyk.in`
```
1
2 7
122 1111 5 4 88 123 999
```

`pyk.out`
```
4 1111
```

## Explanation

The task is $1$, $k = 2$, $n = 7$.
The numbers in the array $X$ formed only from identical digits are: $1111$, $5$, $4$, $88$, $999$. The smallest of these numbers is $4$, and the largest is $1111$.

# Example 2

`pyk.in`
```
2
3 6
12 5 60 125 4 36
```

`pyk.out`
```
3
2 1
3 2
5 1
```

## Explanation

The task is $2$, $k = 3$, $n = 6$. The product of the $6$ numbers in the sequence is: $12 \cdot 5 \cdot 60 \cdot 125 \cdot 4 \cdot 36 = 64800000$.

$y = 90$ is the smallest value for which $P = 90 \cdot 64800000 = 1800^3$ becomes a "**$k$-power**".

The prime factorization of $y$ contains $m = 3$ prime factors: $2^1 \cdot 3^2 \cdot 5^1$.

---

Please review the problem description and ensure it meets your requirements.