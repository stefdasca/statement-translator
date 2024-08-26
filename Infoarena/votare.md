# Voting

On the planet Mars, elections are being held today. The Martians are scattered across the surface of the planet, with their positions specified by the Cartesian coordinates of the point on the map where they are located. Various events occur from time to time: a Martian disappears (goes to vote), a Martian appears (returns from voting) or a Martian wonders how far the nearest Martian is (to ask if they have voted yet).

## Task

Given the sequence of events, the answers to the Martians' questions must be determined.

## Input data

The input file votare.in contains the natural number $N$ on the first line, representing the number of events. The next $N$ lines contain events, one event per line, in the order in which they occur. An event is described by 3 integers separated by spaces as follows:
Event Meaning 
$0$ $x$ $y$ a Martian appears in position with coordinates $(x,y)$
$1$ $x$ $y$ the Martian disappears from position with coordinates $(x,y)$
$2$ $x$ $y$ the Martian in the position with coordinates $(x,y)$ asks what the distance is to the nearest Martian

## Output data

The output file votare.out will contain the answers to the Martians' questions (events of the form $2$ $x$ $y$), one answer per line, in order.

## Constraints and clarifications

$1 \leq N \leq 100000$

All coordinates in the input file are non-zero integers in the range $[-32000, +32000]$

Two Martians cannot be in the same position simultaneously

The distance between $2$ points $(x_0,y_0)$ and $(x_1,y_1)$ is defined as $(x_0-x_1)*(x_0-x_1)+(y_0-y_1)*(y_0-y_1)$

If no Martian exists, the answer $-1$ will be printed

The points given in queries are not inserted into the set of points

A point given in a query may be present in the set of points, in which case the minimum distance will be $0$

A point already present can be queried for insertion or an inexistent point can be queried for deletion, in this case nothing will happen

## Example

`votare.in`
```
9 
0 5 6 
0 7 9 
0 12 9 
2 1 1 
0 5 3 
0 1 4 
2 2 4 
1 5 6 
2 1 1
```

`votare.out`
```
41 
1 
9 
```