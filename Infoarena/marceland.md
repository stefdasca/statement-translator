# MarceLand

After cloning himself multiple times on his boat, the original Marcel began to observe his clones. It wasn't hard to discern which was original, as the other Marcels were chaotic and lacked initiative. Disappointed with his project, Marcel wanted to leave them on one of his new islands. The island can be viewed from above as a matrix of dimensions $N$ rows and $M$ columns, where each cell is either a rock (blocked cell, coded by the character $\#$) or a free plot. On a free plot, there can be either a Marcel's house (coded by the letter/character $M$), a well (coded by $\@$), or sand (coded by $.$). Due to the arrangement of rocks on the terrain, the island can turn into a real labyrinth for the Marcels. Marcel has access to a cell in the matrix if he can move from his house either up, down, left, or right (as seen from Marcel looking from his helicopter), only through free plots (the characters $'.'$, $\@$ , $M$) to the respective cell - in other words, if there is a 4-connected path between his house and the respective cell that does not pass through rocks. Of course, each Marcel does not want to remain dehydrated, so he must drink water from a well. Thus, Marcel wants each Marcel to have access to at least one well.

## Task

Given the matrix that encodes the island, add the minimum number of wells so that each Marcel can reach, starting from his house, at least one well. For this purpose, some sand plots (the character $.$) can be transformed into well plots (the character $\@$). A matrix that meets these conditions is required, or it should be stated that this is not possible.

## Input data

The input file `marceland.in` will contain on the first line the number $T$ of tests that will be described. Each test has on the first line the numbers $N$ and $M$ representing the rows and columns of the matrix, and on the following $N$ lines, there will be $M$ characters from the set {$'.'$, $\@$ , $M$, $\#$} describing the island for that specific test.

## Output data

The output file `marceland.out` will contain $T$ responses, one per line for each test from the input. A response is either a line with the number $"-1"$, or $N + 1$ lines, as follows: The first line contains the number $F$, representing the number of added wells. The next $N$ lines contain $M$ characters from the set {$'.'$, $\@$ , $M$, $\#$}, describing the island after $F$ wells have been added.

## Constraints and clarifications

$$ 1 \leq T \leq 5 $$
$$ 1 \leq N, M \leq 100$$

For $30$ points, it is guaranteed that $N = 1$. 

For another $30$ points, it is guaranteed that $N = 2$. 

For another $10$ points, it is guaranteed that $F = 0$, meaning no wells need to be added, for all $T$ tests in the input for which there exists a solution; for those for which a solution does not exist, $"-1"$ must be printed. 

For another $10$ points, it is guaranteed that for all $T$ tests in the input, a solution exists.

Any correct solution can be printed.

There is at least one Marcel on the island.

You will receive the evaluation results only on the input example file. These will not affect the problem's score, having an associated score of 0.

## Example

`marceland.in`
```
5
5 3
###
.M#
.##
.M#
###
10 1
#
#
#
.
.
#
M
#
#
#
1 10
...####M..
3 3
M##
##M
###
2 6
###MM.
#####@
```

`marceland.out`
```
1
###
.M#
.##
@M#
###
-1
1
...####M.@
-1
0
###MM.
#####@
```