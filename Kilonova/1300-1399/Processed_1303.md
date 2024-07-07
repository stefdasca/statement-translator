
At the opening ceremony of ONI Ploiesti, Gigel, a big fan of logic problems, noticed that the first row in the hall consists of $2 \cdot N + 2$ seats, numbered from left to right from $1$ to $2 \cdot N + 2$. In this row, $N$ boys and $N$ girls are seated in any order, with the two remaining free seats being adjacent.

Immediately Gigel invents a problem. Let's consider that the only possible move is for two students sitting on adjacent seats to stand up and sit down (in the same order) on the two free seats.

The problem consists of determining a sequence of moves after which all the girls are grouped on the left side of the row, all the boys are grouped on the right side, and the two free seats separate the girls from the boys.

# Task

Given the value $N$, as well as the initial arrangement of the students, determine a sequence of moves that will finally lead to the arrangement described in the problem statement.

# Input data

The input file `aranjare.in` contains the natural number $N$ on the first line. The second line of the input file contains a string of $2 \cdot N + 2$ characters ($N$ characters `F`, $N$ characters `B`, and two adjacent characters `S`) representing the initial arrangement of the students on the row and the two free seats. More specifically, `F` indicates a seat occupied by a girl, `B` indicates a seat occupied by a boy, and `SS` represents the two free seats.

# Output data

The output file `aranjare.out` will contain the moves from the determined sequence, in order, one move per line. A move is described by a natural value $K (1 \leq K < 2 \cdot N + 2)$ meaning "the students sitting on seats $K$ and $K + 1$ will move to the free seats."

# Constraints and clarifications

* $3 \leq N \leq 5 \ 000$
* For the test data, there is always a solution. The solution is not unique.

# Example 1

`aranjare.in`
```
3
FBSSFBFB
```

`aranjare.out`
```
7
2
5
3
6
1
7
3
6
4
```

## Explanation

The configurations obtained on the way are:

* FBFBFBSS
* FSSBFBBF
* FFBBSSBF
* FFSSBBBF
* FFBBBSSF
* SSBBBFFF
* FFBBBFSS
* FFSSBFBB
* FFFBBSSB
* FFFSSBBB
```
