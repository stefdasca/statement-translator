# Cmmp

For any natural number $x$, we define the operation "cmmp" where we add digits to the left of $x$, to the right of $x$, or to both ends of $x$, such that the resulting number is a perfect square and as small as possible. You are given $N$ natural numbers $s_1,s_2,\dots,s_N$.

## Task

For each number $s[k]$, $1 \leq k \leq N$, determine the smallest perfect square that can be obtained by applying the "cmmp" operation.

## Input data

The input file `cmmp.in` contains on the first line the number $N$. The second line contains $N$ natural numbers separated by spaces.

## Output data

The output file `cmmp.out` will contain, in the order corresponding to the input and separated by spaces, the $N$ numbers obtained from the given numbers by applying the "cmmp" operation.

## Constraints

$1 \leq N \leq 10^5$  
$0 \leq s[k] < 10^5$  

For 20% of the tests:  
$0 \leq s[k] < 10^2$  

For 20% of the tests:  
$0 \leq s[k] < 10^3$  

If the given number is a perfect square, then the "cmmp" operation leaves it unchanged. 

## Example

`cmmp.in`
```
4
21 0 19 80
```
`cmmp.out`
```
121 0 196 2809
```

## Explanation

$121 = 11^2$, $0 = 0^2$, $196 = 14^2$, $2809 = 53^2$