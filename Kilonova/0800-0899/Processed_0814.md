The inhabitants of the planet Eudora use a rather peculiar representation of natural numbers, such that any natural number is written noting how many thousands, hundreds, tens, and units it contains. For example, the number $3207$ can be represented in multiple equivalent ways: $3m2s7u$ ($3$ thousands $2$ hundreds and $7$ units), $32s0z7u$ ($32$ hundreds $0$ tens and $7$ units), $32s7u$, $3207u$, etc.

To compare two natural numbers, Eudorans use the signs `<` and `>`, which have the same meaning as on Earth. To calculate the sum of two natural numbers, they use the sign `+`.

To test the abilities of earthlings in working with natural numbers, the Eudorans have sent to Earth a text file containing $N$ lines, each line being a comparison of the form: `expression1 > expression2` or `expression1 < expression2`.

Note that a comparison consists of two expressions separated by the sign `<` or the sign `>`.

An expression is composed of a natural number or a sum of two or more natural numbers, all written in Eudoran form. The file does not contain space characters.

# Task

Write a program that determines how many of the given comparisons use the sign `<`, as well as the truth value of each comparison among the given $N$ (displaying $0$ if the comparison is false, respectively $1$ if the comparison is true).

# Input data

The input file `comp.in` contains on the first line the non-zero natural number $N$, representing the number of comparisons, and on each of the following $N$ lines a string corresponding to a comparison.

# Output data

The output file `comp.out` will contain on the first line a natural number representing the number of comparisons in which the sign `<` is used. It follows $N$ lines, each line containing only the value $0$ or the value $1$. The value on the $i$-th line among the $N$ is $0$ if the $i$-th comparison in the input file is false, respectively $1$ otherwise.

# Constraints and clarifications

* $0 < N \leq 1\ 000$;
* The numbers in the file do not exceed in value the Eudoran number $1000m1000s1000z1000u$.
* The length of each line in the file is at most $250$.

# Example

`comp.in`
```
2
120u+7z13u>2s13u
1m11s+2z+1u<2m1s2z5u+0u
```

`comp.out`
```
1
0
1
```

## Explanation

One comparison uses the `<` sign.

The first comparison is false ($203 > 213$).

The second comparison is true ($2121 < 2125$).

