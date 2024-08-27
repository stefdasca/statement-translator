# Airplanes2

Mihai and Alexandra decided to go on vacation abroad. Mihai's problem is that Alexandra always has to decide whether it is worth going on a particular trip or not (depending on money, time, etc.). Let there be $N$ airports (represented as the nodes of a graph) and $M$ flights (the edges of the graph). For each flight, the index of the airport and the time at which the plane takes off, the index of the airport and the time at which the plane lands, and the ticket price for that flight are known. Mihai and Alexandra are in airport 1 at time $0$. Mihai has to answer $K$ queries of the type $(x, y)$: what is the minimum price to get to airport $x$ by time $y$ at the latest.

## Input data

The input file `avioane2.in` will contain on the first line 3 natural numbers $N$, $M$, and $K$. The next $M$ lines contain 5 values representing the details of a flight: $A$, $T_{dec}$, $B$, $T_{Ater}$ (the plane leaves from $A$ at time $T_{dec}$ and arrives in $B$ at time $T_{Ater}$) and $P$, the ticket price. The following $K$ lines contain 2 natural numbers representing the queries of the type $(x, y)$.

## Output data

The output file `avione.out` will contain $K$ lines, the answer for each query. If it is not possible to reach a certain airport by a given time, print $-1$.

## Constraints and clarifications

$1 \leq N \leq 30\ 000$

$1 \leq M \leq 90\ 000$

$1 \leq K \leq 120\ 000$

All other values are within the interval $[1, 10^9]$

Mihai and Alexandra only need to pay for a single ticket for each flight. The characters can wait as long as they want at an airport (having a coffee) for the next flight.

$T_{dec} < T_{Ater}$ for each of the $M$ flights

## Example

`avioane2.in`
```
5 7 6 
1 4 5 8 69 
2 14 3 17 25 
4 2 5 10 564 
5 8 2 13 12 
3 20 1 25 54 
2 4 4 7 34 
1 1 3 8 1000 
3 10 
3 20 
5 7 
2 20 
1 100 
5 13 
```

`avioane2.out`
```
1000 
106 
-1 
81 
0 
69 
```