The transport company where Napocan works needs to transport a billiard game. Napocan's task is to handle the transportation of the $2 \cdot n + 1$ balls of the game. These balls are numbered with distinct natural numbers from $1$ to $2 \cdot n + 1$. For their transportation, $n + 1$ boxes are used, numbered with distinct natural numbers from $1$ to $n + 1$. Each box can contain exactly two balls. Napocan is required to distribute the balls in the boxes such that:

* In the boxes numbered from $1$ to $n$, there are two balls each, and in the box with number $n + 1$, there is only one ball.
* For each box numbered from $1$ to $n$, the modulus of the difference between the numbers of the two balls in it is equal to the respective box number.

# Task

Determine a way to arrange the $2 \cdot n + 1$ balls in the $n + 1$ boxes to meet the imposed requirements.

# Input data

In the file `bile.in` there is a natural number $n$ with the meaning described in the statement.

# Output data

The file `bile.out` will contain $n + 1$ lines. The $i$-th line ($i = 1, 2, \dots, n$) will contain two values separated by a space that represent the numbers on the two balls in the box numbered $i$. The first value among these will be smaller than the second. On the line $n + 1$, there will be a single value representing the number on the ball assigned to the box $n + 1$.

# Constraints and clarifications

* $1 \leq N \leq 1\ 500\ 000$;

# Example

`bile.in`
```
2
```

`bile.out`
```
1 2
3 5
4
```
