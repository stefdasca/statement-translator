# Task

A binary matrix is called connected if one can reach any value of $1$ from any other value of $1$ by only passing through values of $1$. A matrix containing only $0$s is considered connected.

You are given a binary matrix $C$ (not necessarily connected). Find two **connected** binary matrices $A$ and $B$ such that the following condition is met: $C_{ij}=1$ if and only if $A_{ij} \neq B_{ij}$.

**It is guaranteed that matrix $C$ contains at least one $0$ in each row.**

~[Conectate.png|align=center|width=50%]

# Input data

The first line contains the values $n$, $m$ (the dimensions of the matrix). The next $n$ lines each contain $m$ values from the set $\{0,1\}$, representing the elements of matrix $C$.

# Output data

If there is no solution, print $-1$. Otherwise, print matrix $A$ in the form of $n$ lines containing $m$ values from the set $\{0,1\}$, then print matrix $B$ in the same way. You may print a blank line between the two matrices, even if it is not necessary.

# Constraints and clarifications

For all tests, the condition $1 \le n, m \le 1000$ holds.

|#| Score | Constraints                                                  |
|-|---------|-------------------------------------------------------------|
|1|    4    | The values of $1$ in $C$ are connected and $2 \le n \le 100$. |
|2|    7    | The values of $0$ in $C$ are connected and $2 \le n \le 100$. |
|3|   17    | $n=1$                                                       |
|4|   21    | $n \ge 2$, and matrix $C$ is a checkerboard ($C_{ij}=1$ if and only if $i$ and $j$ have different parities).  |
|5|   51    | $n \ge 2$                                                    |

# Example 1

`stdin`
```
4 4
0 1 0 1
0 0 1 0
0 1 0 1
1 1 1 0
```

`stdout`
```
0 1 1 1
0 1 0 0
0 1 1 1
1 1 1 0

0 0 1 0
0 1 1 0
0 0 1 0
0 0 0 0
```

## Explanation

The example is illustrated in the image above. The top-left shows matrix $C$ (the cells marked with 'X' contain $1$). Below are the two matrices $A$ and $B$ (the colored cells contain $1$). The top-right shows the overlap of matrices $A$ and $B$. It can be seen how the cells marked with 'X' appear in exactly one of the matrices $A$ and $B$, according to the task.

This is **not** the only solution.

# Example 2

`stdin`
```
1 9
0 1 1 0 0 1 1 1 0
```

`stdout`
```
0 1 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 0
```

## Explanation

The blank line between the two matrices is optional.

# Example 3

`stdin`
```
1 9
0 1 1 0 1 0 1 1 0
```

`stdout`
```
-1
```

## Explanation

In this case, there is no solution.