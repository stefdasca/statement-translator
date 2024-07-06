```markdown
# Task

A superbet has appeared in CrackLand. In this superbet, there are $N$ machines: one trickery machine $1$, one trickery machine $2$, ... one trickery machine $N$.

We are professionals but have been cursed by the plug. The curse says that if we play at time $i$ on trickery machine $i$, we will definitely lose; otherwise, we will win at any machine (because we are professionals).

We take the machines in any order we want. In how many ways can we take them in a row so that the gain is maximized?

# Input data

The first line contains $N$.

# Output data

Print the number of required ways modulo $10^9+7$.

# Constraints and clarifications

* $1 \leq N \leq 10^6$;
* The result is tripled modulo $10^9+7$.

# Example 1

`stdin`
```
3
```

`stdout`
```
2
```

## Explanation

We can play in the following ways:
$(1,2,3)$ - we do not win at all.
$(1,3,2)$ - we win on the second and third machine.
$(2,1,3)$ - we win on the first and second machine.
$(2,3,1)$ - we win on all machines.
$(3,1,2)$ - we win on all machines.
$(3,2,1)$ - we win on the first and third machine.

We can win on a maximum of $3$ machines at a time, $2$ of these configurations have the maximum gain.

# Example 2

`stdin`
```
11
```

`stdout`
```
14684570
```
```