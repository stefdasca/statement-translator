Éles received the following assignment: *"Given an array $A$ with $N$ distinct natural numbers, calculate the sum of the digits of each element in the array"*.

After finishing his assignment, he notices that there are several pairs of indices ($i, j$) for which, if $A_i < A_j$, then $S_i > S_j$, where $S_i$ represents the sum of the digits of $A_i$. He will call these special index pairs.

# Task

After quickly completing the assignment, Éles receives an additional task with two requirements:

1. Determine two numbers in the array $A$ whose corresponding indices form a special pair.
2. How many special index pairs ($i, j$) are there in the array $A$?

Help Éles solve the additional tasks.

# Input data

The first line of the file `pseudocmp.in` contains two natural numbers: $T$ and $N$. The next line contains $N$ natural numbers, separated by a space, representing the values in the array $A$. The number $T$ denotes the task number.

# Output data

In the first line of the file `pseudocmp.out`:

If $T = 1$, it contains two natural numbers $x, y$, with $x < y$, separated by a space, representing the answer for task $1$ if there is a solution, or $-1$ if there is no solution. If there are multiple solutions, any of them will be accepted.
If $T = 2$, it contains a single natural number, representing the answer for task $2$.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* $1 \leq A_i \leq 1\ 000\ 000$; 

|#|Score|Constraints|
|-|-|--------|
|1|15|$T = 1$ and $N \leq 1\ 000$|
|2|25|$T = 1$ and $N \leq 10^5$|
|3|25|$T = 2$ and $N \leq 1\ 000$|
|4|35|$T = 2$ and $N \leq 10^5$|

# Example 1

`pseudocmp.in`
```
1 6
213 123 523 51 99 92
```

`pseudocmp.out`
```
99 123
```

## Explanation

$99$ is smaller than $123$ and the sum of the digits of $99$ is $18$, while the sum of the digits of $123$ is $6$, $18 > 6$.

# Example 2

`pseudocmp.in`
```
2 6
213 123 523 51 99 92
```

`pseudocmp.out`
```
6
```

## Explanation

The $6$ pairs of indices are as follows: $(5, 1), (5, 2), (5, 3), (6, 1), (6, 2), (6, 3)$.

# Example 3

`pseudocmp.in`
```
1 5
6 5 2 1 3
```

`pseudocmp.out`
```
-1
```