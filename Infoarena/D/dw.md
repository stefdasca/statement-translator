## Task

"People assume that time is a strict progression of cause to effect, but actually, from a nonlinear, non-subjective viewpoint, it's more like a big ball of wibbly-wobbly, timey-wimey $\dots$ stuff.." The Doctor has to save the universe$\dots$ again. With the help of the T.A.R.D.I.S., he can travel to various points in history which he can influence to save the present. As time has a complex structure, one way it can be represented is by a directed graph where nodes represent events, and edges are cause-effect relationships. For any event $i$, we denote its importance by $v_{i}$. Let $x_{1}, x_{2}, \dots, x_{k}$ be a sequence of events. The Doctor can influence this sequence if and only if the following conditions are met: for any $i$ $(1 \leq i \leq k-1)$, $v_{x_{i}} < v_{x_{i+1}}$, and in the time representation as a directed graph, there is a path from the node corresponding to $x_{i}$ to the node corresponding to $x_{i+1}$ (by the existence of a path from $a$ to $b$ we mean that one can get from $a$ to $b$ by only traversing graph edges and only in the corresponding direction). The Doctor needs to influence as many events as possible to save the universe, so he asks you to find the maximum length of a sequence of events that meets the above restrictions.

## Input data

The first line of the file `dw.in` will contain two natural numbers $N$ and $M$, representing the total number of events and the number of cause-effect relationships. The second line will contain $N$ natural numbers, the $i$-th of which represents the importance of the $i$-th event. Each of the following $M$ lines will contain two natural numbers, $x$ and $y$, meaning that there is a directed edge from the node corresponding to event $x$ to the node corresponding to event $y$ (events are indexed with natural numbers from 1 to $N$).

## Output data

The first line of the file `dw.out` will contain $K$, the maximum length of a valid sequence of events.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 200\ 000$

In all tests, the directed graph respects the following condition: for any 3 nodes $A$, $B$, $C$, if there is a path from $A$ to $C$ and from $B$ to $C$, then there is a path from $A$ to $B$, or from $B$ to $A$, or both.

In all tests, there is a node from which one can reach any other node.

for 10% of the tests $1 \leq N \leq 20$

for 40% of the tests $1 \leq N \leq 1000$, $1 \leq M \leq 2000$

for 60% of the tests the graph is acyclic

the above subtasks may overlap

the importance of an event is in the range $[1, 100\ 000]$

## Example

`dw.in`
```
5 8
1 3 1 4 2
1 2
2 3
3 4
4 2
4 3
4 5
3 5
1 5
```
`dw.out`
```
3
```

## Explanation

Nodes 1, 2, and 4 are chosen with respective values 1, 3, and 4.