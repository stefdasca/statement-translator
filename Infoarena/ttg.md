## Task

Time Travel Gossip

It is said that time is infinite. Fortunately, Walman decided that time should start from year $1$. Thus, consider the infinite axis of time beginning from the time numbered $1$. It is known that a new gossip appears each year (gossip is created by Walman). According to logic, all gossip is passed forward in time: at time $i$, all the gossip from $1$ to $i$ is known, but gossips from the future are not known (the past is known, but not the future). However, the Brigade of Trickery has decided to oppose the logic of time by becoming time travelers. The Brigade of Trickery has $M$ time travelers, and for each traveler, their lifespan is known, as well as the years during which they live their life. Thus, a representative can travel from the future to the past, making all the gossip discovered in the future public in the present (if a traveler comes from the future to time $i$, officially from time $i$, not only the gossip from $1$ to $i$ are known, but also other gossips from the future, depending on the amount of information held by that traveler). Given $M$ the number of travelers, their lifespan, and the years they travel through, answer the $N$ queries of the type $time$: how many gossips are known at time $time$.

## Input data

The input file `ttg.in` will contain on the first line $2$ numbers $M$ and $N$. The next $M$ lines will contain: $lifespan_i$ (how long traveler $i$ lives), followed by $lifespan_i$ values representing the years in which they live (in the given order). The next $N$ lines will contain one number $time$, representing the $N$ queries.

## Output data

The output file `ttg.out` will contain $N$ lines, where line $i$ contains the answer to query $i$.

## Constraints

$1 \leq lifespan_i$

The sum of lifespans will not exceed $100\ 000$

$1 \leq N \leq 100\ 000$

All times in the input data (both travelers' times and query times) belong to the interval $[1, 2\ 000\ 000\ 000]$

For $20\%$ of tests $M = 1$

For another $20\%$ of tests, the sum of lifespans is less than $1000$

For another $20\%$ of tests, the times used are up to $100\ 000$

For another $20\%$ of tests, $N \leq 1000$

## Example

`ttg.in`

```
1 3
4
100 46 1000 96
20
50
1001
```

`ttg.out`

```
1000
1000
1001
```

## Explanation

We have a single traveler. This traveler begins their life in the year $100$ (automatically learning all the gossips from $1$ to $100$). Then, they travel to the year $46$ (so in year $46$, all gossips from the interval $[1,100]$ are known). Note: since history is passed on, all the years in the interval $[46,100]$ will also know the gossips $[1,100]$. In step $3$, the traveler goes to the time $1000$ where they learn the gossips $[1,1000]$. Finally, they reach the year $96$, a year in which all the gossips from $1$ to $1000$ are revealed. We observe that since the information is passed through time, if in the year $96$ we have the gossips from $1$ to $1000$, then in the year $100$ we will also have access to these gossips. As a result, our traveler, when they initially set off from the year $100$, knew both the gossips $[1,100]$ and those from $101$ to $1000$. Automatically, we realize that at time $46$ all gossips from $1$ to $1000$ are also known. The answer to the $3$ queries is derived from the analyses made.