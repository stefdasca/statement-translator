Earth can be seen as a matrix with $N$ rows and $M$ columns, consisting only of digits $1$ and $0$, where $1$ represents an island and $0$ represents water. After extensive research, it has been discovered that each island needs at least $K$ neighboring positions with water to transform and become water. Neighbors of an island can be in the N, S, E, or W directions. Moreover, islands have the property of having **one special direction** (NE, SE, SW, or NW) representing another neighbor for that island. Transforming an island into water takes one year.

# Task
Knowing the islands, the number $K$ for each island, as well as each special direction:
1) Determine how many islands transform into water after one year.
2) For $Q$ queries of the form $(x, y)$, determine after how many years the island at position $(x, y)$ will become water. If it is not possible for $(x, y)$, print `-1`.

# Input data
The first line of the console contains 4 natural numbers, $C$, $N$, $M$, $P$, in this order, separated by a space. The following $P$ lines contain four natural numbers $x$, $y$, $K$, $d$, separated by a space, representing the coordinates of an island, the number of necessary neighbors for it to transform, and its special direction. For $d = 1$, the direction is NE, for $d = 2$, SE, for $d = 3$, SW, for $d = 4$, NW. If $C = 2$, then the next line contains the number of queries $Q$, and on the following $Q$ lines, the numbers $x$ and $y$, separated by a space.

# Output data
If $C = 1$, then the console will print the number of islands that transform into water after one year. If $C = 2$, then print the answer to each of the $Q$ queries, one per line.

# Constraints and clarifications
- $1 \leq N, M \leq 1000$
- $0 \leq K \leq 5$
- $1 \leq P \leq N \cdot M$
- $1 \leq Q \leq N \cdot M$
- $d \in \{1, 2, 3, 4\}$
- There is a chance that some neighbors may be outside the Earth. These will not be considered. For example, an island at position $(1, 2)$ with $K = 5$ cannot become water because the northern neighbor does not exist.
- It is guaranteed that for each of the $Q$ queries, $(x, y)$ represents a position where an island is located.
- Coordinate $x$ represents row $x$ in the matrix, and coordinate $y$ represents column $y$ in the matrix.
- In coordinates where there is no island, there is water.
- To solve this problem in C++, researchers recommend using the following lines of code at the beginning of the `main()` function:
```cpp
ios::sync_with_stdio(0);
cin.tie(0);
```
|#|Score|Constraints|
|-|-|--------|
|1|21|$C = 1$|
|2|23|$C = 2$, $1 \leq N, M \leq 50$|
|3|56|No additional constraints|

# Example 1
`stdin`
```
1 4 5 9
1 1 1 2
1 2 2 3
1 5 2 1
2 2 4 3
3 4 2 1
4 2 3 1
4 3 2 2
4 4 4 4
4 5 0 1
```

`stdout`
```
7
```

# Example 2
`stdin`
```
2 4 5 9
1 1 1 2
1 2 2 3
1 5 2 1
2 2 4 3
3 4 2 1
4 2 3 1
4 3 2 2
4 4 4 4
4 5 0 1
5
1 1
1 5
2 2
4 3
4 4
```

`stdout`
```
1
1
1
2
3
```

## Explanation
The image below corresponds to both examples. The numbers on an island represent the island's $K$ value, the arrows represent the island's special direction, and if the island's $K$ value is red, it means that island represents one of the $Q$ queries.

Let's discuss the island at position $(3, 4)$. It has $K = 2$, so it needs at least 2 neighbors to be water to transform itself into water. The special direction of this island is NE (north-east). Thus, the water neighbors of this island are in N, NE, E, and W. Since $4 \geq K = 2$, this island will transform into water.

The islands that transform into water after the first year are: $\{(1,1), (1,2), (1,5), (2,2), (3,4), (4,2), (4,5)\}$.

~[exemplu.png]