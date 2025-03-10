
# Task

The [RoAlgo](https://discord.gg/roalgo) server has been active for $n$ days, and we know how many members it had after each day. Determine the day with the largest growth in the number of members, where the growth on day $i$ is calculated using the formula $a_i - a_{i-1}$, where $a_i$ represents the number of members on day $i$, and $a_{i-1}$ represents the number of members on day $i-1$. It is considered that $a_0 = 0$, so the growth on the first day is $a_1$.

# Input data

The first line will contain $n$, the number of days since the RoAlgo server was created. The second line will contain the $n$ numbers, representing the number of members of the RoAlgo server. It is guaranteed that the numbers in the sequence are in strictly increasing order. 

# Output data

The first line will contain the day with the largest growth in the number of members. If there are multiple days with the same growth, print the first one. 

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000$;
* $1 \leq a_1 \leq a_2 \leq \dots \leq a_n \leq 10^6$. 

# Example

`stdin`
```
7
2 8 12 15 22 34 36
```

`stdout`
```
6
```

## Explanation

The largest growth occurred on day $6$, because $a_6 - a_5 = 12$, being the largest such difference.
