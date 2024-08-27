Don Diego has just moved to a new city which is structured like a tree (a connected acyclic graph), where the $N$ intersections of the city are represented by nodes and the $N-1$ roads between intersections are represented by edges. Don Armando, upset with Don Diego, wants to flood one of the $N$ intersections, thereby splitting the city into several connected components (intersections that can be reached without passing through the flooded intersection). Don Armando wants to cause the most damage possible, ensuring that none of the remaining connected components contain more than $N/2$ intersections. Since you don't exactly know what to do today, you want to find out which intersections Don Armando can flood such that the above property holds.

## Input data

The input file `nustiu.in` contains on the first line the number of test cases $T$. The $T$ test cases follow. The first line of a test case contains $N$, the number of intersections in the city. The next $N-1$ lines contain two numbers $x$ and $y$, indicating that there is a road between intersections $x$ and $y$.

## Output data

The output file `nustiu.out` must contain, for each test, the intersections that Don Armando can flood such that he respects the above task, or the message `NIMIC`, if no such intersection exists. Within a test, the intersections must be printed each on a separate line in ascending order of their indices.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 10000$

$1 \leq x, y \leq N$

## Example

`nustiu.in`
```
2
6
1 3
3 2
3 4
4 5
4 6
12
1 2
2 3
2 4
4 5
5 6
5 7
1 8
8 9
8 10
8 11
10 12
```
`nustiu.out`
```
3
4
1
2
```

## Explanations

For the first test, intersections $3$ and $4$ can be flooded, and for the second test, intersections $1$ and $2$ can be flooded.