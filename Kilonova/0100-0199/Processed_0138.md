In the land of ONI, there are `N` kingdoms connected by `M` bidirectional edges. It is guaranteed that it is possible to travel from any kingdom to any other kingdom using these edges. These kingdoms want to form alliances among themselves and will use border points to achieve this.

Each edge `i`, where `1 \\leq i \\leq M`, has an associated natural number $c_i$ representing the cost of constructing a border point on it. Moreover, each kingdom `i`, where `1 \\leq i \\leq N`, has an associated natural number $r_i$ representing the cost of constructing a border point at its entrance.

For kingdom `X` to form an alliance with kingdom `Y`, where `1 \\leq X, Y \\leq N, X \neq Y`, it has two options:
* Constructs a border point on a *single* edge `i` with cost $c_i$ such that *every* path from `X` to `Y` passes through this border point;
* Constructs a border point at the entrance of its own kingdom (kingdom `X`) with cost $r_X$.

Obviously, kingdom `X` will choose the *minimum* cost to form an alliance with kingdom `Y`. We denote this minimum cost by `Cost(X, Y)`. **Note**, the cost for kingdom `X` to form an alliance with kingdom `Y` might be different from the cost for kingdom `Y` to form an alliance with kingdom `X`!

For kingdom `X` to be in a *perfect alliance*, it must form alliances with all other kingdoms.

**Note** that in forming an alliance, the border points constructed in forming other alliances are not considered. In other words, `Cost(X, Y)` is calculated independently for each pair `(X, Y)`!

# Task
For each kingdom, you must calculate the cost that it must pay to be in a perfect alliance. In other words, for each kingdom `i`, where `1 \\leq i \\leq N`, you must calculate $ \\sum _{j=1,j \\ne i} ^N \\text{Cost}(i, j)$.

# Input data
The input file `regate.in` will contain `N` and `M`, the number of kingdoms and the number of bidirectional edges, respectively, on the first line. The second line contains the numbers $r_1, ..., r_N$ separated by spaces, where $r_i$ represents the cost of constructing a border point at the entrance of kingdom `i`. The next `M` lines contain three natural numbers $a_i, b_i, c_i$ separated by spaces, `1 \\leq i \\leq M`, indicating that there is a bidirectional edge between kingdom $a_i$ and kingdom $b_i$, and $c_i$ represents the cost of constructing a border point on edge `i`.

# Output data
The output file `regate.out` will contain N lines. Each line `i` will contain a single integer, representing the cost that must be paid for kingdom `i` to be in a perfect alliance, in other words, $ \\sum _{j=1,j \\ne i} ^N \\text{Cost}(i, j)$.

# Constraints and clarifications
* `1 \\leq N \\leq 200 \ 000`
* `1 \\leq M \\leq 200 \ 000`
* $1 \\leq c_i \\leq 10^9$
* $1 \\leq r_i \\leq 10^9$
* $1 \\leq a_i, b_i \\leq N, a_i \\neq b_i$ (i.e., there is no edge from a kingdom to itself)
* There can be at most one edge between two kingdoms

## Subtask 1 (5 points)
* `N \\leq 2000` and `M = N - 1`, and the kingdoms and edges will form a chain in the order `1, 2, ..., N`
## Subtask 2 (10 points)
* `N \\leq 200` and `M \\leq 400`
## Subtask 3 (20 points)
* `N \\leq 2000` and `M \\leq 2000`
## Subtask 4 (10 points)
* All numbers in the `c` sequence are equal
## Subtask 5 (35 points)
* `M = N - 1`
## Subtask 6 (20 points)
* No additional constraints

# Examples

`regate.in`

```
5 5
8 13 9 7 12
1 2 10
2 3 10
3 4 10
4 5 10
1 3 10
```

`regate.out`

```
32
46
36
28
40
```

Explanation
---

For example, for kingdom `2` we have:
`Cost(2, 1) = 13`
`Cost(2, 3) = 13`
`Cost(2, 4) = 10`
`Cost(2, 5) = 10`

The sum of these costs is `46`.

Note that, for example, in calculating `Cost(2, 1)`, we cannot place a border point on edge `(1, 2)` with cost `10`, because there exists a path `2 \rightarrow 3 \rightarrow 1` that does not pass through edge `(1, 2)`.