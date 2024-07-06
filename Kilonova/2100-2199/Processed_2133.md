```markdown
# Task

We are given the arrays $A$ and $B$ of $N$ values.
We will simulate the following algorithm using a new array $C$ of $N$ initially zero values.
For each $i$ from 1 to $N$, we add the value $B_i$ to all elements $C_j$ where $j = i + x * A_i$ and $j \leq N$.
What is the array $C$ at the end?

# Input data

The first line contains $N$.
The second line contains the array $A$.
The third line contains the array $B$.

# Output data

$N$ values, the array $C$.

# Constraints and clarifications

* $1 \leq N, A_i \leq 10^5$
* $1 \leq B_i \leq 10^9$

# Points:

* For $20p$ the raw input

# Example 1

`stdin`
```
5
2 1 2 3 100
1 4 2 3 5
```

`stdout`
```
1 4 7 7 12
```

## Explanation

The first element will add $1$ to the elements at indices $1$, $3$, $5$.
The second element will add $4$ to the elements at indices $2$, $3$, $4$, $5$.
The third element will add $2$ to the elements at indices $3$, $5$.
...

# Example 2

`stdin`
```
10
3 17 2 4 1 2 4 1 6 2
12 31 54 1 3 9 19 10 58 17
```

`stdout`
```
12 31 54 13 57 12 88 23 125 51 
```
```