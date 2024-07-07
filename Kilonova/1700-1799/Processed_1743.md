
Two natural numbers $N$ and $K$ are given.

# Task

Determine the number of sequences of length $N$ consisting only of the signs `+` and `–` in which $K$ signs `–` do not appear on consecutive positions.

# Input data

The input file `minusk.in` contains on the first line 2 natural numbers separated by a space, $N$ and $K$, with the significance given in the statement.

# Output data

The output file `minusk.out` will contain on the first line a single natural number representing the required value, modulo $2 \ 011$.

# Constraints and clarifications

* $1 \leq K \leq N \leq 1 \ 000 \ 000$;
* for $30\%$ of the tests $N \leq 10$
* for $70\%$ of the tests $N \leq 1 \ 000$

# Example

`minusk.in`
```
4 2
```

`minusk.out`
```
8
```

## Explanation

The $8$ sequences are: `++++`, `+++-`, `++-+`, `+-++`, `-+++`, `+-+-`, `-++-`, `-+-+`. In none of these sequences do we have two or more `–` characters on consecutive positions.
