# Aiacuhexagoane

A plane can be tiled using regular hexagons of the same size. An ant can move from one hexagon to another only if the two hexagons are connected through the side of a neighboring common hexagon, as shown in the figure (e.g., from hexagon $1$ it can reach hexagon $5$, because they are connected through the side of hexagon $2$, which is a neighbor to hexagons $1$ and $5$). A part of the plane is taken and forms a hexagonal grid. The hexagonal grid will have $N$ lines. Odd lines contain $M$ hexagons each, while even lines contain $M-1$ hexagons each. The hexagons in the grid are numbered as shown in the adjacent figure. Given $Q$ pairs of hexagons $(h_1, h_2)$, it is required to determine if the ant, starting from $h_1$, can reach $h_2$, possibly passing through other intermediate hexagons to form a path.

## Input data

The input file `aiacuhexagoane.in` contains on the first line two natural numbers $N$ and $M$, representing the number of lines and the number of hexagons on the first line, respectively. The next line contains a natural number $Q$, representing the number of queries, and each of the following $Q$ lines contains two numbers separated by a space, representing the values $h_1$ and $h_2$ from the statement.

## Output data

The output file `aiacuhexagoane.out` contains $Q$ lines, corresponding to the $Q$ pairs of hexagons. For each pair, `da` will be printed if there is a path between the pair of hexagons, or `nu` otherwise.

## Constraints and clarifications

$1 \leq N \leq 10^9$  
$2 \leq M \leq 10^9$  
$1 \leq Q \leq 10^5$

For test cases worth $20$ points $N, M \leq 15$.

For test cases worth $65$ points $N, M \leq 800$.

The problem will be evaluated on test cases worth $90$ points.

The examples will represent test cases worth $10$ ("default points") and will come with feedback.

The $Q$ pairs of hexagons will be unique. Attention: the pair of hexagons $h_1$ and $h_2$ is different from $h_2$ and $h_1$. $h_1 ≠ h_2$

## Example

`aiacuhexagoane.in`  
```
2 3
3
1 5
1 2
3 4
```

`aiacuhexagoane.out`  
```
da
nu
da
```

## Explanation

There is a path between hexagon $1$ and hexagon $5$ passing the side of hexagon $2$. There is no path between hexagon $1$ and hexagon $2$, hexagon $2$ being isolated from all the others. There is a path between hexagon $3$ and hexagon $4$ passing the side of hexagon $2$.