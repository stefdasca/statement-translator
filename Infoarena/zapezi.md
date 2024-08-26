# Snow

Snow has once again surprised the city hall. The mayor urgently called the snow removal service and provided a list of streets in the city that must be obligatorily cleared. The mayor selected the streets in the list so that their number is as small as possible, but still, there is a connection between any two intersections in the city. The snow removal service employs two workers, Vasilica and Ionica, with two machines. At this moment, both the workers and the machines are at the headquarters of the snow removal service, located at one of the city intersections. A snow removal machine consumes 1 liter of gasoline per 1 meter (regardless of whether it moves on a snow-covered or cleared street). Vasilica and Ionica have to clear all the streets from the list given by the mayor so that the total amount of gasoline consumed is minimal. When all the streets from the list given by the mayor are cleared, the machines can be parked in the last visited intersection. Obviously, Ionica and Vasilica do not have to park their machines in the same intersection. Write a program that determines the minimum amount of gasoline needed to clear all the streets from the list given by the mayor.

## Input data

The input file `zapezi.in` contains:
- The first line contains two natural numbers $N$ and $S$, where $N$ is the number of intersections in the city, and $S$ is the number of the intersection where the snow removal service headquarters is located, from which Vasilica and Ionica initially depart (the intersections are numbered from $1$ to $N$)
- Each of the next $N-1$ lines contains 3 natural numbers $A$, $B$, $C$ with the meaning "intersections $A$ and $B$ are directly connected by a street of length $C$ meters".

## Output data

The output file `zapezi.out` contains on the first line the minimum amount of gasoline needed to clear all the streets from the list given by the mayor.

## Constraints

$1 \leq N \leq 10\ 000$

$1 \leq S, A, B \leq N$

$1 \leq C \leq 1\ 000$

## Example

`zapezi.in`
```
5 2
1 2 1
2 3 2
3 4 2
4 5 1
```

`zapezi.out`
```
6
```

`zapezi.in`
```
5 1
1 2 1
2 3 1
3 5 1
3 4 1
```

`zapezi.out`
```
5
```

`zapezi.in`
```
4 4
1 3 2
1 2 3
1 4 4
```

`zapezi.out`
```
11
```