~[zumzi.jpg|align=right|width=auto]
Zumzi the bee lives in a hive made up of $N$ hexagonal cells. The $N$ cells, numbered from $1$ to $N$, are arranged in a spiral as shown in the adjacent image. Specifically, the cell in the center of the hive is numbered $1$. Moving from this cell to the south and then spiraling clockwise, the other cells are numbered. Initially, Zumzi is located in the center cell (the one numbered $1$) and wants to reach cell number $X$, where her friend is located. Zumzi can move from one cell to any of the neighboring cells, without leaving the hive. Two cells are considered neighbors if they share a common side. Some cells in the hive are occupied by other bees, preventing Zumzi from passing through them. Your task is to determine how many ways Zumzi can reach her friend after exactly $K$ steps.

# Input data

The input file `zumzi.in` contains on its first line the natural values $N$, $M$, $K$, and $X$ separated by a space, with the following meanings:

* $N$ - the total number of cells in the hive;
* $M$ - the number of cells in the hive occupied by other bees;
* $K$ - the number of steps Zumzi has available;
* $X$ - the cell number where Zumzi's friend is located.

The next line of the input file contains $M$ natural numbers separated by a space, representing the numbers of the occupied cells in the hive.

# Output data

The output file `zumzi.out` will contain on its first line a single natural number representing the number of ways Zumzi can reach her friend.

# Constraints and clarifications

* $1 \leq M < N \leq 300$;
* $X \neq 1$;
* $K \leq 100$;
* Zumzi cannot leave the hive, and once she reaches her friend, she will not leave that cell;
* Zumzi is not very intelligent and may pass through a cell multiple times, except for the final cell where her friend is, into which she will enter only once and will not leave.

# Example 1

`zumzi.in`

```
12 4 3 9 
11 4 6 8
```

`zumzi.out`

```
4
```

## Explanation
~[zumzi1.jpg|align=right|width=auto]
The possible ways are:
$1-2-10-9$
$1-3-2-9$
$1-3-10-9$
$1-7-2-9$

# Example 2

`zumzi.in`

```
12 4 4 2
11 4 6 8
```

`zumzi.out`

```
9
```

## Explanation

The possible ways are:
$1-3-10-9-2$
$1-7-1-3-2$
$1-5-1-7-2$
etc

