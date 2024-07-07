
Gardener Marian has at his disposal a permutation with $n$ elements and a natural number $S$ which initially has the value $0$. Marian performs $n$ operations as follows:

* chooses the minimum element from the permutation, let $x$ be its position within the permutation
* eliminates this element from the permutation, and moves all elements from its left to the end of the permutation (preserving the order of the elements from the left)
* adds $x$ to $S$.

Thus, after the permutation becomes empty, $S$ will have a certain value.

# Task
Determine the value of $S$ after gardener Marian finishes executing all $n$ operations.

# Input data

The input file `permsort.in` will contain on the first line a natural number $n$, representing the number of elements in the permutation, and on the second line contains $n$ distinct natural numbers between $1$ and $n$, separated by a space, representing the permutation on which Marian applies the operations.

# Output data

The output file `permsort.out` will contain on the first line a natural number representing the value of $S$ after the execution of the $n$ operations.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000 \ 000$;
* for $30\%$ of the tests, $1 \leq n \leq 5 \ 000$

# Example 1

`permsort.in`
```
5
5 4 1 3 2
```

`permsort.out`
```
11
```

## Explanation

In the first example:

1) The minimum element in the permutation is $1$ and it is at position $3$. After this step, $S$ becomes $0+3=3$, and the permutation remains (elements to the left of $1$ move in the same order to the end): $(3 \ 2 \ 5 \ 4)$.
2) The minimum element in the permutation is $2$ and it is at position $2$. After this step, $S$ becomes $3+2=5$, and the permutation remains: $(5 \ 4 \ 3)$.
3) The minimum element in the permutation is $3$ and it is at position $3$. After this step, $S$ becomes $5+3=8$, and the permutation remains: $(5 \ 4)$.
4) The minimum element in the permutation is $4$ and it is at position $2$. After this step, $S$ becomes $8+2=10$, and the permutation remains: $(5)$.
5) The minimum element in the permutation is $5$ and it is at position $1$. After this step, $S$ becomes $10+1=11$, and the permutation becomes empty.

The final value of $S$ is $11$.

# Example 2

`permsort.in`
```
7
7 5 6 3 1 2 4
```

`permsort.out`
```
16
```

## Explanation
$S = 5 + 1 + 5 + 1 + 2 + 1 + 1$
