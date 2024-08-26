# Triangle

Gigel likes to play, so he received a game with boxes that have strictly positive integer numbers written on them. With his rich imagination, one day he thought of building a triangle out of boxes: one box is placed on top of two boxes, which are placed on three boxes $\dots$ which are placed on $N$ boxes (thus each box rests on two others). But Gigel doesn't stop there; he wants the number in each box of his triangle (except for the last line) to be equal to the sum of the numbers in the two boxes below it.

## Task

Write a program that determines if Gigel can build a triangle with a side length $N$, in which the sum of the numbers on all the boxes is $S$, knowing that he can use any number of boxes with any number in them.

## Input data

The first line of the file `triunghi.in` will contain the numbers $N$ and $S$ separated by a space.

## Output data

The first $N$ lines of the file `triunghi.out` will contain the numbers on the boxes in the triangle: on line $i$ there will be $i$ strictly positive integer numbers describing line $i$ of the triangle. If Gigel cannot build such a triangle, the file will instead display the message `imposibil`.

## Constraints and clarifications

$1 \leq N \leq 18$

$1 \leq S \leq 1\ 000\ 000$

If multiple solutions are possible, any of them may be displayed.

## Examples

`triunghi.in`

$3\ 34$

`triunghi.out`

$13$

$6\ 7$

$1\ 5\ 2$

`triunghi.in`

$4\ 26$

`triunghi.out`

$8$

$4\ 4$

$2\ 2\ 2$

$1\ 1\ 1\ 1$