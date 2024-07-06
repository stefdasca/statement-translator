# Task

You are given a ranking line in the form $(M, V, E, I, P)$ — (matches, wins, draws, losses, points), some of which may be marked with a question mark ($?$) but not $M$. This ranking line corresponds to the results of a team over a competitive season in a football league from Southeast Europe.

Now B.B.C, a specialist in the field, wants to know if we can obtain a valid configuration starting from the current configuration according to football rules ($3$ points for a win, $1$ point for a draw, $0$ points for a loss) or if it's impossible. This can be done by replacing the question marks with natural numbers.

For example, the configuration $(5, ?, 1, ?, 10)$ is valid because we can obtain the configuration $(5, 3, 1, 1, 10)$ — $3$ wins, $1$ draw, and $1$ loss.

Note that the number of matches is always known.

# Input data

The first line contains the number of tests $T$. 

Each of the following $T$ lines contains a configuration in the format described in the statement, with each of the $5$ positions containing either the character `?` or a natural number, representing the corresponding number for that position.

# Output data

Each line contains either a correct configuration starting from the given input or the message `Impossible`, otherwise.

Any correct configuration is accepted.

# Constraints and clarifications

* $1 \leq T \leq 10^5$
* $0 \leq M, V, E, I, P \leq 10^7$

|#|Score|Constraints|
|-|-|--------|
|1|0|Example|
|2|13|Only one variable is unknown and $M \leq 300$|
|3|13|The number of points is always unknown and $M \leq 300$|
|4|20|$M \leq 300$|
|5|13|Only one variable is unknown|
|6|13|The number of points is always unknown|
|7|28|No additional constraints|

# Example

`stdin`
```
17
5 ? ? ? ?
9 4 ? 4 ?
7 ? ? 5 4
4 1 2 1 6
6 3 ? 4 12
9 ? 4 ? 13
14 5 ? ? 13
58 28 ? ? 94
100 ? ? 43 120
10 ? ? ? ?
10 4 3 3 ?
10 4 3 ? ?
10 4 ? 3 ?
10 4 ? ? ?
10 ? 3 3 ?
10 ? 3 ? ?
10 ? ? 3 ?
```

`stdout`
```
5 0 0 5 0
9 4 1 4 13
7 1 1 5 4
Impossible
Impossible
9 3 4 2 13
Impossible
58 28 10 20 94
Impossible
10 0 0 10 0
10 4 3 3 15
10 4 3 3 15
10 4 3 3 15
10 4 0 6 12
10 4 3 3 15
10 0 3 7 3
10 0 7 3 7
```
