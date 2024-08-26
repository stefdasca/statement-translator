## Kinetic

Given $N$ points moving along the $Ox$ axis. The position of the $i$-th point at time $t$ is given by the formula: $a_i + b_i * t$. You also have $M$ queries of the form $x \ y \ t$. For each query, you need to determine how many points are between coordinates $x$ and $y$ (inclusive) at time $t$.

## Input data

The input file `kinetic.in` will contain on the first line 2 natural numbers $N$, and $M$, the number of points, and the number of queries, respectively. The following $N$ lines will each contain 2 values. Thus, the $(i+1)$-th line will contain the values $a_i$, and $b_i$. The next $M$ lines will each contain 3 values, $x$, $y$ and $t$ representing the interval on the $Ox$ axis at time $t$ for which the query is made.

## Output data

The output file `kinetic.out` must contain $M$ lines, one for each query. Thus, the $i$-th line in the output file must contain the answer for the $i$-th query.

## Constraints

$1 \leq N \leq 500$  
$1 \leq M \leq 200\ 000$  
$-10\ 000 \leq a_i, b_i \leq 10\ 000$  
$-1\ 000\ 000\ 000 \leq x, y \leq 1\ 000\ 000\ 000$  
$0 \leq t \leq 1\ 000\ 000$

## Example

`kinetic.in` 
```
3 3
-9 -1
-2 -5
5 -8
91 -66 10
-73 38 4
86 23 7
```

`kinetic.out`
```
2
3
0
```

## Explanation

At time $10$ the points will be at coordinates $-9 + 10 * (-1) = -19$, $-2 + 10 * (-5) = -52$ and $5 + 10 * (-8) = -75$. Among these, only the first 2 are between $91$ and $-66$ on the $Ox$ axis.