> Boy oh boy, you have two more lives left

[Don](https://kilonova.ro/problems/653/) loves correctly parenthesized strings, your friend Raul loves sequences, and you love number theory. Don has asked you to write a problem that meets the quality of [RoAlgo](https://discord.gg/E82gRbUBCJ) contests and to provide a solution to this problem. You decided to combine number theory, correctly parenthesized strings, and sequences into a single problem.

A string is called correctly parenthesized if and only if characters $+$ and $1$ can be inserted such that the resulting string represents a correct [mathematical expression](https://ro.wikipedia.org/wiki/Expresie_matematic%C4%83). For example, $(())$ and $()(())$ are correctly parenthesized strings because $(1+(1+1))$ and $(1+1)+(1+(1+1))$ are correct mathematical expressions, but $(()$ and $())(()$ are not correctly parenthesized strings.

# Task

You wrote the number $n$ and a string $S$ of characters belonging to the set $\\{ \\texttt{(}, \\texttt{)} \\}$ of length $n$.

Find $\\displaystyle{\\sum_{i=1}^{n} \\sum_{j=i}^{n} gcd(i, j) \\cdot rbs(i, j)}$

# Input data

The first line contains a single natural number representing the number $n$.

The second line contains a string of $n$ characters representing the string $S$.

# Output data

Print a single natural number representing the answer to the task.

# Constraints and clarifications

* $1 \\leq n \\leq 200 \\ 000$
* $gcd(i, j)$ is the [greatest common divisor](https://ro.wikipedia.org/wiki/Cel_mai_mare_divizor_comun) of the numbers $i$ and $j$.
* $rbs(i, j)$ is $1$ if the subarray $s_i \\ s_{i+1} \\ \\dots \\ s_j$ is correctly parenthesized, otherwise it is $0$.

|#|Points|Constraints|
|-|-|--------|
|1|6|$1 \\leq n \\leq 300$|
|2|11|$300 < n \\leq 3 \\ 000$|
|3|65|$3 \\ 000 < n \\leq 50 \\ 000$|
|4|18|No other constraints|

# Example

`stdin`
```
10
()()((()))
```
`stdout`
```
14
```

# Explanation

The subarrays with $gcd(i, j) = 1$ are: 

1. $(1, 2)$
2. $(1, 4)$
3. $(1, 10)$
4. $(3, 4)$
5. $(3, 10)$
6. $(7, 8)$

The subarray with $gcd(i, j) = 3$ is:

1. $(6, 9)$

The subarray with $gcd(i, j) = 5$ is:

1. $(5, 10)$

$6 \\cdot 1 + 1 \\cdot 3 + 1 \\cdot 5 = 14$

So the answer is $14$.