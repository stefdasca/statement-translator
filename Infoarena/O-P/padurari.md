# Woodsmen

Along a straight road, there are $N$ trees. $K$ woodsmen have been assigned the task of cutting down some of the trees. Each woodsman must cut exactly 2 trees. The woodsmen drive to the first tree they have to cut, and then walk to the other tree. They want to organize themselves in such a way that the sum of the distances they will walk is minimized.

## Input data

The input file `padurari.in` contains the numbers $N$ and $K$ on the first line. The next $N$ lines each contain one integer. The $i$-th line contains the distance $D_i$ from the $i$-th tree to the beginning of the road. The distances are given in increasing order.

## Output data

The output file `padurari.out` will contain a single integer representing the minimal sum of the distances the woodsmen will walk.

## Constraints

$2 \leq N \leq 200\,000$

$1 \leq K \leq \frac{N}{2}$

$0 \leq D_i \leq 10^9$

For $20\%$ of the tests, $N \leq 1\,000$.

## Example

`padurari.in` 
```
6 2
1
6
8
12
13
16
```

`padurari.out` 
```
3
```

## Explanation

One woodsman will cut trees $2$ and $3$ and another woodsman will cut trees $4$ and $5$.