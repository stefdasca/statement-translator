You are given an _infinite_ array of zeroes with positions indexed by integers and $N$ position intervals of the form $[A, B]$. For each given interval, you need to perform one of the following two operations on the array:

* **Normal**: Add $1$ to all positions in the array from $A$ to $B$.
* **Flipped**: Add $1$ to all positions in the array _except_ those from $A$ to $B$.

# Task

You are required to choose one type of operation for each interval such that the maximum value found in the array after applying all operations is as small as possible.

# Input data

The first line of the input will contain the number of intervals $N$. The following $N$ lines will each contain two space-separated integers, $A$ and $B$, representing the endpoints of an interval.

# Output data

The first line of the output will contain the maximum value in the array after performing the $N$ operations optimally.

The second line will contain a binary string of length $N$, with the $i$-th character being $0$ if the $i$-th operation used was flipped, and $1$ if it was normal.

If there are multiple ways to choose the operations optimally, any valid solution is accepted.

# Constraints and clarifications

* $1 \leq N \leq 200 \ 000$
* $1 \leq A \leq B \leq 2N$

| # | Points | Constraints           |
| - | ------- | -------------------- |
| 1 | 7      | $N \leq 20$          |
| 2 | 24     | $N \leq 150$         |
| 3 | 21     | $N \leq 1 \ 000$     |
| 4 | 34     | $N \leq 50 \ 000$    |
| 5 | 14     | No additional constraints. |

# Example

`stdin`
```
5
10 10
6 6
1 7
2 5
2 7
```

`stdout`
```
2
11110
```

## Explanation

Another valid solution is:
```
2
11011
