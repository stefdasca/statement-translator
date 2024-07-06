```markdown
You are given an integer $n$ and your task is to check how many numbers from $1$ to $n$ can be written as sum of $k$ not necessary distinct prime numbers.

As this is too easy, you will have to check whether this is possible or not for $q$ such numbers.

# Task

# Input data
The first line will contain only one number $q$, representing the number of queries.

The next $q$ lines will contain two integers $n$ and $k$.

# Output data

The output will contain $q$ lines, each having a single element representing the answer of the problem.

# Constraints and clarifications
* $1 \leq q \leq 10^5$
* $1 \leq n \leq 10^{18}$
* $3 \leq k \leq 10^9$
* For tests worth 10 points, $q = 1, 3 \leq n, k \leq 200$
* For tests worth 20 more points, $q = 1, 1 \leq n \cdot k \leq 10^6$
* For tests worth 30 more points, $1 \leq n \leq 10^6$

# Example

`stdin`
```
4
7 3
10 4
11 5
7 4
```

`stdout`
```
2
3
2
0
```
```