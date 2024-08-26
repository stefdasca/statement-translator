# Caibicol

Every day, farmer Ion takes all the horses out to get some fresh air so they can run and play. When the horses are done having fun, farmer Ion needs to take them back to the stables. To do this, he arranges them in a row, and the horses follow him to the stables. Since the horses are very tired, farmer Ion decides not to subject them to too much extra effort, so he comes up with the following algorithm: the first $P_1$ horses will enter the first stable, the next $P_2$ horses will enter the second stable, and so on. None of the $K$ stables should remain empty, and no horse should be left outside. Now, you should know that farmer Ion has only white and black horses, which do not get along very well with each other. If $x$ white horses and $y$ black horses enter a stable, then the aggression coefficient in that stable is $x*y$. The total aggression coefficient is equal to the sum of the aggression coefficients in each stable. Determine a way to distribute the $N$ horses into the $K$ stables, so as to minimize the total aggression coefficient.

## Task

## Input data

The first line of the input file `caibicol.in` contains the integers $N$ and $K$, separated by a space. The following $N$ lines contain the colors of the horses, in the order they are arranged in the row. If the $i$-th horse is white, then the $i$-th of these lines contains the number $0$; otherwise, it will contain the number $1$.

## Output data

The output file `caibicol.out` must contain the minimum possible total aggression coefficient.

## Constraints

$1 \leq N \leq 500$

$1 \leq K \leq N$

## Example

`caibicol.in` 
```
6 3
1
1
0
1
0
1
```

`caibicol.out`
```
2
```

## Explanation

The first $2$ horses will enter the first stable, the next $3$ horses will enter the second stable, and the last horse will enter the third stable.

