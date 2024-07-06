```markdown
A non-zero natural number $N$ is given, followed by $M$ pairs of natural numbers $(x_1, y_1)$, $(x_2, y_2)$, $\dots$, $(x_m, y_m)$ with $x_1 \leq x_2 \leq \dots \leq x_m$.

Each pair $(x_i, y_i)$ represents a set of consecutive natural numbers where $x_i$ represents the minimum value and $y_i$ the maximum value.

# Task

Determine and print the number of elements from the set $\{1, 2, 3, \dots, n\}$ that do not belong to any of the $M$ sets.

# Input data

The file `multimi.in` contains on the first line 2 natural numbers $N$ and $M$, and on the following $M$ lines, each contains a pair of natural numbers $(x_i, y_i)$ with the meaning described above. Numbers on the same line are separated by a single space.

# Output data

The file `multimi.out` contains a natural number representing the answer to the problem's task.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* $0 \leq M \leq 100\ 000$;
* For any set of the form $(x_i, y_i)$, $1 \leq x_i \leq y_i \leq n$;
* For 33 points, any two sets do not have common elements between them;
* For another 33 points $M \leq 100$, $N \leq 5\ 000$, and the sets may have common elements.

# Example 1

`multimi.in`
```
8 3
1 3
6 7
7 8
```

`multimi.out`
```
2
```

## Explanation

From the numbers from $1$ to $8$, only $4$ and $5$ do not belong to any set.

# Example 2

`multimi.in`
```
8 3
1 4
2 5
7 8
```

`multimi.out`
```
1
```

## Explanation

From the numbers from $1$ to $8$, only $6$ does not belong to any set.
```
