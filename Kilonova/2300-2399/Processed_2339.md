```markdown
Let $n$ be a natural number and $p=(p_1, p_2, \dots, p_n)$ a permutation of order $n$. We define the degree of a permutation as the smallest natural number $k>0$, such that $p^k = p \circ p \circ p \circ \dots \circ p = e$ (k times), where $e$ is the identity permutation, i.e. the permutation for which $e(i)=i$, for any $i=1, 2, \dots, n$.

# Task

For a given $n$, determine a permutation of order $n$ with the maximum degree. If there are multiple solutions, determine the first in lexicographic order.

# Input data

The input file `perm.in` contains a single line with the non-zero natural number $n$.

# Output data

The output file `perm.out` will contain a single line where $n$ distinct natural numbers between $1$ and $n$ are written, separated by a space, representing the first permutation with the maximum degree in lexicographic order.

# Constraints and clarifications

* $1 \leq N \leq 2\ 000$;
* By the operation $ \circ $ we understand the composition of functions. More precisely $p \circ p(i) = p(p(i))$, for any $i=1, 2, \dots, n$.

# Example 1

`perm.in`
```
5
```

`perm.out`
```
2 1 4 5 3
```

## Explanation

The permutation $(2, 1, 4, 5, 3)$ has a degree of $6$ (maximum possible). There are other solutions, but this is the smallest in lexicographic order.

# Example 2

`perm.in`
```
14
```

`perm.out`
```
2 3 1 5 6 7 4 9 10 11 12 13 14 8
```
```