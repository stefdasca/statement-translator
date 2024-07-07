It is considered $ns$ chairs numbered from $1$ to $ns$, arranged in a circle.
For example, for $ns=20$, the arrangement of the chairs is shown in the figure below.
~[img.png|align=center|width=54em]

On each of these chairs, a child is seated. The first child sits on chair $1$, and the last on chair $ns$.

In addition to the $ns$ chairs already occupied, other $nc$ children ($1 \leq nc \leq ns$) are waiting for a place to become available.

At some point, a single child gets up from the chair and leaves. Then, as long as there is no child right next to the free chair, all the children waiting move counterclockwise, one position at a time, until one of them occupies the free spot.

Conditions:

* Initially, all chairs are occupied;
* Each waiting child is initially right next to an occupied chair;
* When a child advances by $n$ positions to a chair, all those waiting also advance by $n$ positions. Since the movement is circular, advancing by $4$ positions from position $18$ means moving to position $2$.

# Task

Given a sequence of the order numbers of the children who leave at each moment, write a program that displays the number of the chair on which each waiting child sits if this is possible.

# Input data

The first line of the input file `scaune.in` contains two numbers, separated by a space, representing the number of chairs $ns$ and the number of children waiting $nc$.

The following $nc$ lines will contain the positions of the children waiting.

Next, until the end of the file, there are lines describing the order numbers of the children who get up one by one from the chairs and leave the game.

# Output data

The output file `scaune.out` contains $nc$ lines, each line containing the initial waiting position of the child and the occupied position, separated by a space. The output lines must be in the same order as those in the input file.

If a child has no possibility to sit, `0` will be written in his line in the output file.

# Constraints and clarifications

* $1 \leq ns \leq 200$
* $nc \leq ns$

# Example

`scaune.in`
```
20 5
6
19
17
13
1
1
3
20
16
```

`scaune.out`
```
6 16
19 3
17 0
13 20
1 1
