# Path8

Marcel has a new challenge for you! He gives you two arrays $A$ and $B$ of length $N$ and asks you for the diagonal path with the maximum sum of elements in the matrix $C$ defined as follows: $C[i][j] = A[i] * B[j]$. A diagonal path is a path $D$ that starts in cell $(1, 1)$, ends in cell $(N, N)$, and only makes moves to the right and down.

## Input data

The input file `drum8.in` contains, in the first line, the number $N$, the dimension of arrays $A$ and $B$. The next two lines each contain $N$ numbers. The first line contains the elements of array $A$, and the second line contains the elements of array $B$.

## Output data

The output file `drum8.out` will contain the positions of the maximum sum path, in the order they are visited, each on a new line.

## Constraints

$1 \leq N \leq 100\ 000$.

$0 \leq A[i], B[i] \leq 2$.

For 20 points, $1 \leq N \leq 500$.

For another 20 points, $0 \leq A[i], B[i] \leq 1$.

If there are multiple paths that lead to the maximum sum, the lexicographically smallest one will be printed.

## Example

`drum8.in`

```
5
1 0 0 1 0
0 1 0 0 1
1
1 2
1 3
1 4
1 5
2 5
3 5
4 5
5 5
```

`drum8.out`

```
1 1
1 2
1 3
1 4
1 5
2 5
3 5
4 5
5 5
```

`drum8.in`

```
5
0 2 0 2 2
1 2 2 1 0
1
1 1
1 2
2 2
2 3
3 3
4 3
5 3
5 4
5 5
```

`drum8.out`

```
1 1
1 2
2 2
2 3
3 3
4 3
5 3
5 4
5 5
```

## Explanation

The path in the first example:
```
0 1 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
```

The path in the second example:
```
0 0 0 0 0
2 4 4 2 0
0 0 0 0 0
0 2 4 4 2
0 2 4 4 2
```