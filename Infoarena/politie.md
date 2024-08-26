# Police

Uncle Puiu, a notorious mobster in Bucharest, is wanted by the police! Bucharest's map is composed of $N$ intersections connected by $M$ bidirectional streets. Each street has two associated values: a danger level and a road category it falls into. In Bucharest, there are $D$ categories of roads: category $1$ is the best, then comes category $2$, $\dots$. Any police patrol moving from intersection $x$ to intersection $y$ will use the best available streets; if there is a path between $x$ and $y$ composed only of category $1$ streets, they will follow that one, regardless of the streets' danger levels. Otherwise, they will use a path composed of streets from categories $1$ or $2$. If there is no such path, they will use a path composed of streets from categories $1$, $2$, or $3$, and so on, ultimately accepting to use roads that contain streets from the last category, $D$. Of course, among all possible paths between two intersections that follow the above rules, the police will choose the one with the smallest maximum danger level of the streets used. Since the starting and destination intersections are not known beforehand, the police must consider all optimal patrol variants between any two intersections.

## Task

Given $N$, the number of intersections, $M$, the number of streets, $D$ the number of possible road categories, and the way the intersections are connected, determine, among the optimal patrol routes between any two intersections, the $P$ largest distinct danger levels that the police will have to traverse.

## Input data

The first line of the file `politie.in` contains $4$ natural numbers $N$, $M$, $D$, and $P$, as described in the statement. The next $M$ lines each describe a street in the city. The $i$-th of these lines describes the $i$-th street and consists of $4$ numbers: $x$, $y$, $t$, and $c$, representing that there is a street between intersections $x$ and $y$, which belongs to category $t$ and has a danger level $c$.

## Output data

The file `politie.out` must contain $P$ lines: the largest $P$ danger levels sorted in descending order. Attention! The $P$ danger levels must be distinct! In other words, if there are multiple roads containing a street with a danger level $y$, it should be printed only once!

## Constraints

$1 \leq N, D \leq 250\ 000$

$1 \leq P < N$ 

$1 \leq M \leq 500\ 000$ 

$1 \leq x, y \leq N$

$x \neq y$

$1 \leq t \leq D$ 

$1 \leq c \leq 1\ 000\ 000\ 000$

There cannot be more than one street between two intersections $x$ and $y$ 

## Example

`politie.in`
`5 5 2 3`
`1 5 2 1`
`1 2 1 3`
`2 3 1 4`
`2 4 2 1`
`4 3 2 2`

`politie.out`
`4`
`3`
`2`

## Explanation

The edges between $(2, 3)$, $(1, 2)$, and $(3, 4)$ must be traversed and form the three largest costs.

`politie.in`
`5 5 3 3`
`1 5 3 5`
`5 2 1 7`
`5 4 1 7`
`4 3 2 4`
`2 3 2 3`

`politie.out`
`7`
`5`
`4`

The edges between $(5, 4)$, $(5, 2)$, and $(1, 5)$ must be traversed and form the three largest costs.