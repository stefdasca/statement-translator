# Points3

We have $N$ points on a horizontal line. We want to draw $M$ segments on this line so that each point is contained in at least one segment. What is the minimum possible length for the segment of maximum length?

## Input data

The input file `puncte3.in` contains on the first line $T$, the number of tests. Furthermore, each test has a single line that contains natural numbers $N$, $M$, $A$, $B$, $C$. $N$ and $M$ have the meaning from the statement. The coordinates of the $N$ points will be generated using the following relations ($X_i$ being the coordinate of the $i$-th point $i = 1 \dots N$):
$X_1 = 1$, 
$X_i = (X_{i-1} \times A + B \times i) \mod C$ for $i = 2 \dots N$

## Output data

The output file `puncte3.out` will contain on each line the required result for each of the $T$ tests.

## Constraints and clarifications

$T = 5$  
$1 \leq M < N \leq 10^5$  
$1 \leq A \leq 1000$  
$1 \leq B \leq 10^{10}$  
$1 \leq C \leq 10^{15}$  

## Example

`puncte3.in`
```
1
5 2 2 1 9
```
`puncte3.out`
```
3
```

## Explanation

The coordinates of the points are: 1, 4, 2, 8, 3. One possible solution is to use the segments $[1, 4]$ and $[8, 8]$. The length of the maximum segment is 3.