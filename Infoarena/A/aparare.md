## Task

There are $N$ strategic points under the administration of the Ministry of Defense (MA). For $M$ pairs of points, the direct connection cost is known if a direct connection of the points in that pair is desired. Select a number of pairs of nodes whose connection will be effectively implemented, among the $M$, so that, at the end of the work, there is direct or indirect communication between any of the $N$ nodes through the realized connections and, in addition, the total cost of the works is minimal (it is guaranteed that this is always possible). The Ground Troops Command (CTU) will take over $5$ of the $N$ nodes, so that, according to the established connection strategy at $(1)$, the communication between any of the $5$ nodes is either direct or using only points taken over by CTU. Knowing that all connection costs (established at $(1)$) between the $5$ points will be paid by CTU, choose the $5$ nodes conveniently so that the cost of the connections (from $(1)$) remaining the responsibility of MA is minimal.

## Input data

The input file `aparare.in` contains on the first line the value of $N$, the number of strategic points, followed by the value of $M$, the number of pairs of strategic points for which the direct connection cost is known. Each of the following $M$ lines contains $3$ numbers: $i$, $j$, and $c$ $(1 \leq i < j \leq N)$ separated by a space, meaning that to directly connect points $x$ and $y$, the cost $c$ must be paid.

## Output data

The output file `aparare.out` will contain on the first line a natural number representing the total connection cost from $(1)$, and on the second line the remaining total cost after CTU has taken over the $5$ conveniently chosen strategic points.

## Constraints and clarifications

$5 \leq N \leq 100\ 000$  
$2 \cdot N \leq M \leq N \cdot (N - 1) / 2$  
$M \leq 500\ 000$  
Connection costs are strictly positive natural numbers, distinct two by two, with a maximum of $9$ digits each. The connection cost from node $i$ to node $j$ is the same as the connection cost from node $j$ to node $i$, for any $1 \leq i, j \leq N$. $40$\% of the score is awarded for the first correct value and $100$\% of the score for both correct values. To receive partial points, both required values must be displayed.

## Example

`aparare.in`  
`6 15`  
`1 2 5`  
`1 3 3`  
`2 3 11`  
`1 4 7`  
`2 4 2`  
`3 4 1`  
`1 5 6`  
`2 5 10`  
`3 5 4`  
`4 5 14`  
`1 6 9`  
`2 6 16`  
`3 6 8`  
`4 6 20`  
`5 6 18`  

`aparare.out`  
`18`  
`2` 

## Explanation

The pairs connected are: $1 - 3$, $3 - 4$, $3 - 5$, $3 - 6$, $2 - 4$ obtaining the minimum total cost $18$. Points $1$, $3$, $4$, $5$, and $6$ are taken over by CTU, with the associated connection costs, MA paying only the connection $2 - 4$ with a cost of $2$.