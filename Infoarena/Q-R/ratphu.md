# Ratphu

Miruna has two natural numbers $N$ and $P$. She would like to know in how many ways she can permute the digits of $N$ so that the resulting new number is divisible by $P$.

## Input data

The input file `ratphu.in` contains on the first line the natural numbers $N$ and $P$ separated by a space.

## Output data

In the output file `ratphu.out` you will print a single number representing the number of ways the digits of $N$ can be permuted so that they meet the conditions in the statement.

## Constraints

$1 \leq N < 10^{18}$

$1 \leq P \leq 20$

## Example

`ratphu.in`

```
11 1
200 2
1234 2
```

`ratphu.out`

```
2
6
12
```

## Explanation

In the first example, we observe that we are interested in the number of permutations, not the number of distinct values that can be obtained. In the second example, we see that the digit $0$ can be at the beginning of the resulting numbers.