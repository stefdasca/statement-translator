Here's the translated and adapted version of your problem statement:

---
Spring is coming and in order to please the Buntopian kids, you decided to buy for them many balls of different types, namely $n$ types of balls.

For the first game, you asked them to arrange all the balls in such a way that among all the possible arrangements of balls, the sum of subarray beauties is as small as possible.

For a given arrangement, the sum of subarray beauties is computed in the following way:

We compute all the maximal subarrays consisting of balls having the same color and then for each of them, we add up to the answer $2^x$, where $x$ is the length of the subarray.

For example, if we have the array $[2, 2, 4, 1, 1, 3, 3, 3]$, the sum of beauties will be $4 + 2 + 4 + 8 = 18$.

Since Buntopian kids are some of the best kids at math from the entire universe, in order to challenge them, now you ask them to compute some of these values during the next $q$ days, while considering potential changes in the number of balls from the gift as well. However, since the values are too big, they are only asking for the remainder of the answer when dividing by $10^9 + 7$.

Can you repeat Buntopian kids' achievement?

# Task

# Input data

The first line of the input contains $n$ and $q$, the number of types of balls and the number of queries $(1 \leq n, q \leq 2 \cdot 10^5)$.

The next line of the input contains the $n$ numbers, representing the initial quantities of each type of ball $(1 \leq v_i \leq 10^9)$.

The next $q$ lines contain the queries, which are of two types:

`1 a b`: The number of balls of type $a$ becomes $b$ ($1 \leq b \leq 10^9$).

`2 x y`: Buntopian kids now want to know the answer for the problem, if we only consider types of balls in range $[x, y]$.

For tests worth $20$ points, $(1 \leq n, q \leq 1 \ 000)$.

# Output data

The output will contain one line for each query of type `2`, representing the answer asked by Buntopian kids modulo $10^9 + 7$.

# Example

`stdin`
```
7 6
4 2 18 5 7 9 3
2 2 4
1 5 19
2 1 7
2 3 6
1 2 106
2 1 7
```

`stdout`
```
54
120
102
328
```
---

Double-checking for grammar and syntax errors:

- The task explanation is clear and unambiguous.
- The mathematical notation is retained accurately.
- The input and output descriptions are correctly translated.
- Examples provided are consistent with the problem statement.
