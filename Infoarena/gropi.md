# Potholes

Due to the excellent results he achieved at the Balkan Junior Olympiad 5 years ago, Danut receives a new car (not a toy) from his parents when he turns 18. Eager to test it, he decides to take various routes through the city. Danut's city can be considered, for simplicity, as a 2-row matrix with $C$ columns, where each area of the city corresponds to a cell in the matrix. Such an area is identified by its coordinates: the row number and the column number it is in. Since the city is under development, it is currently full of potholes. Danut knows in advance which areas of the city are good and which are full of potholes. He does not want to damage his car and therefore will never pass through an area with potholes. Danut plans to take $M$ routes between known areas of the city and wonders, for each of these $M$ planned routes, what is the minimum time it can be completed in, such that areas with potholes are avoided. It is known that traveling through a pothole-free area of the city takes exactly 1 minute (Danut drives at a constant speed of 50 km/h).

## Input data

The input file `gropi.in` contains on the first line two natural numbers, $C$, which represents the number of columns in the schematic representation of the city, and $N$, the number of areas in the city that have potholes and must be avoided. Each of the next $N$ lines contains a pair of natural numbers $(x, y)$, $1 \leq x \leq 2$, $1 \leq y \leq C$, which represent the coordinates of an area with potholes. The next line contains the number $M$, the number of routes Danut takes. The file then contains $M$ lines, each with four natural numbers, $(x_1, y_1, x_2, y_2)$, $1 \leq x_1, x_2 \leq 2$, $1 \leq y_1, y_2 \leq C$, meaning that Danut wants to start driving from the area of coordinates $(x_1, y_1)$ and arrive at the area of coordinates $(x_2, y_2)$.

## Output data

The output file `gropi.out` will contain exactly $M$ natural numbers. Each line contains the minimum duration of the corresponding route from the input file.

## Constraints and clarifications

$1 \leq N \leq \min(100000, 2 \cdot C)$

$1 \leq M \leq 100000$ 

$2 \leq C \leq 2000000000$ 

For 50% of the tests, $C \leq 250$ and $M \leq 200$ 

The $N$ areas containing potholes are distinct from each other

It is guaranteed that it is possible to reach from any area to any other without passing through areas with potholes

The start and destination points for each route are not areas with potholes

## Example

`gropi.in`

```
10
4
1 3
2 9
1 7
1 5
3
1 1 1 6
1 9 2 1
1 1 1 10
```

`gropi.out`

```
8
10
12
```

## Explanation

For the first route of the two, a possible solution is shown in the drawing below. The black areas are those containing potholes and cannot be driven through. Since 8 areas (8 cells) are covered, the route takes a total of 8 minutes.