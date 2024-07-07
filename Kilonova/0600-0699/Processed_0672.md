
Seeking treasures of immense value to add to his almighty random knapsack, Prosto is travelling around the world. During one of his journeys he found a room filled with chests, each being locked. On every chest there is a boolean formula engraved on it. 

The boolean formulas are $\text{XOR}$ sums of multiple clauses, where a clause is the $\text{AND}$ sum of some literals, which can be negated.

Alongside the formula on the chest, there is engraved a number $k$, which represents the number of distinct literals which can appear in the given formula. The $i$-th literal is represented as the $i$-th lowercase letter of the English alphabet e.g. the first literal is 'a', the second literal is 'b' and so on. 

In order to unlock a chest you need to find the number of ways to assign each literal $0$ or $1$ such that the given formula evaluates to $1$.

Let's say we have a chest with $k=3$ variables and the following formula: $\text{(a AND b) XOR (b AND c) XOR (a AND c)}$. If the tuple of literals $(a,b,c)$ is equal to one of the following tuples: $(1,1,0)$, $(1,0,1)$, $(0,1,1)$, $(1,1,1)$ then the given expression is $1$, so the answer is $4$.

Our protagonist promises you glory and $100$ points if you can help him find the keys to some of his chests.

# Task

Given a number of chests, determine the number of valid keys for each chest.

# Input data

The first line of the input contains $T$, the number of chests.

For each chest you are given a number $k$ representing the number of literals, and a string $s$ which represents the formula written on the chest.

# Output data

The output will contain on $T$ lines the keys of the chests in the order they appear in the input.

# Constraints and clarifications

* $1 \leq T \leq 15$
* $1 \leq k \leq 14$
* $1 \leq |s| \leq 10^5$
* For tests worth $20$ points, $1 \leq k \leq 10$
* For tests worth $30$ more points, there aren't any negated literals
* For tests worth another $20$ points, $1 \leq k \leq 12$
* The scores from the contest might be different than the scores you get here

# Example

`stdin`
```
3
4
(c&d)^(!a&b&!c)^(b)
4
(!c)
4
(!c&!d)^(!a&c&!d)^(a&!b&c)
```

`stdout`
```
6
8
8
```
