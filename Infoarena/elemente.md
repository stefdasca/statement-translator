## Task

SMB has discovered a problem with arrays of numbers. Given an array $S$ with $N$ natural numbers, SMB needs to find the number of distinct subsequences that satisfy the property that the difference between any two numbers of the subsequence is at most equal to $K$.

## Input data

The input file `elemente.in` contains on the first line two natural numbers, $N$ and $K$, separated by a single space, having the meaning provided in the statement. On the following $N$ lines, the elements of the initial array follow, one per line.

## Output data

The output file `elemente.out` will contain a single natural number $Res$, which represents the remainder of dividing the number of distinct subsequences with the required property by $1\\ 000\\ 003$.

## Constraints and clarifications

$1 \leq N \leq 100\\ 000$

$1 \leq K \leq 1\\ 000\\ 000\\ 000$

The numbers in the array are natural numbers less than or equal to $2\\ 000\\ 000\\ 000$

A subsequence $A = (S_{i1}, S_{i2}, \dots, S_{ip})$ is considered different from a subsequence $B = (S_{j1}, S_{j2}, \dots, S_{jq})$ if $p$ is different from $q$ or if $q = p$ and there is at least one index $r$ such that $i_r \neq j_r$.

At least 40% of the tests will have $N \leq 1000$

## Example

`elemente.in`
```
4 5
8
1
2
3
```

`elemente.out`
```
9
```

## Explanation

The subsequences are: $8$, $1$, $2$, $3$, $1 2$, $1 3$, $2 3$, $1 2 3$ and $8 3$.