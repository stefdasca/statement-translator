*Boulders and pebbles, let's smash the table with them.*

The two friends, Chip and Adar, play using special stones as follows: Chip has $N$ pebbles, each with a weight and a resistance, and he stacks them in order, forming a vertical tower. Over a pebble with resistance $R$ other pebbles can only be placed if the sum of their weights is strictly less than $R$; otherwise, the pebble will break. If at any point there are multiple pebbles that could break, then all of them will break at the same time.

# Task
Given $N$ triplets of the form $(G, R, X)$, with the following meaning: a pebble with weight $G$ and resistance $R$ is added to the existing tower, guaranteeing that none of the previously placed stones will break. Adar must tell Chip what is the minimum weight a new pebble should have so that, if placed on top of the tower, it would break at least $X$ pebbles.

# Input data
The file `pitricele.in` will contain on the first line a natural number $N$. The next $N$ lines will contain the $N$ triplets $(G_i, R_i, X_i)$. The triplet $(G_i, R_i, X_i)$ will be encoded on line $i + 1$ as $(G_i\\text{ xor }V_{i-1}, R_i\\text{ xor }V_{i-1}, X_i\\text{ xor }V_{i-1})$ where $V_i$ denotes Adar's answer to Chip after he has placed the $i$-th pebble.

# Output data
The file `pitricele.out` will contain $N$ lines, containing Adar's answers, in chronological order, one per line.

# Constraints and clarifications
* $1 \leq N \leq 100\ 000$
* $1 \leq G_i, R_i \leq 1\ 000\ 000\ 000$
* $1 \leq X_i \leq i$

# Example
`pitricele.in`
```
3
3 4 1
6 12 5
3 5 3
```
`pitricele.out`
```
4
2
1
```
Explanation
---
The original triplets are:
$(3\ 4\ 1)$  
$(2\ 8\ 1)$  
$(1\ 7\ 1)$