Sure, here's the translated statement:

---

Xorin was walking on the street when he came across a sequence $u$ of $N$ natural numbers. Being curious, he wants to apply alchemical operations to each element in the sequence. The only alchemical operation he knows is "solve et coagula" (dissolve and coagulate), learned from an essay about Harap Alb. The "solve et coagula" procedure is as follows: take a natural number, for example, $84$, decompose it into prime factors ($84 = 2^2 \cdot 3 \cdot 7$), and the result is obtained from the xor sum of these prime factors, taken only once ($2 \oplus 3 \oplus 7 = 6$).

Xorin applies the "solve et coagula" procedure to each element in the sequence $u$, obtaining a new sequence $v$ (the element $u_i$ corresponds to the element $v_i$).

# Task

Roxana finds the new sequence $v$ and asks you a question: how many pairs of indices $(a, b)$, where $1 \leq a \leq b \leq N$, exist, with the property that the xor sum of the elements $v_i$, with $a \leq i \leq b$, is $0$?

# Input data

The first line contains the natural number $N$. The second line contains $N$ natural numbers, the elements of the initial sequence $u$.

# Output data

The output file will contain on the first line the number of pairs of indices $(a, b)$ with the specified property.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $2 \leq u_i \leq V$, for any $1 \leq i \leq N$.
* $1 \leq V \leq 10\ 000\ 000$
* Applying the procedure for the value $1$ will result in $0$.
* For tests worth $21$ points, $N \leq 1\ 000$ and $V \leq 1\ 000\ 000$.
* For tests worth $39$ points, $N \leq 40\ 000$ and $V \leq 10\ 000\ 000$.
* For tests worth $17$ points, $N \leq 200\ 000$ and $V \leq 10\ 000\ 000$ and all numbers are prime.
* For tests worth $23$ points, there are no additional constraints.
* The xor operation represents the exclusive disjunction operation. The table below represents the table of this operation, for 2 bits.
* In this problem, the xor operation is performed on the bits of the operands. For example, $5 \oplus 12 = 9$ ($0101_2 \oplus 1100_2 = 1001_2$).
* By the xor sum of $n$ numbers $x_i$, it is understood the result obtained by successively applying the xor operation to them: $x_1 \oplus x_2 \oplus \dots \oplus x_{n-1} \oplus x_n$.
* In C/C++, the operator for xor is `^`, and in Pascal, the corresponding operator is `xor`.

|$A$|$B$|$A \oplus B$|
|-|-|-|
|$0$|$0$|$0$|
|$0$|$1$|$1$|
|$1$|$0$|$1$|
|$1$|$1$|$0$|

# Example 1

`basme.in`
```
3
236 23 410
```

`basme.out`
```
1
```

## Explanation

$u_1 = 236$ has prime factors $2$ and $59$, so $v_1 = 2 \oplus 59 = 57$. $u_2 = 23$ is prime, so $v_2 = 23$. $u_3 = 410 = 41 \cdot 2 \cdot 5$, so $v_3 = 41 \oplus 2 \oplus 5 = 46$. Thus, the sequence $v$ is $[57, 23, 46]$. The only continuous subarray that has a xor sum of $0$ is $[57, 23, 46]$, so the answer is $1$.

# Example 2

`basme.in`
```
10
84 4 5 6 10 225 2 13 15 26
```

`basme.out`
```
3
```

## Explanation

The initial sequence $u$ transforms into the following sequence $v$: $[6, 2, 5, 1, 7, 6, 2, 13, 6, 15]$. The subarrays $[6, 2, 5, 1]$, $[5, 1, 7, 6]$ and $[7, 6, 2, 13, 6, 15]$ have a xor sum of $0$. Thus, for this sequence, there are $3$ pairs of indices that respect the given property: $(1, 4)$, $(3, 6)$ and $(5, 10)$.

---

Please review the statement and let me know if there are any errors or if you need further assistance!