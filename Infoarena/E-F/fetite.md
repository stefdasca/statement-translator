## Task

Miruna and her friends found a flower with $N$ petals and want to play a modified version of the game "He loves me, he loves me not". The girls number the petals from $1$ to $N$ in counterclockwise order. They will go around the petals starting with the one numbered $1$, continuing with the one numbered $2$, $\dots$. On the first petal they will all exclaim "He loves me", on the second "He loves me not" and they will pluck it, on the third petal again "He loves me", on the fourth "He loves me not" and they will pluck it. They will continue the game until they are left with a single petal. You will need to identify the ordinal number of this last remaining petal.

## Input data

The input file `fetite.in` contains a single natural number $N$ representing the number of petals on the flower found by the girls.

## Output data

In the output file `fetite.out` you will print the ordinal number of the last petal left after the game.

## Constraints and clarifications

$0 < N < 2^{63}$

## Example

`fetite.in` `fetite.out` $5$ $3$

## Explanation

The petals will be plucked in the following order: $2$, $4$, $1$, $5$. The remaining petal will be the one with the ordinal number $3$.