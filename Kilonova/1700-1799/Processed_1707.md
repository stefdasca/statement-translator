```markdown
Let $N$ and $T$ be two natural numbers.

Determine the number of different solutions $S$ of the equation $x_1 \cdot x_2 \dots x_N = T$, in the set of natural numbers.

# Input data

The input file `ecuatie.in` contains on the first line the numbers $N$ and $T$ as described above, separated by a space.

# Output data

The output file `ecuatie.out` will contain on the first line the natural number $S$.

# Constraints and clarifications

* $1 \leq N \leq 10$
* $2 \leq T < 10^{15}$
* Two solutions $(x_1, x_2, \dots, x_N)$ and $(y_1, y_2, \dots, y_N)$ are considered different if ($x_1 \neq y_1$ or $x_2 \neq y_2$ or $ \dots $ or $x_N \neq y_N$)

# Example 1

`ecuatie.in`
```
2 28
```

`ecuatie.out`
```
6
```

## Explanation

$N = 2$ and $T = 28$

There are $6$ pairs $(x_1, x_2)$ of natural numbers with the property that $x_1 \cdot x_2 = 28$: $(1, 28)$, $(2, 14)$, $(4, 7)$, $(7, 4)$, $(14, 2)$, $(28, 1)$

# Example 2

`ecuatie.in`
```
3 10
```

`ecuatie.out`
```
9
```

## Explanation

$N = 3$ and $T = 10$

There are 9 triplets $(x_1, x_2, x_3)$ of natural numbers with the property that $x_1 \cdot x_2 \cdot x_3 = 10$: $(1, 1, 10)$, $(1, 2, 5)$, $(1, 5, 2)$, $(1, 10, 1)$, $(2, 1, 5)$, $(2, 5, 1)$, $(5, 1, 2)$, $(5, 2, 1)$, $(10, 1, 1)$
```