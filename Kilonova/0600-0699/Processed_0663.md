
Given the numbers $P$, $m$, $n$, $k$, and two arrays: $b_1, b_2, \dots b_m$ and $a_0, a_1, \dots a_{n-1}$ of natural numbers. Array $v_0, v_1, \dots , v_{n-1}$ is formed by traversing the elements of $a$ in steps of $k \pmod{n}$, starting from position 0.

Each number in $v$ is replaced by the closest power with a natural exponent of an element from $b$. If a number is at the same distance from two powers, the smaller value is chosen. For example, if $b = [2, 3]$, the powers of elements in the array $b$ are: $1, 2, 4, 8, 16, \dots, 1, 3, 9, 27, 81, \dots$.

# Task

1. If $P = 1$, find the sum of the values in array $v$ after the replacements.
2. If $P = 2$, when the number is smaller than the chosen power, it will be replaced with the opposite of the chosen power (For example, instead of 5 it would be -5). Then calculate $S$, by traversing the elements of $v$ in order ($0, 1, 2, \dots n-1$) and applying the formula ```S=((S*k+v[i])%n+n)%n```. Initially, $S$=0.

# Input data

The first line of the file `abmnk.in` contains $P$. The second line contains the numbers $m$, $n$ and $k$, in this order, separated by a space. The third line contains the array $b_1, b_2, \dots b_m$ of natural numbers greater than or equal to 2, separated by a space. The fourth line contains the array $a_0, a_1, \dots a_{n-1}$ of natural numbers separated by a space.

# Output data

The first line of the output file `abmnk.out` will contain a single integer, the answer to task $P$.

# Constraints and clarifications
* It is guaranteed [gcd](https://en.wikipedia.org/wiki/Greatest_common_divisor) $(n, k) = 1$.
* $ 1 \le m \le 1\ 000$
* $ 1 \le k < n \le 1\ 000\ 000$
* The numbers in the input file are less than or equal to $10^9$

# Subtasks

|#|Points|Constraints|
|-|-|--------|
|1|11|$P = 1, 1 \leq k < n \leq 1\ 000, 1 \leq m \leq 100$|
|2|18|$P = 1, 1 \leq k < n \leq 1\ 000\ 000, 1 \leq m \leq 1\ 000$|
|3|12|$P = 2, 1 \leq k < n \leq 10\ 000, 1 \leq m \leq 9$|
|4|7|$P = 2, 1 \leq k < n \leq 100\ 000, 1 \leq m \leq 9$|
|5|52|$P = 2, 1 \leq k < n \leq 1\ 000\ 000, 1 \leq m \leq 9$|

# Example 1

`abmnk.in`
```
1
5 15 4
2 32 10000 17 3
5 16 289 57 32 27 70 1 10000000 100000000 4 90 81 1024 531441
```

`abmnk.out`
```
108921736
```

## Explanation
We traverse from 4 to 4 and obtain $V = \{\texttt{5}$ , $\texttt{32}$ , $\texttt{10000000}$ , $\texttt{81}$ , $\texttt{16}$ , $\texttt{27}$ , $\texttt{100000000}$ , $\texttt{1024}$ , $\texttt{289}$ , $\texttt{70}$ , $\texttt{4}$ , $\texttt{531441}$, $\texttt{57}$ , $\texttt{1}$ , $\texttt{90}\}$

# Example 2

`abmnk.in`
```
2
5 15 4
2 32 10000 17 3
5 16 289 57 32 27 70 1 10000000 100000000 4 90 81 1024 531441
```

`abmnk.out`
```
8
```

## Explanation
In the end, $V = \{\texttt{4}$ , $\texttt{32}$ , $\texttt{8388608}$ , $\texttt{81}$ , $\texttt{16}$ , $\texttt{27}$ , $\texttt{100000000}$ , $\texttt{1024}$ , $\texttt{289}$ , $\texttt{64}$ , $\texttt{4}$ , $\texttt{531441}$ , $\texttt{-64}$ , $\texttt{1}$ , $\texttt{81}\}$
