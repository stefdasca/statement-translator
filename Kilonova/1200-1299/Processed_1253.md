In Târgoviște, in the Royal Fortress, a document was discovered containing several natural numbers. Mircea the Younger, passionate about arithmetic, observed the property that sometimes a number in the sequence can be written as the arithmetic mean of two numbers from two other positions in the sequence. The question that Mircea the Younger asks himself is how many times this property appears in the sequence.

# Task

Write a program that determines the total number of triplets $(i, j, k)$ with $(i \neq j, i \neq k , j < k)$ such that $v_i$ is the arithmetic mean of $v_j$ and $v_k$.

# Input data

The input file `medie.in` contains on the first line a value $n$ representing the number of numbers in the sequence, and on the next $n$ lines one value $v_i$ per line, representing the values in the sequence. The values in the sequence are not necessarily distinct.

# Output data

The output file `medie.out` will contain a single line with a value $max$, representing the total number of determined triplets.

# Constraints and clarifications

* $1 \leq n \leq 9\ 000$
* $1 \leq v_i \leq 7\ 000$

# Example 1

`medie.in`
```
5
1
1
1
1
1
```

`medie.out`
```
30
```

## Explanation

Each value $1$ can be written as the mean of any two values from the other $4$ possible. The triplets counted are: $(1, 2, 3)$, $(1, 2, 4)$, $(1, 2, 5)$, $(1, 3, 4)$, $(1, 3, 5)$, $(1, 4, 5)$, $(2, 1, 3)$, $(2, 1, 4)$, $(2, 1, 5)$, $(2, 3, 4)$, $(2, 3, 5)$, $(2, 4, 5)$, $(3, 1, 2)$, $(3, 1, 4)$, $(3, 1, 5)$, etc.

# Example 2

`medie.in`
```
3
4
2
1
```

`medie.out`
```
0
```

## Explanation

* The value $4$ is not the arithmetic mean of the values $2$ and $1$;
* The value $2$ is not the arithmetic mean of the values $4$ and $1$;
* The value $1$ is not the arithmetic mean of the values $4$ and $2$.

# Example 3

`medie.in`
```
6
3 
1
6
4
5
2
```

`medie.out`
```
6
```

## Explanation

* $2 = (1 + 3) / 2$
* $3 = (4 + 2) / 2; (1 + 5) / 2$
* $4 = (3 + 5) / 2; (6 + 2) / 2$
* $5 = (6 + 4) / 2$

The triplets are: $(6, 1, 2)$, $(1, 4, 6)$, $(1, 2, 5)$, $(4, 1, 5)$, $(4, 3, 6)$, $(5, 3, 4)$.