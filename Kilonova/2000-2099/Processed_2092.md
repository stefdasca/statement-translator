**Attention** — This is the easy version of the problem [SuperLiga](https://kilonova.ro/contests/42/problems/2023).

# Task

Given a ranking line in the form $(M, V, E, I, P)$ — (matches, victories, draws, losses, points), this ranking line corresponding to the results of a team throughout a competitive season in a football league in Southeast Europe.

Now B.B.C, a specialist in the field, wants to find out if the given configuration is valid according to the football rules ($3$ points for a victory, $1$ point for a draw, $0$ points for losses).

# Input data

The first line contains the number of tests $T$. 

Each of the next $T$ lines contains a configuration having the format described in the statement, each of the 5 positions contains a natural number, representing the corresponding number for that position.

# Output data

Each line will contain `YES`, if the configuration is correct, or `NO`, otherwise. 

# Constraints and clarifications

* $1 \leq T \leq 10^5$
* $0 \leq M, V, E, I, P \leq 10^6$

|#|Scores|Constraints|
|-|-|--------|
|1|0|Example|
|2|50|$M, V, E, I, P \leq 200$|
|3|50|No additional constraints|

# Example

`stdin`
```
10
11 8 1 2 25
9 4 4 3 16
5 0 5 0 5
58 28 10 20 94
10 4 0 6 12
685 684 0 1 2052 
10 4 3 3 15
10 1 3 6 5
6 0 3 3 3 
11 1 8 2 10
```

`stdout`
```
YES
NO
YES
YES
YES
YES
YES
NO
YES
NO
```

## Explanation

For example, in the last test, the number of points obtained is $11$, not $10$.