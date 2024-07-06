## Task

Two odd natural numbers $p$ and $q$ are given, and $A = \\{1, 2, 3, 4, 5, \\dots, p \\cdot q \\}$ is the set of all natural numbers between $1$ and $p \cdot q$.

## Task

Write a program that determines $p$ sets, denoted $A_1$, $A_2$, $\\dots$, $A_p$ with the following properties:
* The number of elements of each set $A_i$, $1 \\leq i \\leq p$, is equal to $q$;
* $A_i \\cap A_j = \\emptyset$, $1 \\leq i < j \\leq p$;
* $A_1 \\cup A_2 \\cup \\dots \\cup A_p = A$;
* The sums of the elements of each set $A_i$, $1 \\leq i \\leq p$, are equal.

## Input data

The input file `multimi.in` contains on the first line two natural numbers $p$ and $q$ separated by a space, as described above.

## Output data

The output file `multimi.out` will contain $p$ lines. Each line $i$ will contain the $q$ elements of set $A_i$, $1 \\leq i \\leq p$, separated by a space.

## Constraints and clarifications

* $3 \\leq p, q \\leq 1\ 001$;

## Example

`multimi.in`
```
3 7
```

`multimi.out`
```
1 5 9 10 15 16 21
2 6 7 11 14 17 20
3 4 8 12 13 18 19
```

## Explanation

$A = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10,$ $ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 \\}$ 

$A_1 = \\{1, 5, 9, 10, 15, 16, 21 \\}$

$A_2 = \\{2, 6, 7, 11, 14, 17, 20 \\}$

$A_3 = \\{3, 4, 8, 12, 13, 18, 19 \\}$

$1 + 5 + 9 + 10 + 15 + 16 + 21 = 77$

$2 + 6 + 7 + 11 + 14 + 17 + 20 = 77$

$3 + 4 + 8 + 12 + 13 + 18 + 19 = 77$