## Hagi

At the beginning of his career, Ianis Hagi shows signs of becoming a great football player. Consequently, Gica, curious by nature, wants to find out how Ianis's career trajectory will look. He travels to the distant land of iGorj to ask Bogdanel MIPS for more details about his son's future. Bogdanel predicts that Ianis, by the end of his career, will play for $K$ teams, score $N$ goals, and provide $M$ assists. Ambitious Gica wants to know the total number of different career scenarios for Ianis modulo $1.000.000.007$. A scenario (or mode) differs from another if there exists a team $i$ among the $K$ teams for which the number of assists or goals is different.

## Task

The input file `hagi.in` contains on the first line 3 numbers: $K$ (the number of teams), $N$ (the number of goals), and $M$ (the number of assists).

## Input data

The input file `hagi.in` contains on the first line 3 numbers: $K$ (the number of teams), $N$ (the number of goals), and $M$ (the number of assists).

## Output data

The output file `hagi.out` will contain on the first line the total number of different scenarios modulo $1.000.000.007$.

## Constraints and clarifications

$1 \leq K, N, M \leq 1.000.000$

$1 \leq K, N, M \leq 7$

$1 \leq K, N, M \leq 50$

$1 \leq K, N, M \leq 1.000$

## Example

`hagi.in`

`2 2 1`

`hagi.out`

`6`

`1320`

`3921`

`782`

`645226719`

`666013`

`964964`

`123456`

`556923723`

## Explanation

For the first example, the possibilities are as follows:

-> for the first team: $0$ goals, $0$ assists -- for the $2$-nd team: $2$ goals, $1$ assist;

-> for the first team: $0$ goals, $1$ assist -- for the $2$-nd team: $2$ goals, $0$ assists;

-> for the first team: $1$ goal, $0$ assists -- for the $2$-nd team: $1$ goal, $1$ assist;

-> for the first team: $1$ goal, $1$ assist -- for the $2$-nd team: $1$ goal, $0$ assists;

-> for the first team: $2$ goals, $0$ assists -- for the $2$-nd team: $0$ goals, $1$ assist;

-> for the first team: $2$ goals, $1$ assist -- for the $2$-nd team: $0$ goals, $0$ assists.