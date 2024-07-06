Certainly! Here is the competitive programming problem statement translated into English while maintaining the specified format and syntax:

---

A student drew a set consisting of several squares that contain distinct consecutive natural numbers, arranged equally on the sides. On each side of the square, an odd number of values is written. In each square, the numbers are written in increasing order, starting from the bottom-left corner and proceeding counterclockwise. The student numbered the squares with $1$, $2$, $3$, etc., in strict ascending order of the number of values contained in each. The difference between the smallest number in square $P$ ($1$ < $P$) and the largest number in square $P - 1$ is equal to $1$. The first **four** squares are:

~[patrate.png]

Thus, the first square contains distinct consecutive natural numbers from $1$ to $8$, arranged with **three** on each side of the square. The second square contains the next $16$ distinct consecutive natural numbers, arranged with five on each side. The third square contains the next $24$ distinct consecutive natural numbers, arranged with seven on each side. The fourth square contains the next $32$ distinct consecutive natural numbers, arranged with nine on each side, etc.

# Task

Write a program that solves the following two tasks:

1. Read a natural number $M$ and determine the number $K$ of values contained in the square numbered $M$;
2. Read a natural number $N$ and determine the number $T$ of the square which contains the number $N$ on one of its sides.

# Input data

The input file `patrate.in` contains on the first line a natural number $C$ representing the task that needs to be solved ($1$ or $2$). If $C = 1$, then the file contains a natural number $M$ on the second line. If $C = 2$, then the file contains a natural number $N$ on the second line.

# Output data

If $C = 1$, then the output file `patrate.out` contains on the first line the number $K$, representing the answer to the first task of the problem. If $C = 2$, then the output file `patrate.out` contains on the first line the natural number $T$, representing the answer to the second task.

# Constraints and clarifications

* $1 \leq M \leq 260\ 000\ 000$;
* $7 \leq N \leq 2\ 147\ 302\ 920$;
* The numbers $N$, $M$, $T$, and $K$ are natural numbers
* There are no two squares with the same number of values written on their sides
* For correct solving task $1$, $10$ points are awarded; for correct solving task $2$, $80$ points are awarded. $10$ points are awarded by default.

# Example 1

`patrate.in`
```
1
3
```

`patrate.out`
```
24
```

## Explanation

The task is $1$. The square numbered $M = 3$ contains $K = 24$ natural numbers (see the figure in the statement).

# Example 2

`patrate.in`
```
2
73
```

`patrate.out`
```
4
```

## Explanation

The task is $2$. The number $N = 73$ is contained in the square numbered $T = 4$ (see the figure in the statement).

---