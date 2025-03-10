Fix $N-1$ years ago, Rara began observing the behavior of the tribes on the planet Irut, a sister of Earth from a distant galaxy. In the first year of research, the first tribe was formed, consisting of $A$ inhabitants, in the second year, the second tribe, consisting of $B$ inhabitants, and, as you might expect, in the third year, the third tribe, consisting of $C$ inhabitants. Starting from the fourth year, Rara discovered a rule: every year a new tribe appears with a population equal to the sum of the populations of the tribes that appeared in the previous $3$ years. Armed with this cosmic information, Rara traveled through time and space, thus reaching our planet today. To proceed to the next step of the interplanetary operation, he asks you: What are the last $3$ digits of the population of the tribe that appeared this year on the planet Irut?

# Task

Display the last $3$ digits of the number of citizens of the most recently appeared tribe on the planet Irut. If this number has less than $3$ digits, zeros should be added in front of it so that a total of $3$ digits are displayed.

# Input data

The first line contains a single natural number $N$.
The second line contains three natural numbers separated by a space, $A, \ B, \ C$.

# Output data

The first line will contain the last $3$ digits of the population of the tribe that appeared this year.

# Constraints and clarifications

* $4 \leq N \leq 10^6$;
* $0 \le A, \ B, \ C \le 10^9$

| #   | Score | Constraints                    |
| --- | ----- | ------------------------------ |
| 0   | 0     | Examples                       |
| 1   | 28    | $N \le 10$                     |
| 2   | 47    | $A=B=C=1, \ N \le 37$          |
| 3   | 25    | No additional restrictions     |

# Example 1

`stdin`
```
4
7 2 3
```

`stdout`
```
012
```

## Explanation

In year $4$, the $4$-th tribe will have $7+2+3=12$ inhabitants.

# Example 2

`stdin`
```
5
7 2 3
```

`stdout`
```
017
```

## Explanation

In year $5$, the $5$-th tribe will have $2+3+12=17$ inhabitants.

# Example 3

`stdin`
```
2025
1 0 3
```

`stdout`
```
781
```

## Explanation

In year $2025$, the last $3$ digits of the population of the $2025$-th tribe are $781$.