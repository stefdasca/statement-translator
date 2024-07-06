We consider $N$ strings of characters, each string having the length $N$. The strings contain characters from the set {`a`, `b`, ..., `z`, `#`}. We can view these $N$ strings as an $N \times N$ square matrix of characters.

# Task

Determine the total number of correctly formed rhombuses as well as the side length of the largest rhombus that can be constructed in the matrix such that it has the character `#` at all four corners, each side of the rhombus perimeter contains at least one vowel, and the remaining characters that make up the rhombus are different from the character `#`.

A rhombus is valid if its sides are parallel to the diagonals of the matrix and contains at least $13$ elements on the sides and inside.

Examples of valid rhombuses (where $V \in$ {`a`, `e`, `i`, `o`, `u`}, with any character allowed inside the rhombuses except the character `#`):

~[rodiezv.png]

# Input data

The input file `rodiezv.in` contains on the first line the non-zero natural number $N$ as described in the statement. On the following $N$ lines, the $N$ strings of characters.

# Output data

The output file `rodiezv.out` will contain two lines. The first line contains a non-zero natural number representing the total number of correctly formed rhombuses.

The second line contains a non-zero natural number representing the side length of the largest formed rhombus that meets the task specifications. It is guaranteed that there is at least one correctly formed rhombus.

# Constraints and clarifications

* Let $M$ denote the number of `#` characters in the matrix.
* $5 \leq N \leq 2000$, $4 \leq M \leq 50000$
* For tests worth $26$ points: $5 \leq N \leq 300$, $4 \leq M \leq 1000$, the matrix will not contain consonants.
* For other tests worth $33$ points: $5 \leq N \leq 300$, $4 \leq M \leq 10000$.
* For other tests worth $41$ points: There are no other constraints.

# Example

`rodiezv.in`
```
9
ib#addefo
nueaged#s
#etv#m#ce
oawiyacup
ic###awe#
nbaceunoi
f#eiq##eo
oboyhihjn
ioi#etwyi
```

`rodiezv.out`
```
2
3
```

## Explanation

The $2$ valid rhombuses of side $3$ are marked.

~[rodiezv2.png]