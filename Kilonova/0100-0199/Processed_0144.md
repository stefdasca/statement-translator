```markdown
Kaguya, the vice-president of the student council, is sick. Miyuki wants to traditionally give her a gift of a thousand paper cranes. Maybe not a thousand... (*too exaggerated for a simple cold*), and maybe not a crane... (*too traditional and anyway I don't have origami paper...*). A star tree should be ideal!

Miyuki has a tree (an acyclic connected graph) consisting of `N` nodes numbered from `1` to `N`. He wants to transform it into a star tree of size `N - K`, meaning a connected acyclic graph that has at least `N - K - 1` leaves (nodes with exactly `1` neighbor).

To transform his tree into a star tree, Miyuki will perform `K` folding operations of two nodes at a time. For the `i`-th folding operation, Miyuki:
* Chooses two distinct nodes $a_i$ and $b_i$ existing at that moment in the tree.
* Notes with `V` the set of neighbors of nodes $a_i$ and $b_i$ (nodes that have a direct edge to at least one of $a_i$ or $b_i$).
* Deletes nodes $a_i$ and $b_i$ from `V` if they were present.
* Removes nodes $a_i$ and $b_i$ from the tree, along with the edges originating from either $a_i$ or $b_i$.
* Adds a new node with number `N + i` to the tree.
* Adds edges between node `N + i` and each node in the set `V`.

After such an operation, the resulting graph must still be a tree; more specifically, the operation performed must not introduce any cycles. Otherwise, the operation is invalid and cannot be performed.

Because he doesn't want to appear to have tried too hard, Miyuki wants to perform a minimum number `K` of operations. Since the secretary Chika promised not to teach him anymore, you need to help Miyuki determine:
1. What is the minimum number `K` of operations to transform the initial tree into a star tree.
2. What are the `K` operations through which the initial tree is transformed into a star tree.

# Input data
The first line contains a single natural number `N`, representing the size of the initial tree. The next `N - 1` lines describe the edges of the initial tree, with the `i+1`-th line containing two natural numbers $u_i$ and $v_i$, representing the nodes connected by the `i`-th edge of the tree.

# Output data
The first line contains a single natural number `K`, representing the minimum number of operations that need to be performed. The next `K` lines contain `K` pairs of natural numbers $a_i$ and $b_i$ (`1 \leq i \leq K`), separated by a space, representing, in order, the folding operations performed on the tree.

# Constraints and clarifications
* `1 \leq N \leq 500\ 000`
* If there are multiple possible solutions, any one of them can be printed.
* If the minimum number of operations `K` is correctly determined, but the displayed operations do not correctly transform the tree into a star, or one of the operations is invalid according to the definition given in the statement, `30%` of the score will be awarded.

## Subtask 1 (10 points)
* `1 \leq N \leq 15`
## Subtask 2 (20 points)
* `1 \leq N \leq 200`
## Subtask 3 (10 points)
* $u_i = i, v_i = i + 1$, for `1 \leq i < N`
## Subtask 4 (60 points)
* No additional constraints

# Examples

`stdin`

```
5
1 2
2 3
3 4
4 5
```

`stdout`

```
1
2 4
```

Explanations
---

A single folding operation is performed, between nodes `2` and `4`.
The operation proceeds as follows:
- The neighbors of nodes `2` and `4` are `V = 1, 3, 5`.
- Remove nodes `2` and `4` from the tree.
- Add node `N+1 = 6` and edges `(1, 6), (3, 6), (5, 6)`.

The final tree consists of nodes `1, 3, 5` and `6`, and edges `(1, 6), (3, 6), (5, 6)`. We observe that nodes `1, 3`, and `5` have a single neighbor and only `6` has `3` neighbors, so the resulting tree is a star.

`stdin`

```
6
1 2
2 3
3 4
4 5
5 6
```

`stdout`

```
2
2 4
5 7
```

Explanations
---

Two folding operations are performed:
- `(2, 4)`, adding node `N+1 = 7`;
- `(5, 7)`, adding node `N+2 = 8`.

The final tree consists of nodes `1, 3, 6` and `8`, and edges `(1, 8), (3, 8), (6, 8)`.
```