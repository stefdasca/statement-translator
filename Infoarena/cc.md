## Task

In a room, there are $N$ contestants and $N$ computers. We know the distance each contestant must travel from their position to each computer. We want to assign each contestant to a computer in such a way that the sum of the distances traveled by the contestants is minimized. Determine this minimum sum of distances.

## Input data

The first line of the input file `cc.in` contains the integer number $N$, representing the number of contestants and computers. The next $N$ lines contain $N$ numbers each. The $j$-th number on the $i$-th of these $N$ lines represents the distance that contestant $i$ must travel to reach computer $j$.

## Output data

In the output file `cc.out`, you will print the minimum sum of distances traveled by the contestants for each to sit at a computer.

## Constraints

$1 \leq N \leq 100$

Each of the $N \times N$ distances is an integer from the interval $[1, 10\ 000]$

## Example

`cc.in`
```
5
7 9 2 1 6
9 10 11 12 13
8 3 11 6 7
6 6 6 6 6
9 5 3 9 8
```

`cc.out`
```
22
```

## Explanations

Contestant $1$ is assigned to computer $4$. 

Contestant $2$ is assigned to computer $1$. 

Contestant $3$ is assigned to computer $2$. 

Contestant $4$ is assigned to computer $5$. 

Contestant $5$ is assigned to computer $3$.