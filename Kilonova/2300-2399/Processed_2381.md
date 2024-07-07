Dorel, a 10th-grade student, recently started experimenting with algorithms for placing $B$ identical balls into $C$ boxes! He tried to analyze the number of ways to place the $B$ balls into the $C$ chosen boxes such that for a chosen constant $K$, the algorithm he wrote on paper **does not** run indefinitely. His algorithm can be found written in pseudocode below:

```
pos â† 1
sum â† 0
while pos \leq c:
    while sum != k:
        sum â† sum + nrbile[pos] + 1
        pos â† pos + 1
    sum â† 0
```

# Task

For $B$ balls, $C$ boxes, and a constant $K$, determine the number of ways to place the balls into the boxes such that the algorithm presented above does not run indefinitely. Since this number can be very large, Dorel asks you to find the remainder when divided by $10^9+7$.

# Input data

The first line of the input file `dorel.in` contains the number $T$, which represents the number of tests. Then, on the next $T$ lines, there are 3 numbers $B, C$, and $K$ with the above meanings. The tests in the input are independent of each other.

# Output data

The file `dorel.out` will contain $T$ numbers, each on a separate line, where the $i$-th line of the output will contain the answer to the $i$-th test modulo $10^9+7$.

# Constraints and clarifications

* $1 \leq T \leq 2 \cdot 10^5$
* $1 \leq B, C, K \leq 10^6$
* According to the OJI regulations, tests will be evaluated **individually**, so it is not necessary to pass all tests to receive the score for the respective subtask.

| # | Score | Constraints          |
| - | ----- | -------------------- |
| 1 | 20    | $T, B, C, K \leq 10$ |
| 2 | 20    | $T \leq 10; B, C, K \leq 1\ 000$ |
| 3 | 5     | $B, C, K \leq 1\ 000; B + C = K$ |
| 4 | 10    | $B + C = K$          |
| 5 | 10    | $B, C, K \leq 1\ 000$ |
| 6 | 35    | No additional constraints. |

# Example 1

`dorel.in`
```
6
3 3 3
1 5 6 
10 10 10
5 8 1
10 2 4
961 423 346
```

`dorel.out`
```
4
5
43758
0
0
434187092
```

## Explanation

For the case $B = 3, C = 3, K = 3$, we have the following valid configurations:

* $0, 1, 2$
* $1, 0, 2$
* $2, 0, 1$
* $2, 1, 0$

For the case $B = 1, C = 5, K = 6$, we have the following valid configurations:

* $1, 0, 0, 0, 0$
* $0, 1, 0, 0, 0$
* $0, 0, 1, 0, 0$
* $0, 0, 0, 1, 0$
* $0, 0, 0, 0, 1$