Transport2

It is known that a vehicle cannot travel on a road unless its weight does not exceed the maximum authorized weight of the road. The weight of the vehicle is calculated including passengers, goods, etc.

## Task

Thus, a map is given in the form of an undirected graph, where the nodes numbered from $1$ to $n$ represent the localities, and the edges represent the roads, along with a maximum authorized weight. Determine the maximum weight of a vehicle that can legally travel from the source (node $1$) to the destination (node $n$).

## Input data

The input file `transport2.in` contains on the first line two natural numbers $n$ and $m$, representing the number of nodes and, respectively, the number of edges. The next $m$ lines contain three natural numbers $x$ $y$ $w$, separated by a space, representing an edge with a maximum authorized weight $w$ between nodes $x$ and $y$.

## Output data

In the output file `transport2.out` you will print a single value, representing the maximum admissible weight of a vehicle that can legally travel from node $1$ to node $n$.

## Constraints and clarifications

$2 \leq n \leq 100\,000$

$1 \leq m \leq 200\,000$

$1 \leq w \leq 10\,000$

The Minister of Transport has decided that all roads have the maximum authorized weight as an integer.

It is guaranteed that there is at least one road connecting node $1$ to node $n$.

## Example

`transport2.in`

```
6 9
1 2 5
1 4 3
2 4 2
2 3 6
4 5 4
3 4 5
5 3
6 3
5 6 5
```

`transport2.out`

```
4
```

## Explanation

The solution corresponds to the route $1 - 2 - 3 - 4 - 5 - 6$ which has costs $5$, $6$, $5$, $4$ and respectively $5$. Any other route will have a maximum authorized weight less than $4$.