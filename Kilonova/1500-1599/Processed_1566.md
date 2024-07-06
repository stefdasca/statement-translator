# Task

We have a class with $N$ inventive students. For each of them, a non-zero natural number $v_k$ representing an attitude coefficient is known. The interactions within the group of students in the class produce significant side effects, and the school administration has defined a scalar measure called the danger indicator that measures the influence a student has on the other students in the class. The danger indicator associated with student $k$, $1 \leq k \leq N$, is obtained by calculating the greatest common divisor $d_{k,j}$ for each pair $(v_k, v_j)$, $1 \leq j \leq N$, $j \neq k$ and then summing the calculated values.

# Task

Calculate, for each student, the associated danger indicator.

# Input data

In the text file `pericol.in`, the first line contains the natural number $N$. The second line contains $N$ non-zero natural numbers, separated by a space, representing the attitude coefficients of the $N$ students.

# Output data

In the text file `pericol.out`, the first line will contain $N$ natural numbers, separated by a space, the $k$-th natural number representing the danger indicator associated with the $k$-th student.

# Constraints and clarifications

* $1 \leq N \leq 2\cdot 10^5$
* $1 \leq v_k \leq 10^7, 1 \leq k \leq N$

# Example

`pericol.in`
```
6
2 3 4 5 6 4
```

`pericol.out`
```
8 7 10 5 10 10
```

## Explanation

For example, the danger indicator of the $5$-th student is calculated as follows:
$(2, 6) + (3, 6) + (4, 6) + (5, 6) + (4, 6) = 2 + 3 + 2 + 1 + 2 = 10$