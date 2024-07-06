The Blue Army has been tasked with protecting the legendary dragon cubes. To make their job easier, they have been given two magical rings with the ability to fuse the fighters who wear them. When $2$ fighters fuse, the resulting fighter's power is equal to the sum of the two initial powers, plus their product. Formally, if the two fighters have powers $a$ and $b$ respectively, then after fusion, they will have the power $a + b + a * b$. General Abelius needs your help to test the blue army's power.

# Task

You are given an array consisting of $N$ natural numbers representing the powers of the blue army fighters, and $Q$ queries each consisting of a pair of natural numbers $s_i$ and $d_i$. You are asked to determine the power of the fighters in the interval $[s_i, d_i]$, if they were to fuse using the magical rings. The fusion is done in the order of the indices, from left to right: the two leftmost fighters fuse, then the result fuses with the 3rd one, and so on.

# Input data

The first line of the input file `fuziune.in` contains $2$ numbers $N$ and $Q$ representing the number of fighters in the blue army, and respectively the number of queries from General Abelius.
The second line contains $N$ natural numbers $a_i$, each representing the power of the fighter at position $i$.
The next $Q$ lines contain $Q$ pairs of natural numbers $s_i$ and $d_i$, one pair per line, representing the ends of the interval for the $i$-th query.

# Output data

The output file `fuziune.out` will contain $Q$ numbers, each on a new line, the $i$-th number representing the answer to the $i$-th query. Since the result can be very large, it must be displayed modulo $10^9+7$.

# Constraints and clarifications

* $1 \leq N, Q \leq 1\ 000\ 000$;
* $1 \leq s_i \leq d_i \leq N$;
* $1 \leq a_i \leq 1\ 000\ 000\ 000$;

|#|Score|Constraints|
|-|-|--------|
|1|15|$1 \leq N, Q \leq 5\ 000$|
|2|25|$1 \leq N, Q \leq 50\ 000$|
|3|30|$1 \leq N, Q \leq 500\ 000$|
|4|30|$1 \leq N, Q \leq 1\ 000\ 000$|

# Example 1

`fuziune.in`
```
10 5
2 5 7 3 1 3 5 6 9 2
1 4
3 5
8 10
5 5
4 7
```

`fuziune.out`
```
575
63
209
1
191
```

## Explanation

For the first query, we start with the interval $[1, 4]$, consisting of the elements $\{2, 5, 7, 3\}$.
First fusion: $2 + 5 + 2 * 5 = 17$.
The elements in the interval become $\{17, 7, 3\}$.
Second fusion: $17 + 7 + 17 * 7 = 143$.
The elements become $\{143, 3\}$.
Third fusion: $143 + 3 + 143 * 3 = 575$.
The result for the first query is $575$.