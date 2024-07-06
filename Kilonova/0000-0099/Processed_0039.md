~[suma1.png]

\\
The builders hired by Pharaoh Cheops have finished constructing the much-dreamed stepped pyramid. The grand pyramid has $n$ identical cubic-shaped rooms, numbered from $1$ to $n$, arranged on $m$ levels as follows:
- The room at the top of the pyramid forms level $1$ and is numbered $1$;
- Level $2$ of the pyramid consists of the next $4$ rooms which, in a section parallel to the base, have the appearance of a matrix with $2$ rows and $2$ columns; the rooms on level $2$ are numbered from $2$ to $5$ in increasing order of the matrix rows, and within the same row in increasing order of the matrix columns;
...
- Level $m$ of the pyramid is made up of $m \times m$ rooms and, in a section parallel to the base, has the appearance of a matrix with $m$ rows and $m$ columns; the rooms on level $m$ are numbered in continuation of those on levels $1, 2, ..., m - 1$, in increasing order of the matrix rows of the section, and within the same row in increasing order of the matrix columns. For example, the pyramid in the drawing above has $n = 30, m = 4$, and the rooms are numbered and arranged on levels as follows:
\\
~[suma2.png]
\\
The levels of rooms are positioned such that the rooms on the first row and first column of each level overlap. For the given example, rooms $1, 2, 6$, and $15$ are situated one below the other, in this order.

Access to any room in the pyramid, located on different levels, is achieved through paths constructed as follows:
* Entry into the pyramid is only through the room at the top, which is numbered $1$;
* From room number $k$ on a path, it is possible to enter one of the four rooms located on the immediately next level of the pyramid, namely: the room directly below room $k$ or one of its three neighboring rooms in the section (in the directions East, Southeast, South, considering the sections positioned as in the images above). For example, from room number $10$, one can enter one of the rooms numbered $20, 21, 24$, or $25$.

The Pharaoh looks with pride and sadness at the beautiful pyramid. The treasury's funds have dwindled, and the pyramid's rooms must be finished and decorated. His favorite scribe recalculated everything, eliminated unnecessary objects, and determined for each room $k$ a cost $c_k$ for finishing and decorating it ($1 \leq k \leq n$).

However, since the total required sum is still large, the Pharaoh asked the scribe to choose a path, among those constructed, that passes through all levels of the pyramid such that the sum $s$ of all costs for finishing and decorating the rooms on this path is minimal. For now, only these rooms will be arranged...

# Task
Write a program that determines the number $m$ of levels of the pyramid, the minimal sum $s$ of all costs for finishing and decorating the rooms on a path that passes through all levels of the pyramid, constructed as described in the task, and such a path with minimal sum $s$, chosen by the scribe.

# Input data
The input file `suma.in` contains on the first line the natural non-zero number $n$ representing the number of rooms in the pyramid. The second line contains $n$ non-zero natural numbers $c_1, c_2, \ldots, c_n$, separated by spaces, representing the costs for finishing and decorating the rooms, in the order of their numbering.

# Output data
The output file `suma.out` will contain on the first line two natural numbers $m$ and $s$, separated by a single space, with the significance mentioned in the task. The second line will contain, separated by spaces, in the order of their traversal, the numbers of the rooms on a path that passes through all levels of the pyramid, for which the minimal sum $s$ is achieved.

# Constraints and clarifications
* $1 \leq n \leq 63\ 365$
* For each value $n$ read, it is possible to construct a stepped pyramid with $n$ rooms as described in the task.
* $1 \leq c_1, c_2, ..., c_n < 100$
* If there are multiple paths that pass through all levels of the pyramid and for which the minimal sum $s$ is achieved, then the chosen path will be the smallest path in lexicographical order.
* The path $a_1, a_2, a_3, \ldots, a_m$ is smaller in lexicographical order than the path $b_1, b_2, b_3, \ldots, b_m$ if there exists an index $j$ ($1 \leq j \leq m$) such that $a_1=b_1, a_2=b_2, \ldots, a_{j-1}=b_{j-1}$ and $a_j < b_j$.
* Scoring:
* $10\%$ of the points for correctly determining the number $m$ of levels of the pyramid.
* $30\%$ of the points for correctly determining the minimal sum $s$.
* $60\%$ of the points for correctly determining the required path.

# Example

`suma.in`
```
14
7 8 4 5 5 8 4 2 7 7 8 3 1 6
```

`suma.out`
```
3 13
1 3 8
```

Explanations
---

The pyramid contains $14$ rooms arranged on $m = 3$ levels. The levels contain the values:
\\
~[suma3.png]
\\
The minimal sum $s$ of all costs for finishing and decorating the rooms on a path that passes through all $3$ levels of the pyramid is $13$. There are multiple paths for which the minimal sum can be achieved: $[1,3,8], [1,4,13], [1,5,13]$. Lexicographically, the smallest path among these paths is: $[1,3,8]$.