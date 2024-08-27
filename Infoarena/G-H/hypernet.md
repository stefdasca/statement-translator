## Task

Determine the minimum total cost of a network consisting of $K$ hyperchannels.

## Input data

The first line of the input file `hypernet.in` contains 2 integers, separated by a space: $N$ and $K$. The $i$-th of the following $N$ lines contains the integer $Q_i$, representing the number of inhabitants of planet $i$.

## Output data

In the output file `hypernet.out` print the minimum total cost of a hyperchannel network having the specified properties.

## Constraints

$1 \leq N \leq 50000$

$N-1 \leq K \leq N \*(N-1)/2$

$1 \leq Q_i \leq 1000000$

## Example

`hypernet.in`
```
4 3
4
3
1
2
```

`hypernet.out`
```
42
```

`hypernet.in`
```
4 5
10
9
8
7
```

`hypernet.out`
```
117
```