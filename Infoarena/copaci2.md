# Trees 2

Zaharel has $N$ trees in his backyard, arranged in a line, conveniently numbered from left to right from $1$ to $N$. Wanting his garden to look as beautiful and uniform as possible, he aims to minimize the maximum difference between the heights of adjacent trees. The trees cannot be moved from their places, but their heights can be decreased or increased (using modern gardening techniques). Each tree has a height $H_i$ and a cost $C_i$ to increase or decrease its height by one unit. Knowing that he has a budget of value $K$, determine the minimum value for the maximum difference between the heights of adjacent trees.

## Input data

The first line of the input file `copaci2.in` contains two natural numbers $N$, $K$, separated by spaces. The next $N$ lines contain two natural numbers $H_i$, $C_i$, separated by spaces.

## Output data

The first line of the file `copaci2.out` will contain a single natural number representing the minimum value for the maximum difference between the heights of adjacent trees.

## Constraints

$1 \leq N \leq 1000$  
$1 \leq K \leq 10^9$  
$1 \leq H_i, C_i \leq 1000$  
A tree can be reduced to a height of $0$

## Example

`copaci2.in`  
6 9  
8 3  
9 2  
4 3  
7 6  
4 2  
3 4  

`copaci2.out`  
2  

## Explanation

The height of tree $2$ is decreased by $2$ units and the heights of trees $3$ and $5$ are increased by one unit. The new heights will be $8, 7, 5, 7, 5, 3$ and the maximum difference between the heights of adjacent trees is $2$. The total cost is $2*2 + 1*3 + 1*2 = 9$.