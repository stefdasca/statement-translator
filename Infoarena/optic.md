## Task

N switches, numbered from $1$ to $N$, are interconnected in a network through fiber optic connections. The network has a tree structure. The root of the tree is represented by switch number $1$, which is considered to be situated at the highest level in the tree. A connection links $2$ switches and is unidirectional (oriented from the switch at a higher level to the one at a lower level). The switch numbered $1$ must transmit very important information regarding the network's state to all the other switches. To achieve this, a smart broadcast strategy (transmission to all switches) must be established. At any given moment, a switch $A$ that holds the information (initially, at time $0$, only switch $1$ holds the information) can establish an optical path to a switch $B$ located in the subtree of switch $A$. The optical path consists of switches $A$, $B$, and all other switches located on the unique (and oriented) path from $A$ to $B$. Establishing the optical path takes $1$ unit of time, with information transmission then occurring instantaneously. At the end of the transmission along the established optical path, only switch $B$ will receive the information, not the other intermediate switches along the path from $A$ to $B$. An additional restriction due to the operation mode of the switches is that, at any given time, any switch can be part of at most one optical path. Thus, at each moment in time, the optical paths established for the information transmission must be disjoint in terms of the switches that are part of them. The transmission time of a broadcast strategy is the maximum time at which one of the switches receives the information. Determine a broadcast strategy with minimal transmission time.

## Input data

The input file `optic.in` contains, in the first line, the natural number $N$, representing the number of switches in the network. The next $N-1$ lines contain two distinct natural numbers $A$ and $B$ with the meaning that there is a direct connection oriented from $A$ to $B$.

## Output data

The output file `optic.out` will contain, on the first line, the minimal transmission time $T$. Subsequently, for each moment in time $M$ from $0$ to $T-1$, it will contain a natural number $C$, representing the number of optical paths established at moment $M$, followed by $C$ lines containing $2$ natural numbers separated by a space, $A$ and $B$, with the meaning that an optical path from switch $A$ to switch $B$ was established at moment $M$ for the transmission of information.

## Constraints and clarifications

1 $\leq$ $N$ $\leq$ $333$

## Example

`optic.in`
```
6
1 2
1 3
3 4
4 5
5 6
```

`optic.out`
```
3
1
1 3
2
1 2
3 5
2
3 4
5 6
```