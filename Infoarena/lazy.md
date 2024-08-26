## Task

Everybody knows that workers in Romania are very lazy. One of these workers is $Dorel$, who works for a company that builds roads across the country. Yesterday he received a new task: he was specified $N$ cities in Romania (numbered from $1$ to $N$), $M$ bidirectional roads (numbered from $1$ to $M$) which are not yet constructed, each connecting exactly two cities; among these roads, he has to select and construct $N-1$ such that all cities become connected. Unfortunately, this problem is not very simple for $Dorel$: each road $i$ has two associated costs: $C1_i$ – the effort needed to construct the road and $C2_i$: $C1_i * C2_i$ being the profit made from constructing the road. Of course, $Dorel$ wants to work as little as possible so the most important thing is that the sum of the costs of built roads is minimal; if there are multiple ways to build roads such that the total cost is minimal, $Dorel$ wants the total profit (the sum of the profits for each road) to be maximal. You need to solve $Dorel$'s problem!

## Input data

The first line of the file `lazy.in` contains two numbers $N$ and $M$, the number of cities, respectively the number of roads. The next $M$ lines, the $i$-th of these lines, contain $4$ natural numbers: $a_i$ and $b_i$ representing the cities the road $i$ connects, $C1_i$, and $C2_i$.

## Output data

The output file `lazy.out` must contain $N-1$ numbers representing the indices (according to the input file) of the roads that $Dorel$ has to choose.

## Constraints and clarifications

$1 \leq N, M \leq 200000$

$1 \leq a_i, b_i \leq N$

$1 \leq C1_i < 10^{17}$

$-10^{17} < C2_i < 10^{17}$

If there are multiple solutions, any of them is accepted.

## Example

`lazy.in`
```
3 3 
1 2 1 7 
2 3 3 2 
1 3 2 3
```

`lazy.out`
```
1 3
```

## Explanation

In the given example, out of the three possible roads, roads 1 and 3 are chosen to minimize the total construction cost, thereby keeping all cities connected.