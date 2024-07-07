
A natural number $N$ is considered. A **good partition** of $N$ is called a sequence of non-zero natural numbers $x_1, x_2, ..., x_k$ with the following properties:
* $N = x_1 + x_2 + ... + x_k$
* $\frac{1}{x_1} + \frac{1}{x_2} + ... + \frac{1}{x_k} = 1$

# Task

For a given natural number $N$, it is required to determine a good partition.

# Input data

The input file `partitionare.in` contains on the first line the natural number $N$.

# Output data

In the output file `partitionare.out`, print on the first line the *good partition* of $N$, with its terms separated by a space.

# Constraints and clarifications

* $100 \leq N \leq 10 \ 000 \ 000$ for all tests of the problem, except for the example below.
* The solution is not unique! Any correct solution is accepted.
* The order of numbers in the array does not matter.

# Example

`partitionare.in`
```
33
```

`partitionare.out`
```
3 9 3 9 9
```

## Explanation

The sequence of numbers $3 \ 9 \ 3 \ 9 \ 9$ forms a good partition because:
$3 + 9 + 3 + 9 + 9 = 33$
$\frac{1}{3} + \frac{1}{9} + \frac{1}{3} + \frac{1}{9} + \frac{1}{9} = 1$
