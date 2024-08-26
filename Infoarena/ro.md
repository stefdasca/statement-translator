## Task

In Romania, there are $N$ cities interconnected by $M$ highways. A highway connects exactly 2 cities (for example, the highways Bucharest-Pitești or Bucharest-Constanța). All highways are open to traffic in both directions, and it is possible to reach any city from any other city using the existing highways. Following the accession to the European Union, the government will need to take measures to comply with European infrastructure rules. These rules state that at least one of the two cities connected by a highway must have the status of a European capital. Initially, none of the $N$ cities has the status of a European capital, and for each one, the required sum (in millions of euros) to modernize and promote it to that status is known. Since government funds are limited, determine the minimum total amount the government will have to spend to promote some cities to the status of European capitals such that the European infrastructure rules are respected. To solve this problem, you have additional information from the government: no matter which subset of 14 cities out of the $N$ we choose, there is at least one pair of cities $A$ and $B$ in this subset such that there is a city $C$ different from $A$ and $B$ (not necessarily from the chosen subset) such that if all highways ending in $C$ are closed to traffic in both directions, then there will be no road between cities $A$ and $B$ using the remaining open highways. This condition can be reformulated as: If we look at Romania's road infrastructure as a connected undirected graph with $N$ nodes and $M$ edges, any biconnected component of this graph contains at most 13 nodes.

## Input data

The input file contains the integers $N$ and $M$ on the first line, separated by a space, representing the number of cities and the number of highways. The next line contains $N$ integers $S_i$, separated by a space, representing the required sums to promote each city $i$ (from 1 to $N$) to the status of a European capital. The next $M$ lines contain 2 distinct integers separated by a space, $U$ and $V$, indicating that there is a highway between city $U$ and city $V$.

## Output data

The output file will contain on the first line the minimum amount the government has to pay to comply with the European infrastructure rules. The second line will contain the number $O$, representing the number of cities promoted to the status of European capital. The third line of the file will contain $O$ distinct integers between 1 and $N$, separated by a space, representing the cities that were chosen to be promoted to the status of European capital.

## Constraints and clarifications

1 $\leq$ $N$ $\leq$ 2007

$N$ - 1 $\leq$ $M$ $\leq$ 10000

1 $\leq$ $S_i$ $\leq$ 1000000

Cities are numbered with integers from 1 to $N$.

There will be at most one highway between 2 different cities.

At least 20% of the test files will have $M = N - 1$.

The cities chosen to be promoted to the status of European capital can be displayed in any order.

## Example

`ro.in`

```
15 21
9 8 7 100 99 2 3 8 4 6 7 2 1 6 2
1 2
2 4
4 5
5 6
2 6
1 5
4 3
3 7
7 9
9 8
8 4
4 7
3 9
5 10
10 13
5 12
12 13
12 15
12 14
15 14
13 11
```

`ro.out`

```
129
9
1 4 6 7 9 10 12 13 15
```
