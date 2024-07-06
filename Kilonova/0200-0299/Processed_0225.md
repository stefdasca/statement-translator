~[rectangles.jpg|align=right]

*"The real world is horrible and awful."*

In the end, Alex decided to return home... but which home? He still hasn't built his house. The town of Jluc can be viewed as an `M × M` matrix. Alex wants to build his house in a sub-matrix of this matrix. However, on the way to *Piezișă*, he set traps in `N` cells of the matrix (the fewer people reach *Piezișă*, the more milk for Alex). Obviously, he does not want to build his house on any traps (and besides, the traps can still be useful), so he asks himself in how many ways he can build his house.

# Interaction Protocol

To solve the problem, you need to implement the function:
```cpp
int countRectangles(int M, std::vector <std::pair <int , int >> points );
```
`M` represents the size of the matrix, and the parameter `points` represents the cells where the traps are located. The returned value is the total number of rectangles, modulo `6700417`. The function will be called **only once** per test.

# Constraints

* `0 \leq N \leq 200 000`
* $1 \leq M \leq 10^9$
* $0 \leq x_i, y_i < M$ for any `0 \leq i \leq N − 1`
* $x_i ≠ x_j $ or $ y_i ≠ y_j $ for any `i ≠ j`
* **Attention! The scores for this problem were generated randomly**.
* You need to include "rectangles.h"

## Subtask 1 (2 points)
* `1 \leq M \leq 20`
## Subtask 2 (4 points)
* `1 \leq M \leq 100`
## Subtask 3 (7 points)
* `0 \leq N \leq 20`
## Subtask 4 (4 points)
* `1 \leq M \leq 700`
## Subtask 5 (8 points)
* `0 \leq N \leq 80`
## Subtask 6 (3 points)
* $1 \leq M^2N \leq 50 \ 000 \ 000$
## Subtask 7 (9 points)
* `0 \leq N \leq 700`
## Subtask 8 (2 points)
* `1 \leq M \leq 1 600`
## Subtask 9 (4 points)
* `1 \leq M \leq 5 000`
## Subtask 10 (4 points)
* `1 \leq M \leq 25 000` and `0 \leq N \leq 2 500`
## Subtask 11 (5 points)
* `0 \leq N \leq 3 000`
## Subtask 12 (10 points)
* `0 \leq N \leq 5 000`
## Subtask 13 (9 points)
* `0 \leq N \leq 20 000` and `1 \leq M \leq 200 000`
## Subtask 14 (8 points)
* `0 \leq N \leq 20 000`
## Subtask 15 (21 points)
* No other constraints

# Examples

`stdin`

```
3 2
0 1
2 2
```

`stdout`

```
17
```
Explanations
---

The matrix looks like this:
```java
o # o
o o o
o o #
```

There are:
`7` sub-matrices of `1×1`
`3` sub-matrices of `1×2`
`1` sub-matrix of `1×3`
`4` sub-matrices of `2×1`
`1` sub-matrix of `3×1`
`1` sub-matrix of `2×2`

`stdin`

```
5 3
1 2
2 2
2 3
```

`stdout`

```
108
```
Explanations
---

In total, there are `108` sub-matrices

`stdin`

```
1000000000 0
```

`stdout`

```
1974342
```