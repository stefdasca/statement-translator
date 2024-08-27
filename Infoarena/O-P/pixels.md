## Pixels

You are given an $N * N$ pixel matrix. Your task is to color each pixel in black or white such that the visual pleasure is maximized. To achieve this, you must know 3 rules. First, for each pixel, you know the amount of pleasure $A_{ij}$ it provides if it is colored white. Secondly, for each pixel, you know the amount of pleasure $B_{ij}$ it provides if it is colored black. Thirdly, you know for each pair of adjacent pixels (i.e., they share an edge) the pleasure cost $C_{ijk}$ that must be paid if they are colored differently. The pleasure cost is given for each pixel and for all 4 directions. In other words, for a given pixel at coordinates $(i, j)$, $C_{ij0}$ is the cost that must be paid if that pixel and the pixel at coordinates $(i - 1, j)$ are colored differently, $C_{ij1}$ is the cost that must be paid if that pixel and the pixel at coordinates $(i, j + 1)$ are colored differently, $C_{ij2}$ is the cost that must be paid if that pixel and the pixel at coordinates $(i + 1, j)$ are colored differently, and $C_{ij3}$ is the cost that must be paid if that pixel and the pixel at coordinates $(i, j - 1)$ are colored differently. If a pixel does not have a valid neighbor (i.e., one that is part of the matrix), the cost will still be given but will be 0. For example, $C_{110}$ will always be 0. $C_{ij0}$ and $C_{i-1j2}$ will always be the same, and so on (the cost for each pair is symmetric). You need to maximize the total pleasure, that is: the sum of $A_{ij}$ for all white pixels + the sum of $B_{ij}$ for all black pixels - the sum of the costs of adjacent pixels colored differently. Each pair of adjacent pixels colored differently contributes only once (not twice) to the total cost of adjacent pixels colored differently. Good luck!

## Input data

The input file `pixels.in` contains on the first line $N$, the size of the matrix. Then follow $N$ lines with $N$ values on each of them. The $j$-th value on the $i$-th line represents $A_{ij}$. In the same format follow $N$ lines with $N$ values representing $B_{ij}$. Finally, there are $N * N$ lines with 4 values on each line. The $(i - 1) * N + j$-th line in this group contains $C_{ij0}$ $C_{ij1}$ $C_{ij2}$ $C_{ij3}$.

## Output data

The output file `pixels.out` must contain a single line that represents the maximum pleasure that can be obtained.

## Constraints

$1 \leq N \leq 100$

$1 \leq A_{ij}$

$1 \leq B_{ij}$

$1 \leq C_{ijk} \leq 100$

10% of the tests will have $N = 4$

30% of the tests will have $N = 10$

## Example

`pixels.in`
```
2
1 10
2 2
10 1
3 3
0 1 1 0
0 0 0 1
1 1 1 53
0 0 1 0
0 0 53 24
```

`pixels.out`
```
24
```

## Explanation

The maximum pleasure is obtained by coloring Black White Black Black.

Note that the pixels $(2, 1)$ and $(2, 2)$ have a very high cost of being colored differently, so you will color them the same, with black being the best option.