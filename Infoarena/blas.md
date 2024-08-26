Blas

Everyone knows the base-$2$ representation of integers. In this problem, we will start with the number $1$ in base $2$ written separately on a row: $1$ We notice that we have written a $'1'$ above so in the next step we will write: $1$ $1$ (a $'1'$) Now we have written two $'1'$s and two is $'10'$ $(2)$, so we will write: $1$ $0$ $1$ (two $'1'$s) Reading the previous row we notice one $'1'$, one $'0'$ and another $'1'$, so we get: $1$ $1$ $1$ $0$ $1$ $1$ And we can continue as follows: $1$ $1$ $1$ $1$ $0$ $1$ $0$ $1$ (three $=$ $11$ $(2)$ of $1$, one $0$ and two $=$ $10$ $(2)$ of $1$) $1$ $0$ $0$ $1$ $1$ $0$ $1$ $1$ $1$ $0$ $1$ $1$ $1$ $1$ $1$ $0$ $0$ $1$ $0$ $1$ $1$ $0$ $1$ $1$ $1$ $1$ $0$ $1$ $0$ $1$ $\dots$ The problem requires calculating the number of binary digits needed in the $N$-th element of the sequence.

## Task

The input file `blas.in` contains the number of tests $T$ on the first line. The following $T$ lines contain different values for $N$.

## Input data

The input file `blas.in` contains on the first line the number of tests $T$. The next $T$ lines contain different values for $N$.

## Output data

The output file `blas.out` should contain $T$ lines with the answer to each test in order. For each test, the answer is the number of binary digits that appear in the $N$-th sequence, modulo $10067$. Print the result in base $10$.

## Constraints and clarifications

$1 \leq T \leq 10$ 

$1 \leq N \leq 1000\ 000\ 000$ 

## Example

`blas.in`
```
2
1
7
```
`blas.out`
```
1
18
```

## Explanation

The first sequence $"1"$ contains a single binary digit, the $7$-th sequence $"1 1 1 0 0 1 0 1 1 0 1 1 1 1 0 1 0 1"$ contains $18$ binary digits.