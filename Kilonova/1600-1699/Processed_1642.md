On a table, there are $N$ stacks (numbered from $1$ to $N$). Stack $i$ contains $i$ tokens ($1 \leq i \leq N$). In one move, a set of stacks can be chosen and the same number of tokens can be extracted from each stack in the chosen set.

# Task

Determine a sequence of moves with a minimum number of operations to empty all $N$ stacks.

# Input data

The input file `stive.in` contains on the first line the natural number $N$.

# Output data

The output file `stive.out` will contain on the first line a natural number $MIN$ representing the minimum number of moves performed. The next $MIN$ lines describe the moves, one move per line. The line describing a move has the form: $nr$, $s_1$, $s_2$, $\dots$, $s_{nr}$, $x$, where $nr$ represents the number of stacks in the selected set for that move; $s_1$, $s_2$, $\dots$, $s_{nr}$ are the selected stacks, and $x$ represents the number of tokens extracted from each stack $s_1$, $s_2$, $\dots$, $s_{nr}$. The values on the same line are separated by spaces.

# Constraints and clarifications

* $1 \leq N \leq 30\ 000$

# Example

`stive.in`
```
3
```

`stive.out`
```
2
2 2 3 2
2 1 3 1
```

## Explanation

The initial configuration of the stacks is $1, 2, 3$.

In the first move, $2$ stacks ($2$ and $3$) are selected and $2$ tokens are extracted from each. The configuration becomes: $1, 0, 1$.

In the final move, stacks $1$ and $3$ are chosen, $1$ token is extracted from each and thus all stacks are emptied.
