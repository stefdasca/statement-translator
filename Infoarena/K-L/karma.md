## Task

Given a matrix with $N$ rows and $M$ columns containing open and closed parentheses (we only have elements of the type "(" and ")"), in how many ways can the columns of the matrix be permuted so that each row becomes a correct parenthesis sequence?

## Input data

The input file `karma.in` will contain on the first line $N$ and $M$. The next $N$ lines will contain one string of $M$ parentheses each.

## Output data

The output file `karma.out` will contain a single number representing the answer modulo $1\ 000\ 000\ 007$.

## Constraints

$1 \leq N$

$1 \leq M \leq 20$

## Example

`karma.in`

```
2 4
(())
()()
```

`karma.out`

```
2
```

`karma.in`

```
3 8
(((())))
()()(())
))((()()
```

`karma.out`

```
168
```