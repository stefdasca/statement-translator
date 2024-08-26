## Task

Balaurul Arhirel faces a great dilemma. Unintentionally, he ended up in the mountains of Romania and must traverse a route along which he needs to visit $N$ cabins. He can start from any cabin, but he must visit each cabin exactly once. The cabins are numbered from $1$ to $N$, and each is located at a height equal to its index expressed in meters. Traveling between any two cabins is done in a straight line (increasing or decreasing constantly). The problem is that Arhirel cannot climb or descend more than $K$ meters between any two consecutive cabins on the route, so the route must be well chosen. The good news is that there are many possibilities. The bad news for you is that Arhirel knows how many possibilities there are and wants to see if you know too. For the given values of $N$ and $K$, determine the number of possibilities to visit each of the $N$ cabins exactly once, such that the level difference (in absolute value) between any two consecutively visited cabins is at most $K$ meters. The result must be given modulo $30103$ (the remainder of the division by $30103$).

## Input data

The input file `cabane.in` will contain on the first line the values of $N$ and $K$ separated by a space.

## Output data

The output file `cabane.out` will contain a single line that will print the total number of possibilities modulo $30103$.

## Constraints and clarifications

$K \leq N$

$1 \leq K \leq 6$

## Example

`cabane.in`  
```
4 2
```

`cabane.out`  
```
12
```

## Explanation

Out of the $24$ possible routes, $12$ are valid:  
$1 2 3 4$,  
$1 2 4 3$,  
$1 3 2 4$,  
$1 3 4 2$,  
$2 1 3 4$,  
$2 4 3 1$,  
$3 1 2 4$,  
$3 4 2 1$,  
$4 2 1 3$,  
$4 2 3 1$,  
$4 3 1 2$,  
$4 3 2 1$

And the other $12$ are not. For example, $2 1 4 3$ is not valid because there is a difference of $3$ meters between cabin $1$ and cabin $4$.