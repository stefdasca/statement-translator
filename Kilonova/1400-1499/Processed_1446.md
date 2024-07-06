Suleiman I encountered significant internal issues in the year 1548. During that year, he received news that a rebellion was being prepared in one of the regions of the Empire. The Empire's map is represented as a two-dimensional array with $n$ rows and $m$ columns, where each element of the array corresponds to a region of the Empire. In each region, soldiers were already stationed, but to prevent the rebellion, the sultan decided that all $k$ soldiers from the Imperial Guard would be sent to the regions, reinforcing those guarded by fewer soldiers. Their distribution respects the following rules:

* If there is a single region with a number of soldiers smaller than that of all other regions, send one soldier to this region.
* If there are multiple regions with the same minimum number of soldiers, send one soldier to the region that initially had a smaller number of soldiers. If multiple regions had the same initial number of soldiers, a soldier is sent to the region with the smaller row index, and if the regions are in the same row, to the region with the smaller column index.

Suleiman continues distributing the soldiers from the Imperial Guard to the regions as specified above, until the soldiers of the Imperial Guard are exhausted.

# Task

Given $n, m$ and $k$, representing the number of rows, columns, and the number of soldiers in the Imperial Guard, respectively, as well as the number of soldiers already present in the regions of the Empire, determine:

$a)$ the number of regions in the Empire where the soldiers of the Imperial Guard will be sent, and the minimum number of soldiers that will be found in a region after sending the soldiers from the Imperial Guard;

$b)$ the maximum distance between two regions **where soldiers of the Imperial Guard have been sent**. The distance between a region $A$ and a region $B$ is calculated using the formula $|L_A - L_B| + |C_A - C_B|$, where $(L_A, C_A)$ represents the coordinates of region $A$, indicated by the row and column numbers, respectively $(L_B, C_B)$ represents the coordinates of region $B$, indicated by the row and column numbers.

# Input data

The input file `rascoala.in` contains on the first line a natural number $p \in \{1,2\}$. The second line of the file contains three natural values $n, m$ and $k$, separated by a space, with the significance from the statement. Each of the next $n$ lines contains $m$ natural numbers, separated by a space, representing the number of soldiers initially present in each region.

# Output data

If the value of $p$ is $1$, then only **point $a)$** from the task will be solved. In this case, the output file `rascoala.out` will contain two natural values, each on a separate line, representing in order, the number of regions where Suleiman sent the soldiers from the Imperial Guard, and the minimum number of soldiers that are found in a region after sending the soldiers from the Imperial Guard.

If the value of $p$ is $2$, then only **point $b)$** from the task will be solved. In this case, the output file `rascoala.out` will contain a single natural number, representing the maximum distance between two regions where **soldiers of the Imperial Guard have been sent**.

# Constraints and clarifications

* $1 \leq n, m \leq 500$
* $1 \leq k \leq 1\ 000\ 000\ 000$
* the initial number of soldiers in any region is a non-zero natural number that does not exceed $1\ 500\ 000$
* $40\%$ of the tests will have the value $1$ on the first line, and the remaining $60\%$ of the tests will have the value $2$ on the first line.

# Example 1

`rascoala.in`
```
1 
3 4 6
5 3 4 6 
5 5 8 5 
9 6 8 7 
```

`rascoala.out`
```
3
5
```

## Explanation

A soldier is sent to the region $(1,2)$, obtaining two regions with 4 soldiers each. 
A soldier is sent again to the region $(1,2)$, (initial minimum number of soldiers), then a soldier to the region $(1,3)$. The remaining three soldiers will be sent as follows: the first to the region $(1,2)$, the second to the region $(1,3)$, and the third to the region $(1,1)$.

# Example 2

`rascoala.in`
```
2 
3 4 6
5 3 4 6 
5 5 8 5 
9 6 8 7
```

`rascoala.out`
```
2
```

## Explanation

The maximum distance will be $2$ between the regions $(1, 1)$ and $(1,3)$.