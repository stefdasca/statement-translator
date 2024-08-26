## Task

You have entered a directed graph $G$ with weighted edges by car. The weight of an edge denotes its length in kilometers. Currently, you are at node $1$ and want to reach node $N$ as fast as possible. Your car has a maximum speed equal to $V_{max}$ km/h. There is a speed limit in the graph, equal to $LIMIT$ km/h. 

To check compliance with this limit, the graph administrators have placed special traffic cameras in $K$ out of the $N$ nodes. They operate as follows:
- For each node containing a camera, the camera will record all cars entering or leaving that node and note the time of these events.
- If a car passes through multiple nodes with cameras, say, in order, $n_1$, $n_2 \dots n_k$, then the system can check for each pair $n_i$, $n_{i+1}$ if the car has exceeded the speed limit on the road segment from $n_i$ to $n_{i+1}$.

If a car reaches node $n_{i+1}$ from node $n_i$ in a time shorter than the time it would take to travel from $n_i$ to $n_{i+1}$ on the shortest path and at the speed of $LIMIT$, then the system realizes that the car has exceeded the speed limit. Note that it is not necessary for the special nodes in this sequence to be the only nodes on the path traveled by the car. There can be any number of nodes without a camera on the road segment between $n_i$ and $n_{i+1}$.

You are asked to find the minimum time in which you can travel from node $1$ to node $N$ without being caught by the system for violating the speed limit.

## Input data

The first line of the input file contains the numbers $N$, $M$, and $K$, representing the number of nodes, the number of edges in the graph, and the number of cities with a camera. 

The second line of the input file contains the $K$ cities in which there is a camera. 

The next line contains the values $V_{max}$ and $LIMIT$. 

The following $M$ lines each contain an edge in the form $from \;to \; length$, meaning there is a unidirectional edge from node $from$ to node $to$ with a length of $length$ km.

## Output data

The single line of the output file must contain the minimum time in which the car can reach node $1$ to node $N$ without the system noticing that the speed limit has been exceeded.

## Constraints and clarifications

$2 \leq N \leq 100\,000$

$1 \leq M \leq 250\,000$

$1 \leq K \leq N$

$1 \leq V_{max}$, $LIMIT$, $length \leq 30\,000$, where $length$ represents the length of an edge. All these values are integers. 

It is guaranteed that there is at least one path from node $1$ to node $N$. 

The answer can differ from the real one by at most $10^{-9}$

## Example

`cameras.in` 
```
4 7 3
2 3 4
10 5
1 2 1
2 4 5
4 1 1
3 2 9
2 3 3
4 3 10
3 4 4
```

`cameras.out` 
```
1.100000
```