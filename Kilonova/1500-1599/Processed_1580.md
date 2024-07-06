```markdown
We assume we have two boxes noted $A$ and $B$. Box $A$ contains $N$ balls numbered with distinct natural numbers: $0, 1, 2, \dots N-1$. Box $B$ is empty.

We say that a ball in a box is the **special** ball of this box if the number $X$ with which this ball is numbered is equal to the arithmetic mean of the numbers on the other balls in the box.

At some point, someone moves the ball with number $K$ from box $A$ into box $B$.

You are asked to choose another $K$ balls from box $A$ to move into box $B$ so that box $B$ contains $K + 1$ balls, and the ball with number $K$ is the special ball of box $B$.

# Task

Write a program that reads the numbers $N$ and $K$, then determines:
1. if, before any balls are moved from box $A$ to box $B$, there exists a special ball in box $A$; if so, the program determines the number $X$ on which this special ball is numbered.
2. the **smallest** (in lexicographic order) **strictly increasing sequence** of the numbers of the $K$ balls that can be moved from box $A$ to box $B$ so that the ball with number $K$ is the special ball of box $B$.
3. the **largest** (in lexicographic order) **strictly increasing sequence** of the numbers of the $K$ balls that can be moved from box $A$ to box $B$ so that the ball with number $K$ is the special ball of box $B$.

# Input data

The input file `bile.in` contains on the first line three natural numbers $C, N$ and $K$, separated by spaces. $C$ represents the task that needs to be resolved (1, 2, or 3), and $N$ and $K$ have the meaning from the statement.

# Output data

The output file `bile.out` will contain:
* if $C = 1$, on the first line, the natural number $X$ representing the number of the special ball from box $A$ or the value $-1$ if box $A$ does not contain such a ball (representing the answer to task 1);
* if $C = 2$, on the first line, **an increasing sequence of $K$** natural numbers, separated by spaces (representing the answer to task 2);
* if $C = 3$, on the first line, **an increasing sequence of $K$** natural numbers, separated by spaces (representing the answer to task 3);

# Constraints and clarifications

* $N$ natural number, $4 \leq N \leq 100\ 000$
* $K$ a natural number $2 \leq K \leq \frac{N}{2}$
* The sequence $y_1, y_2, \dots y_k$ is **lexicographically smaller** than the sequence $z_1, z_2, \dots z_k$ if there exists an index $p$, $1 \leq p \leq K$, **such that**: $y_1 = z_1, y_2 = z_2, \dots y_{p-1} = z_{p-1}$ and $y_p < z_p$
* 20 points are awarded for task 1, and 40 points are awarded for each of tasks 2 and 3.

# Example 1

`bile.in`
```
1 9 3
```

`bile.out`
```
4
```

## Explanation

Task 1 is resolved.
$N = 9$.
We have 9 balls numbered $0, 1, 2, 3, 4, 5, 6, 7, 8$.
The special ball is $X = 4$ because:
$X = \frac{(0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)}{8} = \frac{32}{8} = 4$.

# Example 2

`bile.in`
```
1 8 3
```

`bile.out`
```
-1
```

## Explanation

Task 1 is resolved.
$N = 8$.
We will write the value $-1$ in the output file because box $A$ does not contain any special ball.

# Example 3

`bile.in`
```
2 8 3
```

`bile.out`
```
0 2 7
```

## Explanation

Task 2 is resolved.
$N = 8$.
The strictly increasing sequences of the numbers of the balls that can be moved into box $B$, alongside the special ball $K = 3$, are: $0, 2, 7$ or $0, 4, 5$ or $1, 2, 6$, because:
$3 = \frac{(0 + 2 + 7)}{3} = \frac{(0 + 4 + 5)}{3} = \frac{(1 + 2 + 6)}{3}$
The smallest strictly increasing sequence in lexicographic order is $0, 2, 7$.

# Example 4

`bile.in`
```
3 8 3
```

`bile.out`
```
1 2 6
```

## Explanation

Task 3 is resolved.
$N = 8$.
The strictly increasing sequences of the numbers of the balls that can be moved into box $B$, alongside the special ball $K = 3$, are: $0, 2, 7$ or $0, 4, 5$ or $1, 2, 6$, because:
$3 = \frac{(0 + 2 + 7)}{3} = \frac{(0 + 4 + 5)}{3} = \frac{(1 + 2 + 6)}{3}$
The largest strictly increasing sequence in lexicographic order is $1, 2, 6$.
```
