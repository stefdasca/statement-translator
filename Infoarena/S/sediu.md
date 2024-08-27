# Headquarters

In a country, there are $N$ cities connected by roads, and there is a terrorist group threatening national security. Each road connects a pair of cities and is bidirectional. The road system is arranged so that between any two cities there is exactly one single path, traveling through the roads of the system. The government has decided to place the army's headquarters in one of the cities to minimize the number of cities controlled by the terrorist group. The terrorist group can control any subset of the remaining $N-1$ cities, so that between any two controlled cities, it is possible to travel through the roads of the road system without passing through the city where the army's headquarters is located. After the army places its headquarters in one of the cities, the terrorist group chooses the maximum possible number of cities to control that respect the aforementioned property.

## Task

Determine all the cities where the army can place its headquarters, so that the number of cities controlled by the terrorist group is minimized.

## Input data

The input file `sediu.in` contains the integer number $N$ on the first line. The following $N-1$ lines contain the numbers of two distinct cities, $a$ and $b$, with the property that there is a road connecting cities $a$ and $b$.

## Output data

The first line of the output file `sediu.out` will contain two integer numbers $O$ and $M$. $O$ represents the minimum number of cities controlled by the terrorist group and $M$ represents the number of cities that can be chosen as the headquarters for which the value $O$ is obtained. On the next line, $M$ integers will be printed, separated by spaces, representing the numbers of the cities where the army's headquarters can be placed. These numbers will be printed in ascending order.

## Constraints

$1 \leq N \leq 16\ 000$

## Example

``
sediu.in
7
1 2
2 3
2 4
1 5
5 6
6 7
``

``
sediu.out
3 1
1
``

## Explanations

If the army's headquarters is placed in city $1$, the terrorist group can control cities $2$, $3$, and $4$ or $5$, $6$, and $7$.