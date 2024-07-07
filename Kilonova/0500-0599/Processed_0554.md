
Consider a sequence of $n$ non-zero natural numbers $a = (a_1 a_2 \dots a_n)$. Two numbers that are in consecutive positions in the sequence ($a_i$ and $a_{i+1}$, where $1 \leq i < n$) can merge if they have at least one common divisor greater than $1$. As a result of merging, they will be replaced by the smallest number that is divisible by all the divisors of $a_i$ and $a_{i+1}$. The merging operation can be repeated on the newly obtained sequence until there is no pair of numbers in consecutive positions that can merge. Let $b$ be the sequence obtained after performing all possible merging operations.

We define the *merging coefficient* of sequence $b$ and denote it by $cf(b)$ as a non-zero number such that any term of sequence $b$ has at least one common divisor with $cf(b)$, strictly greater than $1$. Additionally, $cf(b)$ must satisfy the following conditions:
1. Its prime factors are distinct (for example, $30 = 2 \cdot 3 \cdot 5$ has only distinct prime factors, but $18 = 2 \cdot 3 \cdot 3$ does not have only distinct prime factors);
2. Any prime factor of $cf(b)$ is a prime factor of at least one number in sequence $b$;
3. The list of distinct prime factors of $cf(b)$, strictly ordered in ascending order, is minimal lexicographically.

# Task
Given a sequence of non-zero natural numbers, write a program that solves the following two tasks:
1. Determine the minimal length of sequence $b$ obtained after performing all possible merging operations;
2. Determine $cf(b)$.

# Input data
The input file `fuziune.in` contains on the first line the task $C$ that needs to be solved ($1$ or $2$). The second line contains a natural number $n$, representing the number of values in the sequence. The following $n$ lines contain the $n$ numbers in the sequence, one number per line.

# Output data
The output file `fuziune.out` will contain a single line with the answer to task $C$ from the input file.

# Constraints and clarifications
* $1 \leq n \leq 100 \ 000$;
* $2 \leq a_i \leq 2 \cdot 10^9$, for any $1 \leq i \leq n$;
* It is guaranteed that the number of distinct prime factors for the numbers in sequence $b$ (for task $1$) and for $cf(b)$ (for task $2$) is at most equal to $250$.
* Let $d = (d_1 < d_2 < \dots < d_k)$ and $f = (f_1 < f_2 < \dots < f_h)$ be two lists of distinct prime factors strictly ordered in ascending order. We say that $d$ is lexicographically smaller than $f$ if there exists a position $i$ such that $d_j = f_j$, for any $1 \leq j < i$ and ($d_i < f_i$ or $i = k + 1$).

|# | Score | Constraints|
| - | - | ---------- |
| 1 |15 | $C = 1$, $1 \leq n \leq 1 \ 000$ and the numbers in the sequence are $\leq 10^4$. |
| 2 |15 | $C = 1$, $10 \ 000 \leq n \leq 100 \ 000$ and the numbers in the sequence are $\leq 10^4$. |
| 3 |10 | $C = 1$, $1 \leq n \leq 1 \ 000$ and the numbers in the sequence are $\leq 2 \cdot 10^9$. |
| 4 |30 | $C = 1$, $10 \ 000 \leq n \leq 100 \ 000$ and the numbers in the sequence are $\leq 2 \cdot 10^9$. |
| 5 |12 | $C = 2$ and the result will be a number with a maximum of $18$ digits. |
| 6 |18 | $C = 2$ and the result will be a number with a maximum of $1500$ digits. |

## Example 1

`fuziune.in`
```
1
8
30
18
997
121
625
5
55
101
```

`fuziune.out`
```
4
```

## Explanation
$C = 1$.
The numbers $30 = 2 \cdot 3 \cdot 5$ and $18 = 2 \cdot 3^2$ will merge and get the value $90 = 2 \cdot 3^2 \cdot 5$.
The numbers $625$, $5$ and $55$ will also merge, then the result will merge with $121$ and get the value $75625 = 5^4 \cdot 11^2$.
In the resulting sequence, there will remain, after performing all the merges, $4$ numbers ($90$, $997$, $75625$ and $101$).

## Example 2

`fuziune.in`
```
2
3
16
18
25
```

`fuziune.out`
```
30 
```

## Explanation

$C = 2$.
After performing all possible merging operations, the sequence is obtained:
$144 = 2^4 \cdot 3^2$
$25 = 5^2$
$cf(b) = 2 \cdot 3 \cdot 5 = 30$.

## Example 3

`fuziune.in`
```
2
8
30
18
97
121
625
5
55
10403
```

`fuziune.out`
```
3233010
```

## Explanation

$C = 2$.
After performing all possible merging operations, the sequence is obtained
$90 = 2 \cdot 3^2 \cdot 5$
$97$
$75625 = 5^4 \cdot 11^2$
$10403 = 101 \cdot 103$
$cf(b)=2 \cdot 3 \cdot 5 \cdot 11 \cdot 97 \cdot 101 = 3233010$.
