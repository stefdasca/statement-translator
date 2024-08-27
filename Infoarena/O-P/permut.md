# Permut

Two arrays $(A \text{ and } B)$ of length $N$ are given. The task is to permute the two arrays such that $A_1 \cdot B_1 + A_2 \cdot B_2 + \dots + A_N \cdot B_N$ is as large as possible.

## Input data

The input file `permut.in` will contain on the first line a natural number $N$. The second line will contain $N$ integers representing array $A$, and the third line will contain another $N$ integers representing array $B$.

## Output data

The output file `permut.out` must print a value $VAL$ representing the maximum value for $A_1 \cdot B_1 + A_2 \cdot B_2 + \dots + A_N \cdot B_N$.

## Constraints

$1 \leq N \leq 100\ 000$

$-1\ 000\ 000 \leq A_i, B_i \leq 1\ 000\ 000$

For $10\%$ of the tests, $n \leq 6$

For another $10\%$ of the tests, $n \leq 10$

For another $20\%$ of the tests, $n \leq 1000$

For another $10\%$ of the tests, all values in the input file will be greater than $0$

For another $10\%$ of the tests, the number of elements greater than $0$ in array $A$ will be equal to the number of elements greater than $0$ in array $B$

## Example

`permut.in`
```
3
2 3 2
6 2 4
```

`permut.out`
```
30
```