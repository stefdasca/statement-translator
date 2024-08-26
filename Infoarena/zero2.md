# Zero 2

The tests for this problem are not well designed to correctly distinguish inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem! Determine the number of trailing zeros in the representation of the value $1! * 2! * \dots * N!$ in base $B$.

## Input data

The input file `zero2.in` will contain 10 lines, each containing two natural numbers $N$ $B$, separated by spaces.

## Output data

The output file `zero2.out` will contain 10 lines, each containing the answer for the corresponding line in the input file.

## Constraints

$2 \leq N$
$B \leq 1\ 000\ 000\ 000$

For 50% of the tests
$N, B \leq 100\ 000$

and for 70% of the tests
$N, B \leq 1\ 000\ 000$

$N! = 1 * 2 * 3 * \dots * N$

For each correct answer in the output file, 10% of the test score will be awarded.

It is guaranteed that the result is less than $2^{ 63 }$

## Example

`zero2.in`
`zero2.out`
```
5 10
5
5 9
5
5 8
2
5 7
0
5 6
1
5 5
0
5 4
3
5 3
8
5 2
8
```

## Explanation

$1! * 2! * 3! * 4! * 5! = 34560$ in base $10$

$1! * 2! * 3! * 4! * 5! = 52360$ in base $9$

$1! * 2! * 3! * 4! * 5! = 103400$ in base $8$

$1! * 2! * 3! * 4! * 5! = 202521$ in base $7$

$1! * 2! * 3! * 4! * 5! = 424000$ in base $6$

$1! * 2! * 3! * 4! * 5! = 2101220$ in base $5$

$1! * 2! * 3! * 4! * 5! = 20130000$ in base $4$

$1! * 2! * 3! * 4! * 5! = 1202102000$ in base $3$

$1! * 2! * 3! * 4! * 5! = 1000011100000000$ in base $2$