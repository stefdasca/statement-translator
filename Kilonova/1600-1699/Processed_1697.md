Here is the translated text in English:

```markdown
Given $N$ natural numbers $a_1$, $a_2$, $\dots$, $a_N$ and a nonzero natural number $M$.

# Task

Determine the number of index pairs $(i, j)$, with $i < j$, with the property that the number $a_i \cdot a_j + a_i + a_j$ is divisible by $M$.

# Input data

The input file `prosum.in` contains on the first line the natural numbers $N$ and $M$, and on the next line the $N$ natural numbers $a_1, a_2, \dots a_N$, separated by spaces.

# Output data

The output file `prosum.out` will contain on the first line the number of index pairs $(i, j)$, with $i < j$, with the property that the number $a_i \cdot a_j + a_i + a_j$ is divisible by $M$.

# Constraints and clarifications

* $2 \leq N \leq 100\ 000$
* $0 \leq a_i \leq 10^{18}$; $\forall i \in \{1, 2, ..., n \}$
* $1 \leq M \leq 10^{17}$
* For tests worth $23$ points: $2 \leq N \leq 5\ 000$, $0 \leq a_i \leq 10^9$; $1 \leq M \leq 10^9$
* For other tests worth $13$ points: $2 \leq N \leq 1\ 000$
* For other tests worth $33$ points: $0 \leq a_i \leq 10^9$; $1 \leq M \leq 10^9$, and the numbers $a_i$ have at most $3$ digits equal to $1$ in their binary representation.
* For other tests worth $31$ points: there are no other restrictions.

# Example 1

`prosum.in`
```
4 13
6 15 6 1
```

`prosum.out`
```
2
```

## Explanation

There are two pairs of indices with the required property: $(1, 4)$ and $(3, 4)$, because we have $6 \cdot 1 + 6 + 1 = 13$, which is divisible by $M = 13$.
```
