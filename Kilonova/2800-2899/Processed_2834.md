Matei needs black paint to paint his scooter. Everyone knows that black paint is obtained by mixing the same amount of red, yellow, and blue paint.

Matei has $N$ buckets of paint already mixed. The paint in the $i\\ (1 \\leq i \\leq N)$ bucket was obtained by mixing $r_i$ liters of red paint, $g_i$ liters of yellow paint, and $a_i$ liters of blue paint.

Matei wants to combine some of these buckets (possibly none) so that the resulting paint is black.

# Task 

What is the maximum amount (in liters) of black paint he can obtain?

# Input data

The first line contains $N$, the number of paint buckets.

The next $N$ lines each contain $3$ numbers, with line $i$ containing the numbers $r_i, g_i$, and $a_i$.

# Output data

Print a single number, the maximum amount of black paint that Matei can obtain.

# Constraints and clarifications

* $1 \\leq N \\leq 40$
* $0 \\leq r_i, g_i, a_i \\leq 10^6$
* Let $ S = \max \\{ \sum_{i=1}^{N} a_i, \\ \sum_{i=1}^{N} r_i, \\ \sum_{i=1}^{N} g_i \\}$

| # | Points | Constraints          |
| - | ------ | -------------------- |
| 1 | 27     | $1 \\leq N \\leq 20, 1 \\leq S \\leq 50$ |
| 2 | 36     | $1 \\leq N \\leq 30, 1 \\leq S \\leq 100$     |
| 3 | 37     | No additional constraints.      |

# Example

`stdin`
```
6
1 3 0
10 4 9
2 1 0
0 0 5
1 1 1
2 1 0
```

`stdout`
```
18
```

## Explanation

If we choose buckets $1, 3, 4, 5$, and $6$, we will have $6$ liters each of red, yellow, and blue paint, thus making a total of $18$ liters of black paint