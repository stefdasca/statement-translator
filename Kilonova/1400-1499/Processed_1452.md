Leneșul is a very lazy animal. It moves only in straight lines but takes occasional breaks. In this problem, Leneșul needs to traverse a field represented by an $M \times N$ matrix of natural numbers from north to south and back. The values represent the effort required to traverse each area. Leneșul will choose a column for traversing the matrix, and for the breaks, $k1$ in number, it will choose areas adjacent to the path, either in the column to the left or the right. On the way back, it will follow the same process but will take $k2$ breaks. The problem's rules state that the two paths should not have common areas.

# Task

Given the dimensions $M, N$ of the field, the number of breaks $k1, k2$, and the effort for traversing each area of the field, determine:
1. The minimum effort to traverse the field from **North** to **South**, using $k1$ breaks.
2. The minimum effort to traverse the field from **North** to **South** and back from **South** to **North**, using $k1$ breaks on the **North-South** journey and $k2$ breaks on the **South-North** journey.

# Input data

The `lenes.in` file contains:
* The first line contains a natural number $p$ representing the task to solve. For all input tests, the number $p$ can only have a value of 1 or 2.
* The second line contains 4 natural numbers $M, N, k1, k2$ separated by a space as described above.
* The next $M$ lines contain $N$ natural numbers separated by spaces, representing the efforts to traverse each area of the field.

# Output data

* If the value of $p$ is 1, only Task 1 will be solved. In this case, the `lenes.out` file will contain a single natural number representing the minimum effort required to traverse the field from **North** to **South** under the given conditions.
* If the value of $p$ is 2, only Task 2 will be solved. In this case, the `lenes.out` file will contain a single natural number representing the minimum effort required to traverse the field in both directions from **North** to **South** and from **South** to **North** under the given conditions.

# Constraints and clarifications

* $3 \leq M, N \leq 500$;
* $0 \leq k1, k2 \leq M$;
* The values in the matrix are natural numbers in the range $[1, 1000]$;
* Leneșul can take breaks on the same line in both the left and right cells of the traversed column.
* The movement between the last area of the path from **North** to **South** and the first area of the path from **South** to **North** on return is with zero effort.

# Example 1

`lenes.in`
```
1
4 7 2 3
99 1 33 9 2 4 7
99 1 44 8 1 2 3
98 1 55 8 2 3 2
97 1 66 4 3 2 1
```

`lenes.out`
```
12
```

## Explanation

$p = 1$. Leneșul traverses the field from North to South on the 5th column with breaks in areas $(2, 6)$ and $(4, 6)$. **Attention! Only Task 1 is solved for this test.**

# Example 2

`lenes.in`
```
2
4 7 3 2
99 1 33 9 2 4 7
99 1 44 8 1 2 3
98 1 55 8 2 2 2
97 1 66 4 3 2 1
```

`lenes.out`
```
35
```

## Explanation

$p = 2$. Leneșul traverses the field from North to South on the 7th column with breaks in areas $(3, 6), (1, 6), (4, 6)$, and from South to North on the 5th column, with breaks in areas $(4, 4)$ and $(2, 6)$. **Attention! Only Task 2 is solved for this test.**

# Example 3

`lenes.in`
```
2
3 7 2 2
2 1 33 9 99 4 7
1 1 44 9 99 2 3
2 1 55 9 99 2 2
```

`lenes.out`
```
19
```

## Explanation

$p = 2$. Leneșul traverses the field from North to South on the 6th column with breaks in areas $(2, 7), (3, 7)$, and from South to North on the 2nd column, with breaks in areas $(3, 1)$ and $(2, 1)$. The effort of moving between areas $(3, 6)$ and $(3, 2)$ is zero. **Attention! Only Task 2 is solved for this test.**