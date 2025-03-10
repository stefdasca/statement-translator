# The Shortest Bear-Free Path

Let's imagine a "mountain" formed from $n$ levels ($i=1, 2, \ldots, n$), where each level is represented by a binary matrix $m \times m$. In each matrix, the values of $1$ indicate points that are part of the mountain, whereas the values of $0$ form the areas outside the mountain. It is known that both groups of $1$s and $0$s are connected, considering that two elements are neighbors if they share a side.

Furthermore, the levels of the mountain are "concentric," meaning that the positions with $1$ on level $i$ ($i=2, \ldots, n$) are covered by the $1$s on level $i-1$. In the matrix on the last level, there is a single $1$, which represents the top of the mountain.

Since the points inside each level are considered dangerous as they could be areas frequented by bears, we aim to follow this strategy:
* Start from any point on the edge of level $0$;
* For each level, traverse from the edge of the current level to the edge of the next level with the fewest steps, and on the last level, reach the top;
* Traversing the edges is considered safe because bears do not approach them due to fear of heights, whereas passing through interior areas is considered dangerous.

# Task

Determine how many dangerous steps must be taken to reach from the base of the mountain to the top, following the described strategy.

# Input data

* The first line of the input file `medve.in` contains an integer $t$ - the number of test cases.
* The first line of each test contains two integers $n$ and $m$ - the number of levels and the size of the matrices.
* The next $n \cdot m$ lines contain $m$ binary values, separated by spaces, representing the matrix elements.

# Output data

* For each test, print on a separate line in `medve.out` the total number of dangerous steps.

# Constraints and clarifications

* $1 \leq t \leq 3$
* $1 < n < 100$;
* $3 < m < 100$;

# Example

`medve.in`
```
1
3 10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 0
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 1 1 1 0 0
0 0 0 0 1 1 1 1 0 0
0 0 0 1 1 1 1 1 0 0
0 0 0 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

`medve.out`
```
2
```

## Explanation

The input example consists of a single test case ($t=1$), which represents a mountain formed from 3 levels, encoded by $10 \times 10$ matrices. On the first level, there is a single dangerous step to reach the edge of level 2 ($[3,9]\rightarrow[3,8]$). On level 2, another dangerous step is required to reach the position of the peak on level 3 ($[5,5]\rightarrow[5,6]$).