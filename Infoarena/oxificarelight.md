# Oxification Light

In this problem, you need to place $N + 1$ points on the axis of real numbers while respecting certain constraints. Specifically, you are given a sequence $lungime$ of $N$ elements. The points must be placed on the axis such that:
- The distance on the axis between point number $i$ and point number $i + 1$ must be exactly $lungime[i]$.
- The distance between the leftmost placed point and the rightmost placed point must be as small as possible.

## Input data

The input file `oxificarelight.in` will contain on its first line the number of tests, $T$. The structure of a test is as follows:
The first line contains the natural number $N$. 
The second line contains $N$ natural numbers, representing, in order, the elements of the sequence $lungime$.

## Output data

The output file `oxificarelight.out` will contain $T$ values: for each test, you must print the minimum possible distance between the leftmost point and the rightmost point in an optimal placement.

## Constraints

$1 \leq N \leq 1\,000$

$1 \leq lungime[i] \leq 5\,000$

The sum of the values of $N$ in the same input file is less than or equal to $6\,000$.

For tests worth 50 points, it is additionally guaranteed that:

$1 \leq N, lungime[i] \leq 100$

$1 \leq T \leq 25$

Among these, there are tests worth 20 points, for which it is additionally guaranteed that $lungime[i] \leq lungime[i + 1]$ for all $1 \leq i \leq N - 1$.

## Example

`oxificarelight.in`

```
2
3
5 5 5
3
5 4 5
```

`oxificarelight.out`

``>
15
14
```

## Explanation

One solution for the first test is the list of points $\{1, 6, 1, 6\}$.

One solution for the second test is the list of points $\{0, 5, 1, 6\}$.