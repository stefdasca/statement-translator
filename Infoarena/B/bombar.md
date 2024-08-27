# Bombar

During the bombings, Paftenie became a sapper. He needs to defuse some bombs that are deep underground, and he has to do it quickly. There are exactly $2*N$ bombs, arranged in two parallel rows, as shown in the following figure: Between any two consecutive bombs in the same row or a bomb and its corresponding one in the other row, a tunnel can be dug (the bombs between which tunnels can be dug are connected in the figure). He needs to defuse them all, one by one, digging exactly $2*N-1$ tunnels, and he must be able to circulate between any two bombs only through the dug tunnels. Before getting to work, Paftenie wonders how many ways the tunnels can be dug.

## Task

Help him find out before it's too late!

## Input data

The input file `bombar.in` contains on the first line the number $N$ of bombs in a row.

## Output data

The output file `bombar.out` will contain on the first line a single number, representing the number of possible ways to dig the tunnels.

## Constraints and clarifications

$1 \leq N \leq 20\ 000$

## Example

`bombar.in`
$2$

`bombar.out`
$4$

## Explanation

The bombs are placed as follows: Paftenie can dig the tunnels in $4$ ways:

`bombar.in`
$3$

`bombar.out`
$15$