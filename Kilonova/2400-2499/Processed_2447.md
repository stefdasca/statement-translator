In each year, the Vila Elena restaurant organizes a _7 lei grill_ eating contest for its most loyal customers. In this contest, the score of each participant is determined by the number of _grills_ eaten within an hour.

Due to this method of ranking, it often happens that multiple participants achieve the same score, meaning they consume the same number of _grills_. In this scenario, those with the same score will share the same position in the ranking.

# Task

Knowing that this year, $N$ customers of the restaurant are participating in the eating contest, what is the number of distinct rankings that can be obtained at the end of the contest?

# Input data

The input file `concurs.in` contains one natural number $N$ on the first line, representing the number of customers participating in the contest.

# Output data

The output file `concurs.out` will contain a single natural number on the first line, the number of distinct rankings $mod\\  666013$.

# Constraints and clarifications

* $1 \\leq N \\leq 5 \\ 000$;
* For $30\\%$ of the tests, $N \\lt 10$.

# Example

`concurs.in`
```
3
```

`concurs.out`
```
13
```

## Explanation

There are $13$ distinct rankings. For $3$ contestants $A$, $B$ and $C$, these are:
$(A, B, C)$, $(A, C, B)$, $(B, A, C)$, $(B, C, A)$, $(C, A, B)$, $(C, B, A)$, $(A=B, C)$, $(A=C, B)$, $(B=C, A)$, $(A, B=C)$, $(B, A=C)$, $(C, A=B)$, $(A=B=C)$.

In the above list, we used:
* $(A, B, C)$ to designate the ranking in which $A$ is in the first position, $B$ is in the second position, and $C$ is in the third position.
* $(A=B, C)$ for the ranking in which $A$ and $B$ share the first position, and $C$ is in the second position.
* $(A=B=C)$ for the ranking in which $A$, $B$, and $C$ all share the first position.