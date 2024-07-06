### A Pairwise Prime Array

An array $x_1, x_2, \dots x_N$ is called **pairwise prime** if for every $i$ from $1$ to $N - 1$, $x_i$ and $x_{i+1}$ are coprime.  
Two numbers are coprime if their greatest common divisor is $1$.

Given $N$ and an array $a_1, a_2, \dots a_N$ of non-zero natural numbers, you can perform an operation where you choose a non-zero natural number $x$ and insert it anywhere in the array.

# Task

Determine the minimum number of operations needed to make the array $a$ pairwise prime.

# Input data

The first line of the file `vecoprim.in` contains the number $N$. The second line contains the array $a_1, a_2 \dots, a_N$.

# Output data

Print to the file `vecoprim.out` the **minimum** number of operations needed to make the array pairwise prime.

# Constraints and clarifications

* $2 \leq N \leq 100\ 000$  
* $1 \leq a_i \leq 10^9$

|#| Score | Constraints|
|-|--------|-----------|
|1|20|$N = 2$|
|2|80|No additional constraints|

# Example

`vecoprim.in`
```
6
2 4 7 3 6 1
```

`vecoprim.out`
```
2
```

## Explanation

We can insert the value $3$ between the numbers $2$ and $4$. Then, we can insert the value $5$ between the numbers $3$ and $6$. The resulting array is $2,\underline{3},4,7,3,\underline{5},6,1$ which is pairwise prime (the underlined values are the added ones). It can be shown that a smaller number of operations is not possible.