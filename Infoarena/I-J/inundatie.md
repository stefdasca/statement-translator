Flood

Mitruţ, the booted cat, gives you the map of a magic city inhabited by ants, which has the shape of a rectangular matrix with $N$ rows and $M$ columns. It can be considered that in each cell $(i, j)$ of the matrix, with $i=1,2,\dots,N$ and $j=1,2,\dots,M$, there is a building whose number of floors $e_{i,j}$ is known. Since Mitruţ also tasted the magic cake, he gained supernatural powers and is now thinking about punishing the greedy ants by flooding the city. Thus, Mitruţ asks $Q$ questions such as what is the total number of affected dwellings if he pumps water into the city up to level $e_q^k$ $(k=1,2,\dots,Q)$?

## Task

Answer the $Q$ questions asked by Mitruţ.

## Input data

The first line of the input file `inundatie.in` contains the natural numbers $N$ and $M$. The next $N$ lines each contain $M$ natural numbers. The number $j$ on line $i$ represents how many floors the building located in cell $(i, j)$ on Mitruţ’s map has. The following line contains the natural number $Q$, and the last $Q$ lines contain each a natural number representing Mitruţ’s question.

## Output data

The output file `inundatie.out` must contain the answers to the $Q$ questions asked by Mitruţ.

## Constraints and clarifications

$1 \leq N, M \leq 300$

$1 \leq Q \leq 100 000$

$0 \leq e_{i,j} \leq 1\ 000\ 000\ 000$ $(i=1,2,\dots,N, j=1,2,\dots,M)$

$0 \leq e_q^k \leq 1\ 000\ 000\ 000$ $(k=1,2,\dots,Q)$

For 30% of the tests: $Q \leq 1000$ and $N, M \leq 50$.

Each floor of a building houses a single dwelling. Floor numbering starts from 1.

If $e_{i,j} = 0$, then there is no building in cell $(i, j)$. For a question $e_q^k$, all dwellings located at a floor lower than $e_q^k$ must be completely flooded, while those dwellings located at a floor higher or equal must remain untouched.

## Example

`inundatie.in`

```
3 3
7 3 5
0 2 0
5 0 2
4
2
4
1
5
```

`inundatie.out`

```
6
16
0
19
```

## Explanation

For Mitruţ’s first question, all dwellings located at floors lower than level $2$ will be flooded. There are $6$ such dwellings (the dwellings on the 1st floor in the buildings located at $(1,1)$, $(1,2)$, $(1,3)$, $(2,2)$, $(3,1)$, $(3,3)$).