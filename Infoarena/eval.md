## Task

A mathematical expression containing $N$ variables is given, where the names of the variables are lowercase letters from the English alphabet. The expression will contain variables, parentheses ($($, $)$), binary operators ($+$, $-$, $*$), and unary operators ($-$, $+$, $[]$). Except for the unary operator $[]$, which denotes the squaring operation, all other operators have their classical meanings. Unary operators have the highest precedence, followed by the $*$ operator; binary $+$, $-$ operators have the lowest precedence. Write a program that evaluates such an expression.

## Input data

The first line of the input file `eval.in` will contain the number $N$ of variables in the expression. The next $N$ lines will each contain an integer representing the values of the variables in the expression: the first line will contain the value of the variable $a$, the second line will contain the value of the variable $b$, etc. The following line will contain a string of characters representing the expression to be evaluated.

## Output data

The output file `eval.out` will contain a single integer representing the value of the expression.

## Constraints and clarifications

$1 \leq N \leq 26$

The length of the expression is a natural number in the interval $[1, 100\ 000]$

The value of each variable is an integer in the interval $[-10^3, 10^3]$

It is guaranteed that the expression is mathematically correct.

It is guaranteed that the value of the expression will be an integer in the interval $[-10^3, 10^3]$

For $70\%$ of the tests, the variables and the result of the expression will be natural numbers.

## Example

`eval.in`
```
3
1
2
3
[a]*(b+c)*(a*a+b*--+c)-c
```

`eval.out`
```
32
```