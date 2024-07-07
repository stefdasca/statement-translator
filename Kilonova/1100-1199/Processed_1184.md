
A partition of a natural number $n$ is defined as writing $n$ in the form:

$n$ = $n_1$ + $n_2$ + $\\dots$ + $n_k$, ($k \geq 1$), where $n_1$, $n_2$, $\\dots$, $n_k$ are natural numbers that verify the following relationship: $n_1 \geq n_2 \geq \\dots \geq n_i \geq \\dots \geq n_k \geq 1$.

# Task

Given a natural number $n$, determine how many partitions of it can be written, according to the above requirements, knowing that any number $n_i$ in a partition must be an **odd** number.

# Input data

The file `partitie.in` contains on the first line the number $n$.

# Output data

The file `partitie.out` will contain on the first line the number of partitions of $n$ according to the problem requirements.

# Constraints and clarifications

* $1 \leq n \leq 160$;

# Example

`partitie.in`
```
7
```

`partitie.out`
```
5
```

## Explanation

The five partitions are:

* $1+1+1+1+1+1+1$; 
* $1+1+1+1+3$; 
* $1+1+5$; 
* $1+3+3$; 
* $7$;
