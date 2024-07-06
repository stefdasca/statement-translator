```markdown
Two binary matrices $A$ and $B$ are given, each with $N$ rows and $M$ columns. We define the Hamming distance between two subarrays determined by the top-left corners $(x_1, y_1)$ and bottom-right corners $(x_2, y_2)$ as the number of positions $(i, j)$ with the property that $x_1 \leq i \leq x_2$, $y_1 \leq j \leq y_2$ and $A_{i,j} \neq B_{i, j}$.
We will denote by $H(x_1, y_1, x_2, y_2)$ the Hamming distance between the two subarrays determined by the top-left corners $(x_1, y_1)$ and bottom-right corners $(x_2, y_2)$ in the matrices $A$ and $B$.

# Task

Calculate

$$
\sum_{1 \leq x_1 \leq x_2 \leq N} \left[ \sum_{1 \leq y_1 \leq y_2 \leq M} H(x_1, y_1, x_2, y_2) \right]
$$

# Input data

The first line contains the numbers $N$ and $M$. The next $N$ lines contain $M$ binary digits each, representing the elements of matrix $A$. The following $N$ lines contain $M$ binary digits each, representing the elements of matrix $B$.

# Output data

Print a single number, $ \sum_{1 \leq x_1 \leq x_2 \leq N} \sum_{1 \leq y_1 \leq y_2 \leq M} H(x_1, y_1, x_2, y_2) $.

# Constraints and clarifications

* $1 \leq N, M \leq 1\ 000$;
* $A_{i,j}, B_{i, j} \in \{ 0, 1 \}, \forall i \in \{ 1, 2, \dots, N \}, \forall j \in \{ 1, 2, \dots, M \}$;
* For $30$ points, $1 \leq N, M \leq 50$;
* For the remaining $70$ points, there are no additional constraints.

# Example

`stdin`
```
3 3
1 0 1
1 1 0
0 0 1
0 0 1
1 0 1
0 1 1
```

`stdout`
```
49
```

## Explanation

For example, for the subarray determined by points $(1, 2)$ and $(3, 3)$, the Hamming distance is $3$, because $A_{2,2} \neq B_{2,2}$, $A_{2,3} \neq B_{2,3}$ and $A_{3,2} \neq B_{3,2}$. The sum of the Hamming distances for all subarrays determined by two pairs of points is $49$.
```