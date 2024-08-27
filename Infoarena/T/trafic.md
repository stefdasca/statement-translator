# Traffic

After dividing the country into counties, the monkeys face another problem; they need to stop the banana traffic. The monkeys' country has $N$ cities numbered from $1$ to $N$ connected by $M$ bidirectional roads. Between any two cities, there is at most one road, but there are paths - direct or through intermediate cities. Cities $1$ and $N$ are capitals. Recently, the traffic of bananas between the two capitals has intensified. To combat the traffic, the president has $G$ soldiers at his disposal, who can be placed anywhere on a road, as close to a city as desired, but not in the city. In the event of an attack on one of the capitals, all soldiers must reach that capital. The soldiers move at a constant speed. The time required for such a mobilization is equal to the maximum distance from the soldiers to one of the capitals.

## Task

Write a program to find a placement of the soldiers such that any route from one capital to the other passes through a road with at least one soldier, and the mobilization time in the worst case is minimized.

## Input data

The first line of the input file `trafic.in` contains three numbers $N$ $M$ $G$ separated by a single space. The next $M$ lines each contain three numbers separated by spaces $a$ $b$ $c$ with the meaning "there is a bidirectional road from city $a$ to city $b$ of length $c$".

## Output data

The first line of the output file `trafic.out` will contain the minimum mobilization time with one exact decimal point. If there is no solution, it will print $-1$.

## Constraints

$3 \leq N \leq 154$

$3 \leq M \leq 5054$

$1 \leq$ length of a road $\leq 1023$

$3 \leq G \leq 4095$

## Example

`trafic.in`
```
6 6 2
1 2 1
2 3 2
3 6 1
1 4 1
4 5 3
5 6 1
```

`trafic.out`
```
2.5
```

## Explanation

A soldier is placed in the middle of the road between $4$ and $5$, and another soldier is placed on the road between $2$ and $3$ at $0.5$ distance from city $2$.