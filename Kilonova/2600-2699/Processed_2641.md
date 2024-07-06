We say that a sequence of numbers $(a_i, a_{i+1}, \dots, a_j)$ is **esm** if:

* it has at least $3$ elements
* there are at least two numbers $a_x$ and $a_y$ in that sequence, with $i \leq x < y < j$, such that $a_x \cdot a_y = a_j$

For example, the sequence $(54, 7, 22, 6, 9, 42)$ is **esm** because $7 \cdot 6 = 42$.

# Task

Given a sequence $a_1, a_2, \dots, a_n$ of natural numbers. Determine:

1. The number of **esm** sequences in the array of length $3$.
2. The number of **esm** sequences in the array that end with $a_n$.
3. The number of **esm** sequences in the array.

# Input data

The input file `esm.in` will contain on the first line a natural number $C$, the second line will contain the natural number $n$, and on the third line, separated by spaces, the elements of the array $a_1, a_2, \dots, a_n$.

# Output data

The output file `esm.out` will contain a single natural number $X$:

* If $C = 1$, then $X$ will be the number of **esm** sequences in the array of length $3$.
* If $C = 2$, then $X$ will be the number of **esm** sequences in the array that end with $a_n$.
* If $C = 3$, then $X$ will be the number of **esm** sequences in the array.

# Constraints and clarifications

* $C \in \{1, 2, 3\}$
* $3 \leq n \leq 100 \ 000$
* $1 \leq a_i \leq 100 \ 000$, $\forall i \in \{1, 2, \dots, n\}$
* The length of a sequence is equal to the number of elements in the sequence

|#|Score|Constraints|
|-|-|--------|
|1|30|$C = 1$|
|2|30|$C = 2$|
|3|40|$C = 3$|

# Example 1

`esm.in`
```
1
8
2 3 6 18 1 18 3 5
```

`esm.out`
```
3
```

## Explanation

The **esm** sequences in the array of length $3$ are:

* $(2, 3, 6)$;
* $(3, 6, 18)$;
* $(18, 1, 18)$.

# Example 2

`esm.in`
```
2
8
5 8 20 2 4 7 5 40
```

`esm.out`
```
3
```

## Explanation

The **esm** sequences in the array that end with $40$ are:

* $(5, 8, 20, 2, 4, 7, 5, 40)$;
* $(8, 20, 2, 4, 7, 5, 40)$;
* $(20, 2, 4, 7, 5, 40)$.

# Example 3

`esm.in`
```
3
8
2 2 4 8 1 8 16 7
```

`esm.out`
```
9
```

## Explanation

The **esm** sequences in the array are:

* $(2, 2, 4)$;
* $(2, 2, 4, 8)$;
* $(2, 4, 8)$;
* $(2, 2, 4, 8, 1, 8)$;
* $(2, 4, 8, 1, 8)$;
* $(4, 8, 1, 8)$;
* $(8, 1, 8)$;
* $(2, 2, 4, 8, 1, 8, 16)$;
* $(2, 4, 8, 1, 8, 16)$.