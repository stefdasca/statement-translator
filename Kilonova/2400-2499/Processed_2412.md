Aurel was recently hired at Cernavodă. Since he does not know much about being an engineer, he is asking for your help in solving the following problem: he has various materials of different types arranged in a square area of size $N \times N$, divided into $N^2$ zones, each of $1 \text{ m}^2$. Formally, Aurel has a matrix $A$ with $N$ rows and $N$ columns, where element $A_{i, j}$ represents the type of material in the corresponding zone.

Aurel knows that the power emitted by the material at row $i$ and column $j$, $\text{power}(i, j)$, is equal to:
$$
\text{power}(i, j) = \left| \left\{ \left(k, l\right) |\ k \le i; l \le j; A_{i, j} = A_{k, l} \right\} \right|.
$$

# Task

Aurel wants to find out the total power emitted by the materials. Since he is not good at calculations or programming, he is asking for your help. Determine the sum of all powers emitted by the materials, namely
$$
\sum_{i = 1}^N \sum_{j = 1}^N \text{power}(i, j) .
$$

# Input data

The first line contains the natural number $N$. The next $N$ lines contain $N$ numbers each, where the $j$-th number on line $i + 1$ represents the type of material at row $i$ and column $j$.

# Output data

Print a single number, the sum of all powers emitted by the materials.

# Constraints and clarifications

* $1 \le N \le 2\ 000$;
* $1 \le A_{i, j} \le N^2, \forall i, j \in \left\{ 1, 2, ..., N \right\}$;
* For tests worth 33 points it is guaranteed that $N \le 300$;
* For the remaining 67 points, no additional constraints apply.

# Example 1

`stdin`
```
5
9 9 2 1 3
1 2 2 4 1
2 2 3 5 1
6 4 4 7 7
3 6 8 8 8
```

`stdout`
```
41
```

## Explanation

The image below illustrates the first test.
~[materiale.png|width=12cm|align=center]
The following table contains the power of each material:

|   |   |   |   |   |
|---|---|---|---|---|
| 1 | 2 | 1 | 1 | 1 |
| 1 | 1 | 3 | 1 | 3 |
| 1 | 3 | 1 | 1 | 4 |
| 1 | 1 | 2 | 1 | 2 |
| 1 | 2 | 1 | 2 | 3 |

# Example 2

`stdin`
```
1
1
```

`stdout`
```
1
