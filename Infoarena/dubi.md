The Dubious Function

Chappie, the little robot, received a new task from his father, Ninja, which is to divide a country they have conquered into several counties. The country, besieged by Ninja, contains $N$ cities numbered from $1$ to $N$. Ninja wants a division into the minimum number of counties such that any two cities in a county have a direct road between them. In his division, Chappie must ensure that each city belongs to exactly one county. His uncle, Amerika, is responsible for building the roads. He builds a direct road between cities numbered $X$ and $Y$ if and only if $\min (X, Y) \leq X \oplus Y \leq \max (X, Y)$ (in other words, if the number $X \oplus Y$ is between $X$ and $Y$). Since Chappie is busy "putting to sleep" people who have stolen from his father, he will ask for your help, in return for which you will receive 100 points.

## Task

## Input data

The input file `dubi.in` contains on the first line the number $N$ of cities.

## Output data

The output file `dubi.out` will contain on the first line the number $K$ of counties in the division. Lines from $2$ to $K + 1$ will describe each county, as follows: on line $i + 1$ first the number of cities in county $i$ will be printed, and then the cities in ascending order, separated by a space. 

## Constraints

$1 \leq N \leq 2 \cdot 10^5$

Note: The operation $\oplus$ on bits represents bitwise addition without carrying (for example $1100 \oplus 1010 = 0110$).

Attention! Each subtask has grouped tests!

Subtask 1 (20 points):
$1 \leq N \leq 20$ (Feedback test 2)

Subtask 2 (20 points):
$1 \leq N \leq 2^{12}$ and $N$ is a power of $2$ (Feedback test 4)

Subtask 3 (60 points):

Initial constraints (Feedback test 9)

## Example

`dubi.in`
```
4
```

`dubi.out`
```
3
2 1 3
1 2
1 4
```

## Explanation

There will be $3$ counties in total (two consisting of just one city each, respectively $2$ and $4$, the only relevant road existing in the county formed by the cities $1$ and $3$). The road $1 \ 3$ exists because $1 \leq 1 \oplus 3 = 2 \leq 3$.