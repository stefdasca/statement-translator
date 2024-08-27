Johnie

In a faraway country lived Johnie Walker, a character who loved walks very much. His country was organized into $N$ cities, and between certain pairs of cities, there were paths. Johnie has the desire to walk on every path in his country. Thus, he decided to take a grand walk in a number of stages. In each stage, Johnie starts from any city in the country, traverses a certain route, and stops in any city he wishes. A route is represented by a sequence of cities, such that between any $2$ consecutive cities in the sequence, there exists a path. In his walk, Johnie wishes to traverse each path only once. He does not mind if he passes through a city multiple times, even in the same route. Given the number of cities in the country and the paths between them, the task is to determine the minimum number of stages in which Johnie can traverse all the paths. Additionally, a way of traversing the paths in stages is also required.

## Input data

The first line of the file `johnie.in` contains the number $N$, representing the number of cities, and $M$, representing the number of paths. The next $M$ lines contain pairs $(i, j)$ that mark the existence of a path from city $i$ to city $j$.

## Output data

The first line of the file `johnie.out` must contain the minimum number of stages. The following lines contain, one per line, the routes Johnie travels in each stage. The first number on a certain line represents the number of cities traversed in that route, and the following numbers represent the cities traversed, in order.

## Constraints and clarifications

$1 \leq N \leq 50000$

$1 \leq M \leq 100000$

between two cities, there can be multiple paths

a path is bidirectional

there are no paths that start and end in the same city

## Example

`johnie.in`
```
7 7
1 2
1 3
1 4
2 3
3 5
4 5
6 7
```

`johnie.out`
```
2
7 1 4 5 3 2 1 3 2
6 7
```