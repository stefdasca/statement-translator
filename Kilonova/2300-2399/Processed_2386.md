
Peg Solitaire is a game for a single player. The board is a strip with $N$ positions. Each position can hold a single token.

Any game configuration can be encoded as a binary sequence of length $N$, where $1$ represents a token, and $0$ represents a free position.

A move is a jump to the left or a jump to the right.

In the jump to the right, the token on position $i$ jumps over the token on position $i+1$; the token on position $i+1$ is removed; the token on position $i$ lands on position $i+2$ (this must be free).

In the jump to the left, the token on position $i$ jumps over the token on position $i-1$; the token on position $i-1$ is removed; the token on position $i$ lands on position $i-2$ (this must be free).

For example:
In the configuration $011$, the token on position $3$ jumps to the left over the token on position $2$ and the configuration $100$ is obtained.
In the configuration $110$, the token on position $1$ jumps to the right over the token on position $2$ and the configuration $001$ is obtained.

The game ends successfully when only one token remains on the board.

# Task
Given a set of configurations, determine for which configurations from the set the game ends successfully.

# Input data
The input file `peg.in` contains on the first line a non-zero natural number $T$, representing the number of configurations in the file. Each of the next $T$ lines contains a binary sequence representing a game configuration.

# Output data
The output file `peg.out` will contain $T$ lines, one for each configuration. On line $i$ the digit $1$ will be written if the game for the $i$th configuration from the input file ends successfully, otherwise the digit $0$.

# Constraints and clarifications

* $1 \leq T \leq 10$
* $1 \leq$ Length of any configuration $ \leq 150\ 000$

# Example

`peg.in`
```
5 
1 
110
001111010
1101110
11
```

`peg.out`
```
1 
1 
1 
0 
0
```

## Explanation

Configuration $1$: the game ends successfully in $0$ moves.
Configuration $110$: the game ends successfully in a single move (the first token jumps over the second)
Configuration $001111010$: the game ends successfully in $4$ moves
$001111010 \rightarrow 001100110 \rightarrow 000010110 \rightarrow 000011000 \rightarrow 000100000$
