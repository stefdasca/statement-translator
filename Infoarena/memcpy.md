## Task

Given a matrix of dimensions $1000 \times 1000$ with distinct elements, we aim to copy the subarray of dimensions $N \times M$ that has the top left corner at $(X, Y)$ over the subarray of dimensions $N \times M$ that has the top left corner at $(NEW_X, NEW_Y)$. This must be accomplished using $N \times M$ assignments of the type $A[x][y] = A[z][t]$. Determine the minimum lexicographic order in which these assignments can be made to correctly copy the subarray.

## Input data

The input file `memcpy.in` will contain on a single line 6 numbers: $N$, $M$, $X$, $Y$, $NEW_X$, $NEW_Y$. These represent the dimensions of the subarray, the coordinates of the top left corner for the initial position of the subarray, and the final position respectively.

## Output data

The output file `memcpy.out` will contain a single natural number, `hash`, determined as follows:
```
int hash = 0, mod = 1e9 + 7;
for(int i = 1; i <= n * m; ++i) {
    hash += 1LL * i * response[i].x * response[i].y % mod;
    hash %= mod;
}
```
Where `response[i]` contains the coordinates of the cell that will be copied in operation number $i$.

## Constraints and clarifications

$1 \leq N, M \leq 1000$

All coordinates read or displayed will be in the range $[1, 1000]$.

The subarrays described in the input will be completely included in the matrix.

## Example

`memcpy.in`
```
4 4 1 1 2 2
```

`memcpy.out`
```
858
```

## Explanation

The cells will be copied in this order: $(1, 4)$; $(2, 4)$; $(1, 3)$; $(3, 4)$; $(2, 3)$; $(1, 2)$; $(4, 1)$; $(4, 2)$; $(3, 1)$; $(4, 3)$; $(3, 2)$; $(2, 1)$; $(4, 4)$; $(3, 3)$; $(2, 2)$; $(1, 1)$.