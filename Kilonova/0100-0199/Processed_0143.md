Ana received a tree with `N` nodes with the root at node `1`, where each node has an associated natural value from `1` to `M`. For each node, she will write a string formed from the values of the nodes on the path from the root to that node, in order. Then, she will sort the `N` strings lexicographically.

After obtaining the sorted strings, Ana thinks of a string `S` formed from `K` natural numbers also between `1` and `M`, and asks Portocal if there is at least one string equal to `S`. Since Portocal is a lazy cat, he will check one string per day, starting with the first in the sorted order, until he finds one equal to `S`.

Portocal noticed that some nodes in the tree do not yet have an associated value, so he plans to assign values to these nodes (also between `1` and `M`) before Ana starts writing the strings. His goal is to find the string `S` as quickly as possible. To decide how to complete the missing values in the tree, he needs the answer to two questions:
1. The minimum number of days in which Portocal can find the string `S`
2. The number of ways he can complete the missing values in the tree to achieve that minimum number of days. Since this number can be very large, he is satisfied with the remainder when divided by `1 000 000 009`.

Obviously, Portocal wants to find at least one string equal to `S`. It is guaranteed that there is at least one way to complete the tree's values to achieve this.

# Input data
The first line will contain a number `C`. If `C = 1`, you need to answer question `1`, and if `C = 2`, you need to answer question `2`. The second line will contain the numbers `N, M` and `K`. The third line contains `N` natural numbers $val_1, ... , val_N$, representing the values associated with the nodes in the tree. If $val_i$ is `−1`, it means that node `i` does not yet have an associated value. The fourth line will contain the `K` natural numbers representing the string `S`. The next `N − 1` lines will each contain two numbers `u` and `v`, representing the edges of the tree.

# Output data
Print a single number representing the answer to either the first or the second question, depending on the value of `C`.

# Constraints
* `C ∈ {1, 2}`
* `1 \leq K \leq N \leq 500 000`
* `1 \leq M \leq 500 000`
* $1 \leq val_i \leq M$ or $val_i = −1$, for any `1 \leq i \leq N`
* $1 \leq S_i \leq M$, for any `1 \leq i \leq K`

## Subtask 1 (8 points)
* `C = 1, N \leq 13, M \leq 3`
## Subtask 2 (19 points)
* `C = 1, N \leq 5 000`
## Subtask 3 (22 points)
* `C = 1`
## Subtask 4 (11 points)
* `C = 2, N \leq 13, M \leq 3`
## Subtask 5 (40 points)
* `C = 2`

# Examples

`stdin`

```
1
8 3 3
-1 -1 2 -1 -1 -1 1 2
1 2 2
1 2
2 3
2 4
4 5
1 6
6 7
1 8
```

`stdout`

```
4
```

Explanation
---

Portocal can complete the node values as: `1 2 2 2 1 3 1 2`.

The first strings in lexicographic order will be:
`1` - for node `1`
`1 2` - for node `2`
`1 2` - for node `8`
`1 2 2` - for node `3`, which is equal to `S`.
Thus, the answer is `4`.

Notice that although there is another string equal to `S` for node `4`, Portocal stops when he finds the first one.

`stdin`

```
2
8 3 3
-1 -1 2 -1 -1 -1 1 2
1 2 2
1 2
2 3
2 4
4 5
1 6
6 7
1 8
```

`stdout`

```
6 
```

Explanation
---

There are `6` ways to complete the tree values so that Portocal finds the string `S` on day `4`. These are:
`1 2 2 2 1 3 1 2`
`1 2 2 3 1 3 1 2`
`1 2 2 2 2 3 1 2`
`1 2 2 3 2 3 1 2`
`1 2 2 2 3 3 1 2`
`1 2 2 3 3 3 1 2`
