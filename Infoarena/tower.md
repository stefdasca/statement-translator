Tower

## Task
You are playing a tower defense game on a grid. Some cells on the grid contain rocks which cannot be traversed, some contain enemies, and others are free. You need to place a single laser tower on a free cell. Once placed, the tower shoots laser beams in the north, south, east, and west directions. The beam continues until it exits the grid or hits a rock, destroying all enemies in its path. Each destroyed enemy is worth a certain score. Your final score is the sum of the values of all destroyed enemies. Find the maximum possible score.

## Input data
The input file `tower.in` contains two integers on the first line, $M$ and $N$, representing the number of rows and columns of the grid, respectively. The second line contains two integers $R$ and $E$, representing the number of rocks and the number of enemies. The next $R$ lines contain a pair of integers $l$ and $c$, the coordinates of a cell containing a rock. Each of the following $E$ lines contains a triplet $l$ $c$ $s$, representing the coordinates of a cell containing an enemy and the score gained by destroying it.

## Output data
The output file `tower.out` will print a single number, the maximum possible final score for the given configuration.

## Constraints
$1 \leq M, N \leq 1000000000$

$1 \leq R, E \leq 100000$

$1 \leq l \leq M$

$1 \leq c \leq N$ for all coordinates

$1 \leq s \leq 10000$ for all enemy scores

A cell contains at most one enemy or one rock.

For 10% of the tests, $M, N, R, E \leq 1000$

For another 20% of the tests, $R, E \leq 1000$

For another 30% of the tests, $R, E \leq 30000$

## Example

`tower.in`
```
10 10
3 6
2 3
1 5
6 3
5 2 40
5 5 10
5 6 30
1 3 20
2 5 50
3 3 10
```

`tower.out`
```
90
```

## Explanation
Placing the tower at coordinate $(5, 3)$ results in 90 points $(40 + 10 + 10 + 30)$. Although placing the tower at coordinate $(5, 5)$ would have yielded more points, the tower must be placed on a free cell.