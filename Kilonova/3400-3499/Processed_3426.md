Antonia recently visited London. There, she was impressed by the large number of metro stations which, to her surprise, formed a tree. Getting bored in the metro, Antonia wonders if she could generate a tree with a minimum number of nodes, which has exactly $K$ paths from $X$ to $Y$, for any nodes $X$, $Y$ with the condition that $X$ is an ancestor of $Y$. By replacing the current metro map with this tree, she believes she could reduce the rush hour crowding.

# Task

Help Antonia generate the desired tree with a minimum number of nodes.

# Input data

A single natural number, $K$ - the number of paths with the above property, will be read from the keyboard.

# Output data

$N + 1$ lines representing the generated tree, with the nodes indexed from $0$, will be displayed on the screen.

The first line will contain the number $N$ - the number of nodes of the tree.

The following $N$ lines will contain two numbers $X$ and $T$, separated by a space, with the following meaning:

* The node $T$ is the parent of node $X$. If the node $X$ does not have any parent, the value of node $T$ will be $-1$.

# Constraints and clarifications

- For each test, the tree must have at most $10^6$ nodes.
- $0 \leq K \leq 10^9$
- For each test, the score will be awarded as follows:
  1. $100\%$ of the score if $N_{\text{participant}} = N_{\text{comisie}}$
  2. $80\%$ of the score if $N_{\text{participant}} \in [N_{\text{comisie}} + 1, N_{\text{comisie}} + 2]$
  3. $P\%$ of the score if $N_{\text{participant}} \geq N_{\text{comisie}} + 3$, where $P = \frac{N_{\text{comisie}} + 3}{N_{\text{participant}}} \cdot 50$
- Note: $N_{\text{comisie}}$ is the minimum number of nodes with which a tree can be generated with the mentioned property.

| # | Score | Constraints |
| ------- | ------- | ---------- |
| 1 | 20 | $0 \leq K \leq 50$ |
| 2 | 30 | $0 \leq K \leq 500$ |
| 3 | 50 | No additional constraints |

# Example 1

`stdin`
```
2
```

`stdout`
```
3
0 -1
1 0
2 0
```

## Explanation

~[subway-1.png]

There are $2$ paths from $X$ to $Y$, for any nodes $X$, $Y$ such that $X$ is an ancestor of $Y$:

$(X,Y) \in \{(0, 1), (0, 2)\}$

# Example 2

`stdin`
```
4
```

`stdout`
```
4
0 -1
1 0
2 0
3 2
```

## Explanation

~[subway-2.png]

There are $4$ paths from $X$ to $Y$, for any nodes $X$, $Y$ such that $X$ is an ancestor of $Y$:

$(X,Y) \in \{(0, 1), (0, 2), (0, 3), (2, 3)\}$