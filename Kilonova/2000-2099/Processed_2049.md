# Task

You are a fan of the king of sports and want to make a prediction before the start of the season regarding the number of points your favorite team will score.

However, you want your prediction to make sense, and for this, the number of points must be achievable in a season.

You know that your team plays $m$ matches, and your prediction is $p$ points. You will need to display `YES` if the prediction makes sense, and `NO` otherwise.

It is known that a victory brings $3$ points, a draw brings $1$ point, and a defeat brings $0$.

# Input data

The first line will contain $t$, the number of tests. The next $t$ lines will contain the values of $m$ and $p$, corresponding to each prediction.

# Output data

For each test, you will print `YES` if the prediction makes sense, or `NO` otherwise.

# Constraints and clarifications

* $1 \leq t \leq 10^5$
* $0 \leq m, p \leq 10^9$

# Example

`stdin`
```
6
7 11
5 19
8 23
14 34
99 296
40 120
```

`stdout`
```
YES
NO
NO
YES
NO
YES
