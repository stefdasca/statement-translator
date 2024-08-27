# Digits3

You are given 2 integers $A$ and $B$. You are asked to determine how many numbers can be written as the product of the digits of at least one integer in the interval $[10^A, 10^B)$. For example, $30$ can be written as the product of the digits of the number $325$, but $66$ cannot be written as the product of the digits of any integer.

## Input data

The first line of the file `cifre3.in` will contain 2 integers $A$ and $B$.

## Output data

The file `cifre3.out` must contain a single integer representing the number of integers that can be written as the product of the digits of at least one integer in the interval $[10^A, 10^B)$.

## Constraints and clarifications

$0 \leq A < B \leq 20$

## Example

`cifre3.in`
```
0 1
```
`cifre3.out`
```
9
```

`cifre3.in`
```
0 2
```
`cifre3.out`
```
37
```

All numbers from $1$ to $9$ can be written as the product of the digits of a number in the interval $[1, 10)$.