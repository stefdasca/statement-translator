# Bilute2

X and Y are playing with $N$ marbles, each marble having a non-zero digit written on it. Being inventive, they divided the $N$ marbles into two piles such that the average value of X's pile is equal to the average value of Y's pile. The average value of a pile is equal to the sum of all numbers in the pile divided by the number of its elements. Given the $N$ values written on the marbles, find in how many ways the marbles can be divided into two piles with equal average values. Since this number can be very large, display only the remainder of this number when divided by $666013$.

## Input data

The input file `bilute2.in` contains on the first line the natural number $N$, and the second line contains $N$ natural numbers separated by exactly one space, representing the values written on the $N$ marbles.

## Output data

The output file `bilute2.out` contains a single number, representing the number of ways to divide the marbles into piles as described in the task above.

## Constraints and clarifications

$2 \leq N \leq 750$ 

Two configurations are considered distinct if there is at least one marble that is in different piles.

For a configuration, the order of distribution of the piles for X and Y is significant.

Each pile must contain at least one marble.

Each marble must be in exactly one of the two piles.

For $15\%$ of tests $N \leq 20$.

For $25\%$ of tests the value on the marbles $\leq 3$.

## Example

`bilute2.in`
```
6
1 2 3 4 5 6
```
`bilute2.out`
```
6
```

## Explanation

$G_X =[1,2,5,6]$; $G_Y =[3,4]$, where $(1+2+5+6)/4=(3+4)/2$ 

$G_X =[1,3,4,6]$; $G_Y =[2,5]$

$G_X =[1,6]$; $G_Y =[2,3,4,5]$

$G_X =[2,3,4,5]$; $G_Y =[1,6]$

$G_X =[2,5]$; $G_Y =[1,3,4,6]$

$G_X =[3,4]$; $G_Y =[1,2,5,6]$

`bilute2.in`
```
6
1 1 2 2 3 3
```
`bilute2.out`
```
22
```