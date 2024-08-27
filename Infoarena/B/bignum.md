## Bignum

We will denote a number in base 2 with the digits $b[ 1 ], \dots, b[k]$ as $b[ 1 ] \dots b[k]_2$. For example, $101_2$ is the number $1 + 2^2 = 5$. We define the ordering of a number in base 2 as the number resulting from sorting its digits in increasing order. For example, $ordering(101_2) = 011_2 = 1 + 2^1 = 3$, or $ordering(10101_2) = 00111_2 = 1 + 2^1 + 2^2 = 7$. A number $N_2$ in base 2 is given. Calculate the sum $ordering(1_2) + \dots + ordering(N_2) \mod 10^9 + 7$

## Input data

The first line of the input file contains the number $N_2$ in base 2.

## Output data

The output file will contain the described sum, in base 10.

## Constraints and clarifications

For tests worth 20 points,
$N_2$ has at most 20 digits in base 2.

For other tests worth 30 points,
$N_2$ has at most $2000$ digits in base 2.

For other tests worth 50 points,
$N_2$ has at most $200000$ digits in base 2.

## Example

```
bignum.in
100
```
```
bignum.out
6
```

```
bignum.in
11110000
```
```
bignum.out
5040
```

## Explanation

We observe that:
$ordering(1_2) + ordering(10_2) + ordering(11_2) + ordering(100_2) = 1_2 + 01_2 + 11_2 + 001_2 = 1 + 1 + 3 + 1 = 6$