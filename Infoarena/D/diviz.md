# Diviz

Given a natural number $N$. Determine how many distinct non-zero natural numbers are subsequences of the number $N$, are divisible by $K$, and have between $A$ and $B$ digits.

## Input data

The first line of the file `diviz.in` contains three natural numbers, $K$, $A$, and $B$. The second line contains the number $N$ with at most 200 digits.

## Output data

The first line of the file `diviz.out` contains the number of existing subsequences with the required properties, modulo 30103 (i.e., the remainder of the division of the number of subsequences by 30103).

## Constraints and clarifications

$1 < K \leq 100$  
$0 < A \leq B \leq$ the number of digits of the number $N$  
Any natural number must start with a non-zero digit  
A number $X$ is a subsequence of the number $Y$ if and only if $X$ can be obtained from $Y$ by deleting some of its digits. For example, the number $508$ is a subsequence of the number $1530998$, because it can be obtained from $1530998$ by deleting the digits $1$, $3$, $9$, and $9$. Any number $X$ is its own subsequence.

## Example

`diviz.in`  
```
8 1 2
24
```
`diviz.out`  
```
1
```
`diviz.in`  
```
3 1 3
12055
```
`diviz.out`  
```
4
```

## Explanation

For the first example, the only possible number is $24$.

The 4 possibilities for the second example are $105$, $120$, $255$, $2055$.