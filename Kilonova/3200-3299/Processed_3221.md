
# Task

Given an integer $Q$ and then $Q$ queries of the form $(a, b, c, d, s, t)$ as integers. Determine the number of integer pairs $(x, y)$ that simultaneously satisfy the conditions:
* $\\frac{a}{b} \\leq \\frac{x}{y} \\leq \\frac{c}{d}$
* $s \\leq y \\leq t$

# Input data

The first line contains an integer $Q$. Each of the next $Q$ lines contains $6$ integers $a$, $b$, $c$, $d$, $s$, and $t$, representing the queries.

# Output data

On line $i$, print the answer to the $i$-th query.

# Constraints and clarifications

* $1 \\leq Q \\leq 10^5$;
* $1 \\leq a, b, c, d \\leq 100$;
* $1 \\leq s, t \\leq 10^7$;
* It is guaranteed that $s \\leq t$ and $\\frac{a}{b} \\leq \\frac{c}{d}$ for any query;
* For tests worth $19$ points, $t - s \\leq 10^3$;
* For other tests worth $45$ points, $s$ and $t$ are divisible by the least common multiple of $b$ and $d$;
* For other tests worth $36$ points, there are no additional constraints.

# Example

`stdin`
```
2
1 5 2 3 1 3
3 10 7 2 8 9
```

`stdout`
```
3
55
```

## Explanation

For the first example, the pairs $(x, y)$ that satisfy the task condition are $(1, 2); (1, 3); (2, 3)$, because $\\frac{1}{5} \\leq \\frac{1}{2}, \\frac{1}{3}, \\frac{2}{3} \\leq \\frac{2}{3}$, and $1 \\leq y \\leq 3$ for each pair.

For the second example, you will have to trust us.
