# Task

To protect the wildlife and flora, in the Rodnei Mountains, the natural reserve **Piatra Rea** was established. The reserve is represented on the map as a grid with $L$ rows and $C$ columns. The grid consists of $L \times C$ square cells with a side length of $1$. Among the plants protected by law, there are also $N$ trees declared as natural monuments, numbered from $1$ to $N$. Each tree is positioned at the center of a cell. No two trees occupy the same position. To restrict access to the reserve, it was proposed to build a fence, made up of identical segments, each segment being of length equal to the side length of a cell. The segments are placed on the contour of the cells. Construction of the fence starts at the top-left corner of the first cell of the grid, located on row $1$ and column $1$, and ends at the same point. There are no other intersection points.
~[rezervatie-naturala.png|align=center]

# Task

Knowing the positions of all fence segments, the size of the reserve, and the positions of the $N$ trees declared as natural monuments, identify the trees that are located inside the fenced area.

# Input data

The input file `rezerv.in` contains on the first line the natural numbers $L$ and $C$. The second line contains a string of directions consisting only of the characters `N`, `S`, `E`, `V`, representing the placement of the segments (North, South, East, West respectively). The first character in the string represents the direction in which the first segment is built and can only be `E` or `S`. The $i$-th character in the string, with $i$ between $2$ and the number of segments, represents the direction in which the $i$-th segment is built, starting from the free end of the $(i - 1)$-th segment. The third line contains the natural number $N$. On each of the following $N$ lines, there are two natural numbers representing the row and column corresponding to the trees $1, 2, 3, \dots, N$.

# Output data

The output file `rezerv.out` will contain on the first line a natural number $K$, representing the number of trees that are inside the fenced area. On the second line, separated by a space, $K$ natural numbers will be written in ascending order, representing the order numbers of the trees located inside the fenced area. In the situation where no tree is inside the fenced area, the output file will display a single value: $0$.

# Constraints and clarifications

* $1 \leq L, C \leq 200$
* $1 \leq N \leq 1 \ 000$
* $4 \leq \text{number of fence segments} \leq 10 \ 000$

# Example 1

`rezerv.in`
```
5 4
ESSENNEESVSSVVVNNN
3
3 1
1 4
1 2
```

`rezerv.out`
```
2
1 2
```

# Example 2

`rezerv.in`
```
4 5
SSSESENEEENNVSVVVNEENVVV
4
4 2
3 4
2 3
1 1
```

`rezerv.out`
```
3
1 2 4
```

## Explanation

The test data below correspond to figures $1$ and $2$.