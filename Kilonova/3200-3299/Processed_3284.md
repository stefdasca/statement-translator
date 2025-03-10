> \- Lina, now there are green stripes on the monitor; I think the graphics card is broken.
> \- Oh no, Vasile!
> \- I think it's from the holy water I poured on the laptop.
> \- Ah, so the holy water was more "effective" than we expected!
> -- Vasile and Lina, After a failed baptism

Ana and Bob are bored during their vacation. They found a magazine with multiple games in the city they are visiting. The following caught their attention:

The game is played with a rooted tree (consult page three for more details). A single pawn is placed at the root. The game proceeds over multiple rounds, each with the same steps. Specifically, during a round:

1. The First Player chooses at most one edge from the tree and permanently blocks it (they can also choose to do nothing).
2. Then, the Second Player must move the pawn to a child node. If all edges to child nodes are blocked, the game ends. Otherwise, they choose a child node with an unblocked edge and move the pawn there.

The game's score is the distance of the pawn from the root when the game ends. The First Player must make their moves so that the final score is as minimal as possible, while the Second Player must make theirs so that the final score is as maximal as possible. Therefore, the goal of the First Player is to bring the pawn as close to the root as possible, while the Second Player tries to move it as far away as possible.

Ana will take on the role of the First Player, and Bob the role of the Second Player. Ana and Bob have traveled a path full of challenges and efforts to reach this culmination in their ascent as logicians. Thus, you can consider that each plays every game perfectly optimally to achieve their goal.

After a few rounds, the children want to make the game more interesting. Thus, they will generate an infinite tree to play on. This is generated through the following process:

1. Initially, a root node with an associated value of 1 is created.
2. Then, whenever a node with value $x$ appears, it will be attached $K_x$ child nodes with associated values $v_{x, 1}$, $v_{x, 2},\dots, v_{x, K_x}$. These, in turn, will generate new nodes, and so on. Remember that the indices of the newly created nodes can be chosen arbitrarily, the only specification of this process concerns the associated values.

# Task

Ana holds a grudge against Bob for a while, so to play a little prank on him, she wants to convince him that she is a clairvoyant. Thus, she will give you the configuration of a game they are about to play and wants you to tell her beforehand what the game's score will be at the end of the moves. She observes that there are cases where the game will go on indefinitely, in which case you just need to communicate $-1$.

# Input data

The first line contains $N$, the number of existing values that nodes can have.

In the $i$-th of the following $N$ lines, there will be first $K_i$, then $K_i$ values $v_{i, 1}$, $v_{i, 2}, \dots, v_{i, K_i}$.

# Output data

Print a single value: $-1$ if the game goes on indefinitely, or Bob's score at the end of it otherwise.

# Constraints and clarifications

* $1 \le N \le 10^6$;
* $1 \le K_i \le 10^6$, and in particular $1 \le S_K \le 10^6$, where $S_K$ is the sum of all $K_i$ present in a test;
* $1 \leq v_{i, j} \leq N$.

|#| Points | Constraints |
|-|--------|-------------|
|1|    6   | $K_i \geq 2$ |
|2|   25   | $N \leq 7$ and $S_K \le 7$ |
|3|   22   | $K_i \leq 2$ |
|3|   21   | $N \leq 10^3$ and $S_K \le 10^3$ |
|4|   26   | No additional constraints. |

# Example 1

`stdin`
```
3
2 2 3
1 1
2 3 3
```

`stdout`
```
1
```

# Example 2

`stdin`
```
4
2 1 2
3 1 3 4
2 2 3
1 1
```

`stdout`
```
-1
```

## Explanation

~[graph-jpa2.png]

The first 4 levels of the infinite tree described in the second example. The values adjacent to the nodes represent the values associated with them assigned according to the procedure. Note that the tree infinitely continues from this point.

# Rooted Tree

A **rooted tree** is a group of points (formally called nodes) connected to each other by lines (formally called edges), similar to a tree, where a special point is considered the beginning or the "root." This grouping of lines and points respects the following conditions:

* Each point is either directly or indirectly connected to the "root," which is drawn as the node at the top.
* The lines do not form loops or circles — you can travel from one point to another through a unique succession of lines.
* Considering the succession of points and lines connecting the root to any other point $X$, we call the last point traversed on this path before $X$ the parent. Also, we call the children of a node $X$ the set of points that have $X$ as their parent.
* You can imagine starting from the root and "growing" (downwards) the points on branches without going back.

In the given drawing, the root is $A$. For node $F$, its parent is $C$, and its children are $N$ and $O$.