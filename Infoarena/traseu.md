# Route

Gigel has moved to a new city! To get familiar with the new surroundings, he bought the city's map and noticed that it consists of $M$ one-way streets of different lengths and $N$ street intersections. Gigel took the map and started to plan a route that starts from a specific intersection, goes through each street at least once, and returns to the intersection from which it started. Although his desire to explore is high, his physical condition is not so good, so he wants to find a route where the sum of the lengths of the streets traveled is minimal.

## Task

Write a program that finds a route with the minimum length in Gigel's city.

## Input data

The first line of the file `route.in` contains the numbers $N$ and $M$ separated by a space. The next $M$ lines contain triplets of numbers $i$ $j$ $k$ with the meaning that there is a street from intersection number $i$ to intersection number $j$ of length $k$.

## Output data

The first line of the file `route.out` will contain a single natural number representing the minimum length of Gigel's route.

## Constraints and clarifications

$1 \leq N \leq 60$

The lengths of the streets are natural numbers in the interval $[1, 10\ 000]$

If there is a street between two intersections $i$ and $j$, then there will certainly not be a street between the intersections $j$ and $i$

It is guaranteed that there is at least one route in the city that goes through each street at least once and starts and ends at the same intersection

## Example

`route.in`
```
6 8
1 2 3
2 3 1
3 1 2
1 4 4
4 6 2
6 1 5
4 5 1
5 1 6
```
`route.out`
```
28
```

## Explanation

The chosen route is: $(1, 2, 3, 1, 4, 6, 1, 4, 5, 1)$.