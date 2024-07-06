```markdown
Through $fibosir(N)$ we understand a sequence constructed by adding at the end (concatenation) the first $N$ non-zero terms of the Fibonacci sequence defined as follows:

* $F_1 = 1$
* $F_2 = 1$
* $F_N = F_{N-1} + F_{N-2}$

For example, if $N = 8$ the constructed fibosir is: $fibosir(8) = 1123581321$.

# Task

For a given natural value $N$, remove $M$ disjoint subarrays of length $K$ each from the constructed fibosir, such that the number formed by the remaining digits in the fibosir is maximum.

# Input data

The input file `fibosir.in` contains on the first line three natural numbers $N$, $M$, and $K$ separated by a space with the meaning given in the statement.

# Output data

The output file `fibosir.out` will contain on the first line the maximum number obtained by removing $K$ disjoint subarrays of length $K$ from $fibosir(N)$.

# Constraints and clarifications

* $0 < N \leq 2\ 000$
* $0 < M \cdot K <$ length of $fibosir(N)$
* By subarray of length $K$ we understand a subsequence of $K$ digits located at consecutive positions in the sequence

# Example

`fibosir.in`
```
8 3 2 
```

`fibosir.out`
```
5821
```

## Explanation

$fibosir(8)$: $1123581321$ removing $3$ subarrays of length $2$: $11$, $23$, $13$
```