> Don't leave for tomorrow what you can do today, leave it for the day after tomorrow

Alice Elice challenged Bob Glob to a game. Alice Elice has two piles with $P_1$ and $P_2$ gifts. Before the game starts, Alice rolls a die with $N$ faces and notes the result as $K$. The game consists of the following stages:

At the beginning, if $K$ is even, she opens all the gifts from the first pile, and if $K$ is odd, she opens all the gifts from the second pile. In the following turns, the two alternately choose gifts, starting with Bob. The player must open between $1$ and $K$ gifts from the remaining pile. The player who cannot open at least one gift loses.

# Task

Alice wishes to have many gifts next year as well, so she wants to find out the probability of winning the game, **considering that both play optimally.**

# Input data

The first line contains $T$, the number of tests. The next $T$ lines contain $P_1$, $P_2$, and $N$.

# Output data

Print for each of the $T$ tests the chance of winning modulo $10^9 + 7$ (see below).

# Constraints and clarifications

* $0 \leq T \leq 10^3$
* $0 \leq P_1, P_2 \leq 10^9$
* $0 \leq N \leq 10^4$
* We assume that there is a die model with $N$ faces.
* If we express the probability of Alice winning through the ratio $\frac{a}{b}$, then you will display $a \cdot b^{-1} \text{ mod } (10^9 + 7)$, where $b^{-1}$ is the modular inverse of $b$, modulo $10^9+7$.
* **Both play optimally.**

| # | Score | Constraints | 
| - | ----- | ------------ |
| 1 | 10 | $N = 2$, $0 \leq P_1, P_2 \leq 3$ |
| 2 | 30 | $N = 6$, $0 \leq P_1, P_2 \leq 20$ |
| 3 | 60 | No additional constraints |

# Example

`stdin`
```
3
3 2 3
333625 453145 800
1 1 1
```

`stdout`
```
0
855000006
0
```

## Explanation
If the die value is $1$ then:
* The remaining pile is $1$ with $3$ gifts $\rightarrow$ Alice loses;

If the die value is $2$ then:
* The remaining pile is $2$ with $2$ gifts $\rightarrow$ Alice loses;

If the die value is $3$ then:
* The remaining pile is $1$ with $3$ gifts $\rightarrow$ Alice loses.