```markdown
# Task

The defense device of the elves is in the shape of a matrix with $N$ rows and $M$ columns. In each position of the matrix, a defense tower is placed according to well-established rules. As long as there are positions not occupied by a tower, such a position is chosen and a level $1$ tower is placed there. We call this operation placement. Depending on the configuration of neighboring positions (in $8$ directions), the tower will upgrade to a higher level. When a tower reaches level $X$ and has at least one neighbor of level $X$, it becomes a level $X+1$ tower, and all neighboring towers of level $X$ disappear, leaving free spots where other towers can be placed again. We call this operation upgrade and it will be applied as often as possible after a placement. The defense device has its final form when no other towers can be placed.

Given the final configuration of the defense device, indicate a minimal sequence of placements to reach that configuration.

# Input data

The file `tower8.in` contains on the first line two natural numbers separated by space, $N$ and $M$ - the number of rows and columns of the defense device. On the following $N$ lines, there are $M$ non-zero natural numbers separated by space - the levels of the defense towers in the final form of the defense device.

# Output data

The file `tower8.out` will contain on the first line a natural number $K$ representing the minimum number of towers that were placed to bring the defense device to the final form. On the following $K$ lines, there are two natural numbers $L$ and $C$ separated by space - meaning: a level $1$ tower is placed on row $L$, column $C$ of the defense device.

# Constraints and clarifications

* $2 \leq N, M \leq 100$
* if only the minimum number of placements is shown correctly, $20 \%$ of the score is obtained
* if a correct sequence is shown with a higher number of placements, $80 \%$ of the score is obtained provided that the number of placements is at most double the minimum number
* if the minimum number of placements and a correct sequence of them are shown, $100 \%$ of the score is obtained (the sequence of placements is not unique!)
* Note: the positions in the corners of the defense device have only $3$ neighbors, and those on the edge of the defense device have only $5$ neighbors.

# Example 1

`tower8.in`
```
2 2
1 2
3 4
```

`tower8.out`
```
15
1 1
1 2
1 1
2 1
1 1
1 2
1 1
2 2
1 1
1 2
1 1
2 1
1 1
1 2
1 1
```

## Explanation

The following sequence of moves was made.

~[tower8.png]

Where $P$ – means a placement is about to be made in the hashed position and $U$ – means an upgrade is about to be made in the bordered position using the highlighted tower from the neighboring position.
```