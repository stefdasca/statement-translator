
# Task

Given a string $S$ consisting only of lowercase Latin letters. We say that the score of a string $T$ is $k + |T|$, where $k$ is the number of occurrences of $T$ as a subsequence in $S$, and $|T|$ is the length of the string $T$. The task is to display the maximum possible score of a string $T$ that appears in $S$ as a subsequence at least once.

# Input data

The first line will contain the string $S$.

# Output data

The first line will contain a single integer, the maximum score sought.

# Constraints and clarifications

* $1 \leq |S| \leq 1 \ 000 \ 000$
* For tests worth $50$ points, we have $1 \leq |S| \leq 50$.

# Example 1

`stdin`
```
aaa
```

`stdout`
```
4
```

## Explanation

An optimal string is $T = \text{aa}$.

# Example 2

`stdin`
```
ab
```

`stdout`
```
3
```

## Explanation

The only optimal string is $T = \text{ab}$.
