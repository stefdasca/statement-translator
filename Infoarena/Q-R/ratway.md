## Task

"You could say the Ratway is the city under the city. Dark, dangerous, and no place for decent folk." The city of Riften in the province of Skyrim is known for its underground network of tunnels, called "The Ratway". This network consists of bidirectional tunnels and tunnel intersections, so it can be represented by a connected undirected multigraph (each intersection is associated with a node, and each tunnel is associated with an edge between corresponding nodes; there may be multiple edges between the same nodes, and there may be edges from a node to itself). The Ratway also contains the headquarters of the Thieves' Guild of Skyrim. Brynjolf, one of its leaders, wants to develop a new system of traps to keep the guards away, but first the tunnel network must meet a few constraints: the tunnels must be directed (can be traversed in one direction only, otherwise, the traps would be activated), for any intersection, both the number of entrances and the number of exits must be even numbers (an entrance is a tunnel directed from any intersection to the current intersection, and an exit is a tunnel directed from the current intersection to any intersection). Help Brynjolf direct the tunnels to meet the above constraints. If it's not possible, construct a minimum number of tunnels, which you must also direct so that the resulting network meets the restrictions.

## Input data

The first line of the `ratway.in` file will contain two natural numbers $N$ and $M$, representing the number of intersections and the number of initial tunnels. Each of the next $M$ lines will contain two natural numbers, $x$ and $y$, meaning that there is a tunnel between intersections $x$ and $y$ (the intersections are represented by natural numbers from $1$ to $N$).

## Output data

The first line of the `ratway.out` file should contain $K$, the minimum number of tunnels in the final network. Print each of the next $K$ lines with two numbers, $x$ and $y$, indicating that we have a tunnel directed from node $x$ to node $y$. Among the tunnels printed, the tunnels from the initial configuration must be included, each assigned exactly one of the two possible directions. If there are multiple solutions with a minimum $K$, print any of them.

## Constraints

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 200\ 000$

For 15% of the points

$1 \leq M \leq 20$

No additional tunnels need to be constructed

For another 30% of the points

$1 \leq N \leq 1\ 000$

$1 \leq M \leq 2\ 000$

## Example

`ratway.in`

```
3 4
1 2
2 3
1 1
3 3
```

`ratway.out`

```
6
1 1
2 1
2 3
1 3
3 1
1 1
```

## Explanation

The edges from the input file are directed as follows: $1 \leftarrow 2$, $2 \rightarrow 3$, $1 \rightarrow 1$, $3 \rightarrow 3$. Additional directed tunnels are added: $3 \rightarrow 1$, $1 \rightarrow 1$. For node $1$ we have: $4$ entrances, $2$ exits. For node $2$ we have: $0$ entrances, $2$ exits. For node $3$ we have: $2$ entrances, $2$ exits.