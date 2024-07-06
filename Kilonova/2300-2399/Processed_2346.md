# Task

Luci has a ball. It has an interesting property: it can move on the integer number axis! More precisely, it can only move within the interval $[-X, X]$. Luci noticed that the ball moves in the first minute by one position, in the second minute by two positions, $\\dots$, in the $N^{th}$ minute it moves by $N$ positions. If it reaches the end of the interval $[-X, X]$, it changes direction and continues with the remaining number of positions.

If initially the ball is at position $0$ and moves towards $X$, what position will it be after $N$ minutes?

# Input data

The first line contains the numbers $X$ and $N$.

# Output data

The first line contains the position of the ball after $N$ minutes.

# Constraints and clarifications

* $1 \leq X \leq 10^9$;
* $1 \leq N \leq 10^9$;

| # | Points | Constraints | 
| - | ----- | ------------ |
| 1 | 20 | $1 \leq X \leq 10^4, 1 \leq N \leq 1000$ |
| 2 | 20 | $1 \leq X \leq 10^6, 1 \leq N \leq 5 \times 10^5$ |
| 3 | 60 | No additional constraints |

# Example 1

`biluta.in`
```
4 3
```

`biluta.out`
```
2
```

## Explanation

The ball moves as follows:

$0 \rightarrow 1 \rightarrow 3 \rightarrow 2$

# Example 2

`biluta.in`
```
3 7
```

`biluta.out`
```
2
```

## Explanation

The ball moves as follows:

$0 \rightarrow 1 \rightarrow 3 \rightarrow 0 \rightarrow -3 \rightarrow -1 \rightarrow 2$