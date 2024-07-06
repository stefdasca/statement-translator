```markdown
# Statement
To celebrate the achievements of those who qualified for the county stages of this year's Olympiads, the students of a class decided to order cakes during the homeroom period. A class consists of $N$ students, and each will express their opinion on exactly two cakes out of the $M$ available at the pastry shop near the school. Each student expresses their opinion on the cakes as follows: "+ x" if they like cake $x$, or "- x" if they do not like cake $x$ (where $x$ is a number from $1$ to $M$).

# Task
Find out which cakes will be ordered so that at least one of each student's preferences is satisfied. If such an order cannot be established, the students will no longer buy cakes.

# Input data
The first line contains two non-negative natural numbers, $N$ and $M$. The next $N$ lines will contain the two preferences of the current student, in the form "+ x" (they like cake $x$) or "- x" (they do not like cake $x$).

# Output data
The first line contains $M$ answers. Each cake will correspond to `YES` (if the cake will be ordered) or `NO` (if the cake will not be ordered).

# Constraints and clarifications
- $1 \leq N, M \leq 10^{5}$
- $1 \leq x \leq M$, for any cake.
- If the students do not order cakes, $-1$ will be displayed.
- The solution is not unique.

# Example

`stdin`
```
7 6
+ 4 + 6
+ 3 + 2
- 6 + 5
+ 2 + 6
- 1 - 6
- 3 + 5
+ 1 + 2
```

`stdout`
```
YES YES YES YES YES NO
```
```