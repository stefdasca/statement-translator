
# Task

On a table, there are $N$ piles of stones placed from left to right, numbered from $1$ to $N$. The pile with index $i$ contains $a_i$ stones. Roxana and Sorin will start taking stones alternately (starting with Roxana), as follows: on each move, each player chooses a pile $x > 1$, takes a non-zero number of stones from it and moves them to pile $x-1$. The player who can no longer make a move loses. As this game is too easy for them, they decide to make it a little more complicated. In each of the following $Q$ moments in time, they will perform one of the following operations:

1. Choose an interval $[l,r]$, play on it, and then record the winner in a notebook.
2. They choose to change the number of stones at position $l$ to $x$, at position $l+1$ to $x+1$, $\dots$, at position $r$ to $x+r-l$.

Unfortunately, at the end of the day they lost the notebook. Knowing that both players play optimally, they ask you to help reconstruct the list written on the lost notebook.

# Input data

The first line contains the natural numbers $N$ and $Q$, representing the number of piles and the number of moments in time.

The second line contains $N$ natural numbers $a_1, a_2, \dots, a_N$, representing the number of stones in each pile.

The following $Q$ lines contain the query components. Thus, each line will contain $T$, the type of operation executed at that time. If $T=1$, it will also contain $L$, $R$ representing the interval on which the two will play. If $T=2$, it will contain $L$, $R$ and $X$ meaning they will change the elements in the interval $[L, R]$ to $X, X+1, \dots, X+R-L$.

# Output data

For each line corresponding to a query (a game) print the winner of the game: `Roxana` or `Sorin`. Note, do not print in another format, such as `roXaNa` or `SORiN`.

# Constraints and clarifications

* $ 1 \leq N, Q \leq 2 \cdot 10^5$
* $ 1 \leq L \leq R \leq N $
* $0 \leq a_i, X, X+R-L \leq 10^9$

|#| Score  |        Constraints                                 | 
|-|--------|----------------------------------------------------|
|0|   0    | Examples                                           |
|1|   10   | $N \le 5, Q = 1, T = 1, L = 1, R = N, a_i \leq 5$  |
|2|   36   | $Q = 1, T = 1, L = 1, R = N$                       |
|3|    7   | $N, Q \leq 1000$                                   |
|4|   15   | $a_i, X, X+R-L \leq 10^6$                          |
|5|   32   | No additional constraints                           |

# Example

`stdin`
```
4 4
4 2 5 2
1 1 4
2 1 3 1
1 2 3
1 1 4
```

`stdout`
```
Sorin
Roxana
Sorin
```

## Explanation

The first query will be played on the sequence `4 2 5 2`, where Sorin wins. After the update, the sequence becomes `1 2 3 2`. In the second query, the game will be played on the sequence `2 3`, where Roxana wins. In the third query, the game will be played on the sequence `1 2 3 2`, where Sorin wins.
