
# Task

Given a natural number $Q$ and $Q$ natural numbers $x$, each can undergo an arbitrary number of transformations. A transformation consists of the following types of operations:

* Addition or multiplication by $2$ ($x \leftarrow x + 2$ or $x \leftarrow x \cdot 2$);
* Addition or multiplication by $3$ ($x \leftarrow x + 3$ or $x \leftarrow x \cdot 3$);
* Addition or multiplication by $5$ ($x \leftarrow x + 5$ or $x \leftarrow x \cdot 5$);
* Addition or multiplication by $7$ ($x \leftarrow x + 7$ or $x \leftarrow x \cdot 7$).

For each of the $Q$ given numbers, determine the minimum number of transformations required so that the sum of the digits of the resulting number is divisible by $9$.

# Input Data

The first line contains a natural number $Q$. The next $Q$ lines each contain a natural number $x$.

# Output Data

On line $i$, print the minimum number of transformations applied to the $i$-th number.

# Constraints and Clarifications

* $1 \leq Q \leq 10^{5}$;
* $1 \leq x \leq 10^{18}$;
* For tests worth $70$ points, $1 \leq x \leq 10^9$;
* For other tests worth $30$ points, there are no additional constraints.

# Example

`stdin`
```
3
4
9
23895793
```

`stdout`
```
1
0
2
```

## Explanation

For $x = 4$, it can be increased by $5$, resulting in $9$.
For $x = 9$, it already has a sum of digits divisible by $9$.
For $x = 23895793$, two transformations are applied:
1. $x \leftarrow x + 2$, which makes it equal to $23895795$;
2. $x \leftarrow x \cdot 3$, making it equal to $71687385$, which has a digit sum of $45$.
