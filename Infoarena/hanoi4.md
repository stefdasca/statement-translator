# Hanoi4

We all know the classic problem of the 3 towers (stacks) of Hanoi. On one of the 3 stacks there are $N$ disks, in ascending order (from top to base) by size. You can perform moves, a move consisting of taking a disk from the top of one of the 3 stacks and placing it on top of another, provided that at no time, on any stack, there is a larger disk over a smaller disk. It is known that the minimum number of moves required to move the $N$ disks from the stack they are initially on to another, using only 3 stacks, is $2^N -1$. You need to determine the minimum number of moves required to move $N$ disks from one stack to another, having a total of 4 stacks available.

## Input data

The input file `hanoi4.in` contains a single integer: $N$ 

## Output data

The output file `hanoi4.out` will contain a single integer value: the required minimum number of moves.

## Constraints and clarifications

$1 \leq N \leq 1000$ 

The result fits into a 64-bit integer.

## Examples:

`hanoi4.in` `hanoi4.out`
`7` `25`
`64` `18433`

