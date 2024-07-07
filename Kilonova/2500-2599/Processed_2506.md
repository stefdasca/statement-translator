In the Magic Land of Islands, an annual treasure hunt takes place, where teams explore enchanted islands, delineated by the surrounding water. By order of King A., treasures are hidden on each island. The map of the land is represented as a matrix of size $n \times m$, whose elements encode square areas, each with a side length of 1 meter. These can be:
* an area containing water, marked with $-1$;
* an area containing only land, marked with $0$; or
* an area containing land and a single treasure, marked with a non-zero natural number.

Two areas are considered neighbors if they share a common side. Two areas belong to the same island if they are neighbors or if a path can be created from one to the other through a succession of areas, with any two consecutive areas being neighbors. This year, Captain Poseidon wishes to prank King A. by permuting the treasures, such that every treasure is moved to an area where another treasure was originally located. However, to not attract too much attention, the treasures will remain within the island they were initially on.

# Task

Initially, Captain Poseidon proposes the following tasks:
1. Count the treasures on the island where Captain Poseidon is located.
2. Determine the number of solutions for placing all the treasures, such that each treasure is moved within the same island, to an area where another treasure was originally located. Since the number of solutions can be very large, the answer will be provided modulo $1\ 000\ 000\ 007$.

# Input data

The input file `poseidon.in` contains:
* The first line contains the natural number $c$, representing the task that needs to be solved ($1$ or $2$).
* The second line contains two natural numbers $n$ and $m$ representing, in this order, the number of rows and the number of columns of the Magic Land of Islands map. Each of the next $n$ lines contains $m$ integers, representing the encoding of the matrix areas.

For the case when $c=1$, the last line of the file contains two natural numbers $x_P$ and $y_P$, representing the row and column of the area where Poseidon is located.

# Output data

The output file `poseidon.out` will contain a single natural number:
* If $c=1$, it contains the total number of treasures specified in Task 1.
* If $c=2$, it contains the number of placement solutions specified in Task 2, in the indicated form.

# Constraints and clarifications

* $1 \le c \leq 2$;
* $1 \le n, m \leq 1\ 000$;
* Elements of the matrix have integer values in the range [$-1, n \cdot m$]. The matrix is indexed starting from $1$.
* Any two distinct areas containing a treasure will be described by distinct numbers.
* Islands are composed of compact areas of land. It is guaranteed they do not contain water inside.
* $1 \le x_P \le n$, $1 \le y_P \le m$, the area given by $x_P$ and $y_P$ contains land.
* Let $n_c$ be the maximum number of treasures on a single island.

| #  | Points | Constraints |
| -  | -      | ------------|
| 1  | 5      | $c=1$ and there is only one island             |
| 2  | 10     | $c=1$ and $n = 1$                                |
| 3  | 26     | $c=1$, without other constraints                |
| 4  | 13     | $c=2$ and $n_c \leq 4$                           |
| 5  | 17     | $c=2$ and $n_c \leq 8$                           |
| 6  | 29     | $c=2$, without other constraints                 |

# Example 1

`poseidon.in`
```
1
8 6
-1 -1 -1 -1 -1 -1
-1 0 0 -1 -1 -1
-1 9 1 0 -1 -1
-1 3 4 0 -1 -1
-1 0 0 -1 0 -1
-1 -1 -1 5 10 -1
-1 -1 0 6 7 -1
-1 -1 -1 -1 -1 -1
2 2
```

`poseidon.out`
```
4
```

## Explanation

There are two islands, one containing treasures $1,3,4,9$ and the other containing treasures $5,6,7,10$. Poseidon is on the island containing treasures $1,3,4,9$.

# Example 2

`poseidon.in`
```
2
8 6
-1 -1 -1 -1 -1 -1
-1 0 0 -1 -1 -1
-1 9 1 0 -1 -1
-1 3 4 0 -1 -1
-1 0 0 -1 0 -1
-1 -1 -1 5 0 -1
-1 -1 0 6 8 -1
-1 -1 -1 -1 -1 -1
```

`poseidon.out`
```
18
```

## Explanation

There are $18$ ways to rearrange the treasures. One of them is:
```
-1 -1 -1 -1 -1 -1
-1  0  0 -1 -1 -1
-1  3  9  0 -1 -1
-1  4  1  0 -1 -1
-1  0  0 -1  0 -1
-1 -1 -1  6  0 -1
-1 -1  0  8  5 -1
-1 -1 -1 -1 -1 -1
