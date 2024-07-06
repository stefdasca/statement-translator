We have a square rectangular area of size $n \\cdot n$ ($n$ - odd). The $1 \\cdot 1$ tile in the top-left corner is missing. The goal is to tile as much of the area as possible with tiles of size $1 \\cdot 2$ (or $2 \\cdot 1$). We must use as many tiles as possible and additionally, the number of horizontal tiles used must be equal to the number of vertical tiles used for tiling.

# Input data

The file `pavele.in` contains the number $n$ in the first line.

# Output data

The file `pavele.out` contains a number $r$ in the first line, representing the number of vertical (horizontal) tiles used. The following $n$ lines contain $n$ integers each, separated by a space, representing the tiling pattern encoding.

The numbers must be between $-r$ and $r$. The value $0$ signifies that the specific position in the rectangular area is not tiled (or is missing, as $0$ also represents the top-left corner). 

For encoding horizontal tiles, use two equal numbers, between $1$ and $r$, positioned next to each other on the same line. For encoding vertical tiles, use two equal numbers, between $-r$ and $-1$, positioned one below the other.

# Constraints and clarifications

* $5 \\leq n \\leq 299$;
* $n$ – odd;
* Horizontal tiles are encoded using positive values, and vertical tiles using negative values;
* Obviously, tiles cannot overlap and must be completely embedded within the rectangular area;

# Example

`pavele.in`
```
5
```

`pavele.out`
```
6
 0   1   1  -1  -2
-3  -4  -5  -1  -2
-3  -4  -5   4   4
 2   2  -6   5   5
 3   3  -6   6   6
```

## Explanation

Here, the data is indented just for an easier understanding of the example.

~[pavele.png]

The top-left corner is encoded by $0$ since it is missing. There are no other $0$ values since the rest of the area can be entirely tiled using $6$ horizontal tiles (encoded with numbers between $1$ and $6$) and $6$ vertical tiles with numbers between $-6$ and $-1$.