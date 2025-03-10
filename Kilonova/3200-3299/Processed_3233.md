# Task

Consider a circle. There are $N$ distinct points marked on the circle. If we draw lines connecting all pairs of points, what is the maximum number of pieces into which the circle can be divided? Answer this question for $Q$ such scenarios.

# Input data

The program reads from the keyboard the number $Q$ and on the next $Q$ lines, it reads a number $N$, representing the number of points in the respective scenario.

# Output data

On the next $Q$ lines, the program will print the answers for each scenario, modulo $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications

* It is recommended to use [fastio](https://www.geeksforgeeks.org/fast-io-for-competitive-programming/).
* $1 \leq Q \leq 100 \ 000$
* $1 \leq N \leq 1 \ 000 \ 000 \ 000$
* For 25 points, $Q \leq 5\ 000$, $N \leq 5\ 000$.
* For another 50 points, $Q \leq 100 \ 000$, $N \leq 1 \ 000 \ 000$.
* Since the answer can be very large, it will be printed modulo $1 \ 000 \ 000 \ 007$.

# Example

`stdin`
```
6
1
2
3
4
5
6
```

`stdout`
```
1
2
4
8
16
31
```

## Explanation

For the fourth scenario, one of the possible optimal arrangements for the $4$ points is the following:

~[moser.png]