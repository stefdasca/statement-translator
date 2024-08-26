## Task

A sequence $A$ of $N$ distinct natural numbers is given. The task is to find two numbers in $A$ such that their least common multiple is as small as possible. 

## Input Data

The input file `minlcm.in` will contain on its first line the number of tests $T$. Each test has the following structure: the first line contains $N$, the number of numbers, and the second line contains the $N$ numbers. 

## Output Data

The output file `minlcm.out` will contain $T$ natural values, each on a separate line, representing the answer for the respective test. 

## Constraints

$1 \leq T \leq 25$

$2 \leq N \leq 100\,000$ 

$1 \leq A[i] \leq 100\,000$ for any $0 \leq i \leq N - 1$

The sum of values of $N$ within the same input file is less than or equal to $300\,000$. 

## Example

`minlcm.in`
```
1
3
10 11 14
```

`minlcm.out`
```
70
```