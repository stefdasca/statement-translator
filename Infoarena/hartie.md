# Paper

Company X produces sheets of paper of a single size: $6 \times 6$ (measured in the preferred unit). Company Y needs a varied number of sheets of paper of dimensions $1 \times 1$, $2 \times 2$, $3 \times 3$, $4 \times 4$, $5 \times 5$, $6 \times 6$, which they want to purchase from Company X. More specifically, Company Y needs $x(i)$ sheets of paper of dimension $i \times i$ ($1 \leq i \leq 6$). To meet Company Y's demand, Company X will produce a number of sheets of paper of dimension $6 \times 6$, and then cut from these sheets the dimensions required by Company Y. Any shapes with sides parallel to the sides of the sheet can be cut from a sheet of paper. Determine the minimum number of sheets of paper of dimension $6 \times 6$ that Company X needs to produce to completely satisfy Company Y's demand.

## Input data

The input file `hartie.in` will contain multiple tests (the number is not specified). Each test is described on a single line of the input file and contains 6 numbers, separated by a space: $x(1)$, $x(2)$, $x(3)$, $x(4)$, $x(5)$, $x(6)$.

## Output data

In the output file `hartie.out` you will print, for each test in the input file (and in the order the tests are given in the input file), the minimum number of sheets of paper of dimension $6 \times 6$ that Company X needs to produce to satisfy Company Y's demand.

## Constraints and clarifications

$0 \leq x(i) \leq 100$

The number of tests in the input file is at most 2500.

The possible scores for this problem are: 0 and 100.

## Example

`hartie.in` 
```
1 2 3 0 0 0
7 5 1 2 0 0
```

`hartie.out`
```
2
3
```