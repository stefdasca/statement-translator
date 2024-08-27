# Plates

Every day, Zaharel is required by Eugenia to wash the plates and cutlery after each meal. After washing them, he has to arrange them on two shelves: the plates on the first and the cutlery on the second$\dots$ but not just in any way! He has $N$ plates of distinct sizes, ranging from $1$ to $N$, and $K$ identical pieces of cutlery. For each pair of plates arranged on the shelf in such a way that the larger plate, among the two, appears before the smaller plate, Zaharel places a piece of cutlery on the second row.

## Task

Help Zaharel arrange all the plates on the first shelf in such a way that he places all the cutlery on the second shelf. Among all possible arrangements, determine the one that is lexicographically minimal in terms of sizes.

## Input data

The first line of the input file `farfurii.in` contains the natural numbers $N$ and $K$.

## Output data

The first line of the output file `farfurii.out` will contain $N$ distinct numbers between $1$ and $N$ representing the sizes of the plates, displayed in the order they are arranged on the shelf.

## Constraints and clarifications

$1 \leq N \leq 100\, 000$

$0 \leq K \leq N*(N-1)/2$

For at least 40% of the tests $N \leq 2\, 000$

An arrangement $ (A_1, A_2, \dots, A_N) $ is lexicographically smaller than another arrangement $ (B_1, B_2, \dots, B_N) $ if there is a position $p$ such that $A_p < B_p$ and $A_1 = B_1, A_2 = B_2, \dots, A_{p-1} = B_{p-1}$

## Example

`farfurii.in`

    7 8

`farfurii.out`

    1 2 5 7 6 4 3

## Explanation

For the pairs of plates in the arrangement $(5, 4)$ $(5, 3)$ $(7, 6)$ $(7, 4)$ $(7, 3)$ $(6, 4)$ $(6, 3)$ $(4, 3)$ Zaharel places a piece of cutlery on the second row. Another possible arrangement is $1 2 6 5 7 4 3$ but this is lexicographically larger.