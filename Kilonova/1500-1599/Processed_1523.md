~[asdf.jpg|align=right]

Given a sorted array $v$ in ascending order with $N$ distinct positive natural elements which we do not know, but which we aim to determine. With this array $v$, using the binary search algorithm presented in the attached image, we can respond to queries of the form:

- Given a number $X$ and an interval $[a, b]$, determine the smallest element greater than $X$ within the interval defined by indices $a$ and $b$, the interval from array $v$.

We know the steps that the binary search algorithm followed for different values of the triplet $(X, a, b)$.

# Task

Given $N$ (the length of the array), $Q$ (the number of queries called), and the $Q$ queries, determine the initial array. If there are multiple solutions, the lexicographically smallest solution will be displayed. If there is no solution, the value $-1$ will be displayed. An array $V_1$ is considered lexicographically smaller than another array $V_2$ if there is an index $i$ such that: $V_1[1] = V_2[1]$, $V_1[2] = V_2[2]$, $\dots$, $V_1[i-1] = V_2[i-1]$ and $V_1[i] < V_2[i]$.

The $Q$ queries consist of:
* $X$ which represents the value we are looking for by binary search in the array
* $M$ which represents the number of iterations in the binary search algorithm
* $[a, b]$ representing the interval in which the binary search algorithm is applied (the pair $(a, b)$ is considered the first iteration in the algorithm)
* $M-1$ pairs of indices representing the values displayed by the binary search algorithm following each iteration

# Input Data

The input file `bsrec.in` contains on the first line a value $T$ representing the number of tests to be performed. For each of the $T$ tests, the first line will contain the value $N$ (the number of elements in the array), followed by $Q$ (the number of queries), separated by a space.
The following lines describe the $Q$ queries. Within a query, the first line will contain a pair of numbers $(X, M)$ separated by a space, where $X$ represents the value sought in the array, and $M$ the number of steps performed in the binary search for the smallest value in the array which is greater than $X$. On the next line of the query, there is a pair of values $(a, b)$ as described above. The following $M-1$ lines contain pairs $(st, dr)$ of natural values separated by a space, which represent the left and right indices displayed following each iteration of the above algorithm.

# Output Data

The output file `bsrec.out` will contain $T$ lines, line $i$ containing the answer for test $i$. If the test admits a solution, $N$ positive natural strictly increasing numbers representing the values of the array $v$ will be printed. Since there are multiple solutions, the lexicographically smallest solution will be displayed. If the test does NOT admit a solution, the value $-1$ will be displayed.

# Constraints and clarifications

* $1 \leq T \leq 10$
* $1 \leq N,Q \leq 1 \ 000$
* $1 \leq X \leq 10^9$
* $1 \leq st \leq dr \leq N$, except for the last pair in the binary search where $st > dr$.
* For $20\%$ of the total score there are tests with $1 \leq N, Q \leq 10$ and the lexicographically minimum solution admits values up to $20$.
* It is guaranteed that $M \leq 15$.

# Example

`bsrec.in`
```
2
5 3
3 4
1 5
1 2
2 2
2 1
30 3
2 4
4 4
5 4
25 2
4 5
4 3
5 3
30 4
1 5
1 2
2 2
2 1
3 3
2 4
4 4
5 4
5 2
4 5
4 3
```

`bsrec.out`
```
1 3 4 25 26
-1
```

## Explanation

The file contains $2$ tests.

The first test has $3$ queries:
- The first query looks for the value $3$ in the interval $[1, 5]$ and makes $4$ iterations;
- The second query looks for the value $30$ in the interval $[2, 4]$ and makes $3$ iterations;
- The third query looks for the value $25$ in the interval $[4, 5]$ and makes $2$ iterations.

The second test has $3$ queries, but it does NOT admit a solution.