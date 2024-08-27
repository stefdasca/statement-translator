## KCity

In the city of KCity, there are $N$ intersections, numbered from 1 to $N$, interconnected by $M$ bidirectional streets (each street connects 2 different intersections). In recent months, crime has increased significantly in the city, so the police chief wants to determine some routes for police patrol cars to keep citizens safe. According to the police chief, each route should be in the form $x_1, x_2, \dots, x_P$ ($P \geq 1$), where $x_i$ are the numbers of some intersections and between any two consecutive intersections on the route, $x_i$ and $x_{i+1}$, there is a street. To avoid redundancies (which, in the opinion of the police chief, would increase costs too much), a route must not contain an intersection more than once. In addition, each intersection must appear in exactly one route (if there were an intersection that did not belong to any route, the crime rate in that area would increase significantly). The police chief's assistant, however, has a different opinion. He believes that each route should be in the form $x_1, x_2, \dots, x_P$ ($P \geq 4$), where $x_i$ are the numbers of some intersections, $x_1 = x_P$ and between any two consecutive intersections on the route, $x_i$ and $x_{i+1}$, there is a street. However, he also agrees that each intersection must belong to exactly one route, and a route must not contain an intersection more than once (except for the first intersection on the route, which will also be the last). Since the police department does not have too many people available, the aim is to determine the minimum number of routes to send police patrols in each case (according to the definition of a route by the police chief and according to the definition by the assistant). It is also known that the name of the city ($KCity$) was not chosen randomly, it comes from a condition known only to officials, that if there is a street between intersections $A$ and $B$, then $|A-B| \leq K$.

## Input data

The first line of the input file `kcity.in` contains 4 integers, separated by a space: $N$, $K$, $X$, and $M$. Each of the next $M$ lines contains 2 integers, separated by a space, $A$ and $B$, meaning there is a street between intersection $A$ and intersection $B$. If $X=1$, then the task is to determine the minimum number of routes corresponding to the police chief's opinion; if $X=2$, the task is to determine the minimum number of routes corresponding to the assistant's opinion.

## Output data

The output file `kcity.out` will contain the integer $T$, representing the minimum number of routes that respect the police chief's opinion (if $X=1$), or the minimum number of routes that respect the assistant's opinion (if $X=2$). If it is not possible to establish routes that meet the conditions specified in the statement, print $-1$.

## Constraints and clarifications

$1 \leq N \leq 1000$

$1 \leq K \leq 6$

$0 \leq M \leq 6000$

There will not be more than one street between the same pair of intersections.

In 50% of the tests, $X=1$ (obviously, in the remaining 50% of the tests, $X=2$).

## Examples

`kcity.in`
```
9 3 1 10
1 4
2 4
1 2
3 6
6 9
9 7
7 8
8 5
5 3
4 7
```

`kcity.out`
```
1
```

`kcity.in`
```
9 3 2 10
1 4
2 4
1 2
3 6
6 9
9 7
7 8
8 5
5 3
4 7
```

`kcity.out`
```
2
```