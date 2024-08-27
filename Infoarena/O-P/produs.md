## Task

Viviana loves to multiply numbers. Recently, she managed to calculate the product of all natural numbers between $X$ and $Y$. Specifically, she found $P = X * (X + 1) * (X + 2) * \dots * Y$. Unfortunately, she forgot what the numbers $X$ and $Y$ are, but she still remembers $P$. Help Viviana find two numbers $X$ and $Y$ such that the product of all natural numbers between them is equal to $P$.

## Input data

The input file `produs.in` will contain on the first line the number $P$.

## Output data

In the output file `produs.out` you will print the two numbers $X$ and $Y$, separated by a space, that meet the condition from the statement.

## Constraints

$1 \leq P \leq 10^{10}$
It is guaranteed that there is always a solution, and it will satisfy the condition 
$1 \leq X \leq Y \leq 100000$
If there are multiple solutions, print the one with the minimum $X$.

## Example

`produs.in`
336

`produs.out`
6 8

`produs.in`
646300418472124416000000

`produs.out`
5 25

## Explanation

For the first example: $6 * 7 * 8 = 336$.