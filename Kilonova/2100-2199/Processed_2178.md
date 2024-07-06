A candidate for the presidency of a major world state has entered the election campaign. To obtain as many votes as possible, the campaign team wants the time without electoral activity to be as minimal as possible. This time is measured by the distance traveled by plane between cities and by traveling within cities on roads without voters. All the cities chosen for the campaign have the same architectural structure, meaning that each contains two airports labeled $AS$ and $AP$, with $AS$ only for arrivals, and $AP$ only for departures. The streets of each city are parallel, and two consecutive parallel streets are connected by roads without voters, with intersections at the connection points. Any two intersections on consecutive parallel streets are connected by a straight road. All streets have houses and thus voters. $AS$ is on the first street, in the farthest bottom left point, and $AP$ is on the last street, the farthest right of the city.

An example of the architectural structure for a city is shown below.

~[campanie.png]

The campaign team has at its disposal a map with the coordinates of the airports of $N$ cities and $N$ maps, one for each city, with the coordinates of the intersections on each street. The coordinate system for each city has its origin at the arrival airport $AS$, the streets being parallel to the ordinate axis, and the departure airport $AP$ is located on the last street (the farthest to the right). The ordinate axis is the first street (the farthest left street).
The campaign starts at an arrival airport of a city and ends at the same airport. The candidate must necessarily pass through all airports.

# Task
Determine the minimum time without electoral activity in the presidential campaign.

# Input data

The input file `campanie.in` will have the following structure:

* The first line contains $N$, the number of cities
* The following lines contain the data for the architectural structure of each city: one line with the coordinates of the airports $x_{AS} \\ y_{AS} \\ x_{AP} \\ y_{AP}$, separated by a space, one line with the number $k$ of streets followed by $k-1$ numbers with the distances between two consecutive streets, separated by a space from left to right, then $k$ lines with the positions of the intersections on each street in the format: $h \\ y_1 \\ y_2 \\dots \\ y_h$, where $y_1 \\ y_2 \\dots \\ y_h$ are the ordinates of the intersections.

# Output data

The output file `campanie.out` will contain a single natural number representing the minimum time without electoral activity in the presidential campaign.

# Constraints and clarifications

* $N$ is a natural number such that $2 \\leq N \\leq 18$
* The distance traveled between two cities or two intersections with coordinates $(x_1, y_1)$ and $(x_2, y_2)$ is defined as $(x_1 - x_2)^2 + (y_1 - y_2)^2$.
* The number of streets in a city $\\leq 1 \\ 000$.
* The number of intersections on a street $\\leq 1 \\ 000$.
* The distances between two consecutive streets of the same city $\\leq 1 \\ 000$.
* All ordinates of the intersections in a city and those of the departure airport are $\\leq 10 \\ 000$.
* The coordinates on the city map are integers in the interval $[-10 \\ 000, 10 \\ 000]$.

# Example

`campanie.in`
```
3
100 0 30 0
3 10 20
2 0 20
2 10 20
3 10 30 0
0 0 10 0
2 100
1 0
2 0 10
200 0 300 0
2 100
1 0
1 0
```

`campanie.out`
```
97500
```

## Explanation

The order of the cities in which the candidate will arrive is $1, 2, 3$. In city $1$ the time without electoral activity will be $500$, in city $2$ it will be $10000$, and in city $3$ it will be $10000$.