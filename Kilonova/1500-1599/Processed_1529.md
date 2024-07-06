Two sequences $D = (D_1, D_2, ..., D_n)$ and $E = (E_1, E_2, ..., E_n)$ are given, which represent the prime factorization of a nonzero natural number $X$ as follows: $D_i$ – the prime factor, $E_i$ – the power of the prime factor $D_i$ in the factorization of $X$ ($1 \leq i \leq n$), where $n$ represents the number of prime factors.

# Task

Determine:

1. The total number of natural divisors of $X$
2. The divisors of $X$ that belong to the interval $[A, B]$, where $A$ and $B$ are given natural numbers.

# Input data

The input file `descmult.in` contains:
- The first line contains a natural number $C$ which represents the task to be solved ($C = 1$ or $C = 2$).
- The second line contains three natural numbers $n \ A \ B$, separated by spaces, with the significance given in the statement.
- The third line contains $n$ natural numbers, separated by spaces, representing the prime factors $D_1 \ D_2 \ ... \ D_n$ of $X$.
- The fourth line contains $n$ natural numbers, separated by spaces, representing the powers of these factors $E_1 \ E_2 \ ... \ E_n$.

# Output data

For $C = 1$, only the first task will be solved. In this case, the output file `descmult.out` will contain on the first line a single nonzero natural number representing the total number of natural divisors of $X$.
For $C = 2$, the second task will be solved. In this case, the output file `descmult.out` will contain, separated by spaces, the divisors of $X$ that belong to the interval $[A, B]$.

# Constraints and clarifications

* $2 \leq n \leq 20$
* $1 \leq A \leq B \leq {10}^{7}$
* $2 \leq D_i < 1 \ 000$ (distinct prime numbers), $1 \leq i \leq n$
* $1 \leq E_i \leq 10$, $1 \leq i \leq n$
* The prime factors $D_1, D_2, ..., D_n$ are not necessarily in ascending order
* It is guaranteed that the maximum number of natural divisors of $X \leq {10}^{19}$
* The interval $[A, B]$ contains at least one divisor
* The maximum number of divisors in the interval $[A, B]$ is $\leq {10}^{6}$
* **The order of displaying the divisors is not important**
* For the correct solution of task $1$, $20$ points are awarded, and for the second task, $80$ points are awarded.

# Example 1

`descmult.in`
```
1
4 30 50
3 2 5 11
1 3 2 1
```

`descmult.out`
```
48
```

## Explanation

For this test, task $1$ is solved.
$X = {3}^{1} \cdot {2}^{3} \cdot {5}^{2} \cdot {11}^{1} = 6600$ and has $48$ divisors: $1$, $2$, $3$, $4$, $5$, $6$, $8$, $10$, $11$, $12$, $15$, $20$, $22$, $24$, $25$, $30$, $33$, $40$, $44$, $50$, $55$, $60$, $66$, $75$, $88$, $100$, $110$, $120$, $132$, $150$, $165$, $200$, $220$, $264$, $275$, $300$, $330$, $440$, $550$, $600$, $660$, $825$, $1100$, $1320$, $1650$, $2200$, $3300$, $6600$.

# Example 2

`descmult.in`
```
2
4 30 50
3 2 5 11
1 3 2 1
```

`descmult.out`
```
30 44 50 40 33
```

## Explanation

For this test, task $2$ is solved.
$X = {3}^{1} \cdot {2}^{3} \cdot {5}^{2} \cdot {11}^{1} = 6600$.
The divisors that belong to the interval $[30, 50]$ are: $30, 33, 40, 44, 50$. The order of displaying the divisors is not important.