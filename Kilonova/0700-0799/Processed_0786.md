Gigel learned in mathematics the definition of the factorial of a nonzero natural number $n$. It is the product of all natural numbers starting with $1$ and ending with the respective number and is denoted by $n!$. Thus, the factorial of the natural number $6$ is $6! = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6$ and is equal to $720$. The factorials of natural numbers grow extremely fast. For example, $7! = 5040$ while $10! = 3628800$.

Being a good mathematician, Gigel imagined another method to indicate the factorial of a number. Thus, he knows that a nonzero natural number can be decomposed into prime factors. For example, $720$ can be written as $2^4 \cdot 3^2 \cdot 5^1$. Gigel encodes the decomposition into prime factors as follows: $4 \\ 2 \\ 1$ indicating that in the decomposition of $720$ into prime factors, the factor $2$ appears $4$ times, the factor $3$ appears two times, and the factor $5$ appears once. In other words, Gigel indicates for each prime number $\leq n$ the power at which it appears in the decomposition into prime factors of $n!$.

# Task

Write a program that reads a sequence of nonzero natural numbers and displays the factorials of the numbers read in the manner described in the statement.

# Input data

The input file `factori.in` contains multiple nonzero natural numbers, one number per line. The last line of the input file contains the value $0$ indicating that the set of numbers has ended.

# Output data

The output file `factori.out` will contain one line for each nonzero number in the input file. Each line $i$ in the output file will describe the decomposition into prime factors of the factorial of the number on line $i$ of the input file, in the manner described in the statement. The numbers written on the same line will be separated by a space.

# Constraints and clarifications

* The natural numbers in the input file (except the last one) are in the range $[2, 60\ 000]$.
* The input file contains at most $10$ nonzero natural numbers.

# Example

`factori.in`
```
2
8
15
10
0
```

`factori.out`
```
1
7 2 1 1
11 6 3 2 1 1
8 4 2 1
```

## Explanation

$2! = 2$

$8! = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 \cdot 5 \cdot 7$

$15! = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 \cdot 3 \cdot 3 \cdot 3 \cdot 3 \cdot 5 \cdot 5 \cdot 5 \cdot 7 \cdot 7 \cdot 11 \cdot 13$

$10! = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 \cdot 3 \cdot 3 \cdot 5 \cdot 5 \cdot 7$