Ion and Vasile are playing a game. They have at their disposal a strict binary tree (meaning each node has `0` or `2` children) with `N` nodes, numbered from `1` to `N` (the node numbered `1` is the root of the tree). Initially, all nodes are white. The players will take turns, and the player on their turn will color a white node black. Ion makes the first move and can color any node black. Considering that the last node colored by one of the players is `P`, the player who follows can color one of the following nodes black (if they have not already been colored black):
- one of the `2` children of `P` (if `P` is not a leaf in the tree)
- the parent of `P` (if `P` is not the root of the tree)

The game continues until one of the players can no longer make a move. Then, the player who made the last move is considered the winner.

# Task
Considering that both players play optimally, determine all the nodes in the tree that Ion can color on the first move so that he is guaranteed to win.

# Input data
The first line of the file `color.in` contains the integer `N`, representing the number of nodes in the tree. The following `N-1` lines contain two integers separated by a space, `a` and `b`, meaning that `a` is the parent of `b`.

# Output data
The first line of the file `color.out` will contain the integer `M`, representing the number of nodes that Ion can color on the first move so that he is guaranteed to win. On the next line, print the numbers of these nodes, in increasing order.

# Constraints and clarifications
* `1 \leq N \leq 16\ 000`, `N` odd
* `40%` of the tests will have `N \leq 1\ 000`

# Example

`color.in`
```
9
1 2
1 3
2 4
2 5
4 6
4 7
3 8
3 9
```

`color.out`
```
6
1 5 6 7 8 9
