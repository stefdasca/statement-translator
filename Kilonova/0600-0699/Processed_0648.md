Sure, here is the translated text:

```
Given $P$, $N$, $T$ and $C$, as well as an array $a$ of $N$ natural numbers in base 10: $a_1$, $a_2, \cdots, a_N$.

A number is called $based$, if and only if when written in base $T$, the last digit of this number is $C$.
We will consider that the digits in base $T$ are $0$, $1$, $2, \cdots, T-2$, $T-1$. For instance, the digits in base 15 are: 0, 1, 2, $\cdots$ 14.

For example, if $T$ = 6 and $C$ = 4: $4$, $10$, $70$ are $based$, because the number 4 converted from base 10 to base 6 is 14, and its last digit is 4, the number 10 converted to base 6 is 14, and the last digit of 14 is 4, respectively the number 70, converted to base 6 is 154. Numbers $6$, $25$ and $44$ are not $based$ because $6$ = $10_6$, $25$ = $41_6$ and $44 = 112_{6}$, these have the last digit different from 4.

# Task

If $P = 1$, find how many $based$ numbers are in the array.

If $P = 2$, find how many pairs ($i$, $j$) exist such that $1 \leq i < j \leq N$ and $a_i$ + $a_j$ is $based$.

# Input data
The first line of the input file `bazat.in` contains four natural numbers $P$, $N$, $T$ and $C$ separated by a space. The second line contains $N$ natural numbers separated by a space, representing the array $a$.

# Output data

The first line of the output file `bazat.out` contains a natural number representing the answer to task 1 if $P = 1$, otherwise to task 2.

# Constraints and clarifications
* $P = 1$ or $P = 2$
* $1 \leq N \leq 100 \ 000$
* $2 \leq T$, $0 \leq C < T \leq 10^9$
* $0 \leq a_i \leq 10^9$, for any $1 \leq i \leq N$
* For 30 points $P = 1$
* For 20 points $P = 2$ and $N \leq 2 \ 000$
* For 30 points $P = 2$, $N > 2 \ 000$ and $T \leq 10^6$

# Example 1
`bazat.in`
```
1 7 6 4
10 154 6 25 94 44 70
```
`bazat.out`
```
4
```

# Example 2
`bazat.in`
```
2 7 6 2
10 154 6 25 94 44 70
```
`bazat.out`
```
7
```

# Explanations
In the first example, the $based$ numbers are $10, 154, 94, 70$.

In the second example, the pairs ($i$, $j$) are { ($1$, $2$); ($1$, $5$); ($1$, $7$); ($2$, $5$); ($2$, $7$); ($3$, $6$); ($5$, $7$)}.

These correspond to the sums {$164$, $104$, $80$, $248$, $224$, $50$, $164$}.
```