In the region of Ionia of the ancient Greek world, a region corresponding to the current territory of the Aegean Sea, there are several islands. The sea map is represented by an $N \times M$ matrix, having values of $1$ and $0$, and each element of the matrix represents a $1 \times 1$ area of the sea. The rows of the matrix are numbered from $1$ to $N$, from top to bottom, and the columns from $1$ to $M$, from left to right. Thus, the top-left corner of the matrix is associated with the area $(1, 1)$, and the bottom-right corner corresponds to the area $(N, M)$. An element containing the value 0 means that in that area there is water. An island is determined by a rectangle formed entirely of values of $1$. It is guaranteed that all areas containing the value $1$ form valid rectangles and that any two islands are separated by water. For example, Figure $1$ below represents a valid map, while Figures $2$ and $3$ do NOT represent a valid map.

~[img1.JPG|align=center]

# Task
The Ionians, being practical people, want to build a lighthouse-library (placed on a $1 \times 1$ platform) in an area covered by water. The position of the platform will be chosen in a cell $C$ such that the sum of the distances between all the islands and $C$ is minimized. The distance between a cell $C$ and an island is defined as the minimum of the Manhattan distances between $C$ and each cell belonging to the island (the distance can pass through other islands as well as areas covered by water). The Manhattan distance between two cells located at row $x1$ and column $y1$, respectively at row $x2$ and column $y2$, is defined as $|x1 - x2| + |y1 - y2|$, where $|x|$ represents the absolute value of $x$.

# Input data

The input file `arhipelag.in` contains, on the first line, the values $N$ and $M$, having the meaning from the statement. The next $N$ lines contain $M$ binary values, separated by a space, representing the sea map.

# Output data

The output file `arhipelag.out` will contain a pair of natural numbers, representing the row and column of the cell chosen by the Ionians for construction. If there are multiple possible solutions, the one with the minimum row will be chosen. If there are still multiple solutions, the one with the minimum column will be chosen.

# Constraints and clarifications

* For tests worth $15$ points, $1 \leq N, M \leq 50$;
* For other tests worth $20$ points, $1 \leq N, M \leq 300$, and the number of islands in the archipelago does not exceed $300$;
* For other tests worth $20$ points, $1 \leq N, M \leq 300$;
* For the rest of the tests, $1 \leq N, M \leq 1 \ 000$;
* It is guaranteed that there is at least one area covered by water;

# Example 1

`arhipelag.in`
```
7 7
0 1 0 1 0 1 1
0 1 0 1 0 1 1
0 0 0 1 0 0 0
0 0 0 1 0 0 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 1 1
```

`arhipelag.out`
```
2 3
```

## Explanation

Denoting with $D(x1, y1, x2, y2)$ the island determined by the rectangle having the top-left corner at $(x1, y1)$ and the bottom-right corner at $(x2, y2)$, the archipelago contains the following islands: $D1(1, 2, 2, 2)$, $D2(1, 4, 7, 4)$, $D3(1, 6, 2, 7)$, $D4(6, 1, 7, 2)$ and $D5(6, 6, 7, 7)$. Denoting with $dist(D)$ the distance between the cell $(2, 3)$ and the island $D$, the distances are as follows: $dist(D1) = min \{|2 - 1| + |3 - 2|, |2 - 2| + |3 - 2|\} = 1$, $dist(D2) = 1$, $dist(D3) = 3$, $dist(D4) = 5$ and $dist(D5) = 7$.

# Example 2

`arhipelag.in`
```
4 4
0 0 1 1
0 0 1 1
0 0 1 1
0 0 0 0
```

`arhipelag.out`
```
1 2
```

## Explanation

For each of the cells $(1, 2)$, $(2, 2)$, $(3, 2)$, $(4, 3)$ and $(4, 4)$, the distance between the cell and the only existing island in this example is the same. The one with the minimum row will be chosen, and in case of a tie, the one with the minimum column will be chosen. Thus, the cell $(1, 2)$ represents the solution.