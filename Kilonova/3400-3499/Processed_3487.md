# Hiking Trails

A terrain is modeled as an $N \times M$ matrix, containing integer values. The values of the elements represent the altitude or depth of each point relative to sea level.

Entry to the terrain is from the northern side (the first line of the matrix) and at each step, one moves down a line, moving either south, southwest, or southeast. The terrain is exited on the southern side (the last line of the matrix).

# Task

You need to determine how many possible trails exist if we do not want to go below sea level (meaning we do not want to cross elements with negative values), and we want to traverse a maximum number of saddle points. A saddle point is defined as a non-negative element that is strictly greater than its north and south neighbors and strictly less than its west and east neighbors.

# Input data

* The first line of the input file `tura.in` contains an integer $t$ - the number of tests.
* For each test, the first line contains two integers: $N$ and $M$.
* The next $N$ lines contain $M$ integer values separated by spaces, representing the elements of the matrix.

# Output data

* For each test, print on a separate line in `tura.out` the number of possible trails.

# Constraints and clarifications

* $0 < t < 9$
* $1 < N, M < 19$
* The values of the elements are in the range $[-10, 10]$.

# Example

`tura.in`
```
1
7 5
-1 2 3 3 -1
5 3 4 4 -1
4 2 5 1 2
1 1 5 4 5
4 2 3 1 4
4 3 4 2 3
2 2 5 1 1
```

`tura.out`
```
24
```

## Explanation

The saddle points in the example are $(2,2), (4,4), (6,2)$ and $(6,4)$.