Following the bombings of September 11, 2001, the Pentagon building suffered damage to one of its walls. The encoded image of the damaged wall is represented as a matrix with $m$ rows and $n$ columns, as shown in the figure below:

$$
1110000111 \\
1100001111 \\
1000000011 \\
1000000011 \\
1110000111 \\
$$

where $1$ represents an intact wall and $0$ represents a damaged wall.

Funds allocated by Bin Laden for the restoration of the Pentagon will be donated to those who will help the Americans restore this building by placing vertical blocks with heights $k$, $k = 1, \ldots, m$, and width $1$ in the damaged spots.

# Task

For a given structure of a wall in the Pentagon building, determine the minimum number of blocks, with heights $k=1, k=2, \ldots, k=m$, necessary to restore the building.

# Input data

The input file `pentagon.in` will contain on the first line the dimensions $m$ and $n$ of the building's wall, and on the following $m$ lines, each containing a sequence of characters $1$ or $0$ of length $n$.

# Output data

The file `pentagon.out` will contain, on each line, ordered in ascending order by $k$, sequences:

* $k$, $nr$ - where $k$ is the block height, and $nr$ is the number of blocks with height $k$, separated by a space.

# Constraints and clarifications

* $1 < m,n \leq 200$
* Blocks of height $k$, whose number is zero ($0$), will not be displayed.

# Example

`pentagon.in`
```
5 10
1110000111
1100001111
1000000011
1111101111
1110000111
```

`pentagon.out`
```
1 7
2 1
3 2
5 1
```

Please double-check for any grammatical or syntax errors following the rules of the English language.