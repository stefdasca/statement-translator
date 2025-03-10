# Task

In Jump Civilization, the world is represented by $N$ floating islands, numbered from $1$ to $N$. Once at island $i$ (for $1 \leq i < N$), members of the Jump Civilization can perform:

* a light jump, from island $i$ to island $i + 1$; or
* a difficult jump, from island $i$ to island $v_i$, where $i < v_i \leq N$.

To advance the Jump Civilization, its members need to calculate the _jump power_ of each island. The jump power of island $i$ is the number of islands you can reach if you start at island $i$ and use at most $K$ jumps.

The previous _Jump Champion_, in trying to ensure that the jump route is fair, established the following important rule: Whenever $1 \leq i < j \leq N$, either $v_i \leq j$ or $v_j \leq v_i$. You, as an aspiring member of the Jump Civilization, want to find the jump power of each island — can you do this efficiently?

# Input data

The first line of the input contains two space-separated integers $N$, $K$. The second line of the input contains $N - 1$ space-separated integers $v_1, \dots , v_{N-1}$.

# Output data

Print $N$ space-separated integers, the jump power of the islands in order.

# Constraints and clarifications

* $1 \leq N \leq 300 \ 000$
* $1 \leq K \leq N - 1$
* $i < v_i \leq N$
* For $1 \leq i < j \leq N$, either $v_i \leq j$ or $v_j \leq v_i$.
* If island $j$ can be reached from island $i$ in two different ways using at most $K$ jumps, then the island will be counted only once in the jump power of island $i$.
* For computing the jump power of an island, it does not matter whether we use light or difficult jumps — only the number of jumps matters.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 6      | $N \leq 2 \ 000$ |
| 2 | 27      | $N \leq 100 \ 000$ and $K \leq 50$      |
| 3 | 11      | $v_i \leq i + 2$ for $1 \leq i < N$      |
| 4 | 37      | $N \leq 100 \ 000$     |
| 5 | 19      | No additional constraints      |

# Example 1

`stdin`
```
5 1
4 3 4 5
```

`stdout`
```
3 2 2 2 1
```

## Explanations

From island $1$, you can reach island $1$ without jumping, and islands $2$ and $4$ with $1$ jump. In total, the jump power of island $1$ is $3$.

# Example 2

`stdin`
```
6 2
2 3 5 5 6
```

`stdout`
```
3 4 4 3 2 1
