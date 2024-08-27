## Equation

Zaharel has learned in math class how to solve quadratic equations of the form $Ax^2 + Bx + C = 0$. To solve them more easily, he usually rewrites such an equation in the form $(P_1 x + Q_1)(P_2 x + Q_2) = 0$ where $P_1$, $Q_1$, $P_2$, $Q_2$ are integers. Shortly, Zaharel noticed that there are multiple ways to write an equation in this form and wrote them all on a sheet, sorted in ascending order by $P_1$, and in case of equality, in ascending order by $Q_1$. To check if he made any mistake, he needs a program that tells him the $K$-th possibility in the sorted order.

## Input data

The input file ecuatie.in will contain on the first line the integers $A, B, C$ and $K$.

## Output data

The output file ecuatie.out will contain a string of the form $(P_1 x + Q_1)(P_2 x + Q_2)$ where $P_1$, $Q_1$, $P_2$, $Q_2$ are integers. The following formatting rules must be respected during display:
- if $P_1$ or $P_2$ are equal to $1$, the value $1$ will not be displayed
- if $P_1$ or $P_2$ are equal to $-1$, only the sign $-$ will be displayed
- if $Q_1$ or $Q_2$ are less than $0$, the sign $-$ will replace the sign $+$
- If there are no $K$ possibilities to write the given equation, the value $-1$ will be displayed instead.

## Constraints

$-10^9 \leq A, B, C \leq 10^9$

$A, C \neq 0$

$1 \leq K \leq 10^9$

## Example

`ecuatie.in` `ecuatie.out` 
```
4 8 -12 9
(2x-2)(2x+6)
```

## Explanation

All possibilities of rewriting $4x^2 + 8x - 12$ are:
```
(-4x-12)(-x+1)
(-4x+4)(-x-3)
(-2x-6)(-2x+2)
(-2x+2)(-2x-6)
(-x-3)(-4x+4)
(-x+1)(-4x-12)
(x-1)(4x+12)
(x+3)(4x-4)
(2x-2)(2x+6)
(2x+6)(2x-2)
(4x-4)(x+3)
(4x+12)(x-1)
```