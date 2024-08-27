## Task

In distant lands, there was a high mountain with many villages surrounding it. The $N$ villages are connected by $M$ bidirectional roads with positive integer lengths of at most $10^9$. Interestingly, the villagers did not build more than one road between any two pairs of villages and never built a road that starts and ends in the same village. The legendary hiker, Artskjid, began to explore these villages. Of course, it was easy for him to find the lengths of the shortest paths between any pair of villages. However, now he wants to pursue a new challenge. For $Q$ pairs of villages $(x, y)$, and an integer $p$ from $\{0, 1\}$, he wants to know if there is a chain (not necessarily simple - that is, it can visit nodes or edges multiple times) from $x$ to $y$ of length $l$ such that $l \mod 2 = p$.

## Input data

The input file `hiking.in` will contain on the first line three positive integers $N$, $M$, $Q$ which represent the number of villages, the number of roads, and the number of queries.

The next $M$ lines will contain three positive integers $a$, $b$, $c$ which represent that there is a bidirectional road of length $c$ between the villages $a$ and $b$.

The last $Q$ lines will contain three integers $x$, $y$, $p$ which represent a query regarding the villages $(x, y)$ and the parity of the road length $p$.

## Output data

The output file `hiking.out` must contain $Q$ lines, which describe the answers for the given queries (in order). The answer is $1$ if Artskjid can find a road with the given parity length between the given nodes and $0$ otherwise.

## Constraints and clarifications

$1 \leq N \leq 100\,000$

$1 \leq M \leq 200\,000$

$1 \leq Q \leq 100\,000$

## Example

`hiking.in`:
```
4 4 3
1 2 1
2 3 2
3 4 1
1 4 5
1 2 0
2 3 0
3 4 1
```

`hiking.out`:
```
1
1
1
```