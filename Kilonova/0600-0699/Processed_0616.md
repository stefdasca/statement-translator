In the morning of the Sperry’s training session 1 relay, after waking up on time, the champions naturally want to have the champions' breakfast. As we all know, the champions' breakfast is only taken at Profi.

The city of Slatina can be regarded as a tree with $N$ nodes, each node being a point of interest in the city, and where the points of interest are connected by bidirectional streets of equal lengths. As the city Slatina is continuously developing, in each of the following $Q$ days, one of the following events will take place:
* A Profi store will be built in the point of interest $u_i$. It is guaranteed that no Profi store was built in the point of interest $u_i$.
* The Profi store in the point of interest $u_i$ will be demolished. It is guaranteed that there was a Profi store built in the point of interest $u_i$. 

Since the champions are undecided about the location where they want to have breakfast, they want to meet at a point of interest that is at an equal distance from all Profi stores in the city. Initially, there are no Profi stores built in the city.

# Task

Help the champions have their breakfast! After each of the $Q$ days, calculate the number of locations where the champions can meet, while being at an equal distance from all Profi stores.

# Input data

The first line contains the numbers $N$ and $Q$. The following line contains $N$ numbers, the $i$-th representing the parent of node $i$. The following $Q$ lines each contain an integer $u_i$. If $u_i > 0$, a Profi store will be built in the point of interest $u_i$. If $u_i < 0$, the Profi store in the point of interest $-u_i$ will be demolished.

# Output data

There will be $Q$ lines. The $i$-th line will contain the number of points of interest where the champions can meet after day $i$, such that they are at an equal distance from all Profi stores.

# Constraints and clarifications
* $1 \leq N, Q \leq 200 \ 000$
* $0 \leq parent_i \leq N$
* The node with $parent_i = 0$ is the root of the tree.
* It is guaranteed that the array $parent$ describes a tree of size $N$.
* If there is no Profi store, the champions will meet at any point of interest.
* $-N \leq u_i \leq N$ and $u_i \neq 0$, $ \forall 1 \leq i \leq Q$.
* The distance between two points of interest is considered the number of edges between them.

## Subtask 1 (7 points)
* $1 \leq N, Q \leq 200$
## Subtask 2 (9 points)
* $1 \leq N, Q \leq 2 \ 000$
## Subtask 3 (20 points)
* $\sum_{i=1}^{Q} S_i \leq 1 \ 000 \ 000$, where $S_i$ is the number of Profi stores in the city on day $i$
## Subtask 4 (8 points)
* $u_i > 0$, $\forall 1 \leq i \leq Q$
## Subtask 5 (56 points)
* No further constraints

# Examples
`stdin`
```text
7 3
6 7 2 6 3 0 4
5
4
-5
```
`stdout`
```
7
1
7
```

`stdin`
```text
7 12
0 1 2 1 4 1 6
2
4
6
-4
5
-2
-6
3
7
-3
-5
1
```
`stdout`
```
7
3
1
3
0
0
7
3
1
3
7
1
```