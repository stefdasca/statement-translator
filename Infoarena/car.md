Car

Ionel has turned $18$ years old and he has received his driving license. Today, he wants to drive from his home to school by car, and the only condition his father imposed is not to take too many turns! To get the car another time, Ionel wants to impress his father by taking the least costly route in terms of turns. The city is represented by a matrix of $N$ rows and $M$ columns, with an element of the matrix being $0$ if the car can pass through it and $1$ if it cannot. The car can move from one cell of the matrix to all $8$ adjacent cells, if those cells are free. The cost of a route from the initial position to the final position is given by the sum of the movement costs. A move in the current direction costs $0$, a $45$ degree move from the current direction costs $1$, a $90$ degree move costs $2$, a $135$ degree move costs $3$, and a $180$ degree move costs $4$. Initially, the car can start in any of the $8$ directions, provided the respective cell in that direction is marked with $0$.

## Task

Determine for Ionel the minimum cost in terms of turns from an initial position to a final position.

## Input data

The first line of the input file `car.in` contains two natural numbers: $N$ (the number of rows of the matrix) and $M$ (the number of columns of the matrix). The next line contains the numbers $Si$ - the row of Ionel's initial car position, $Sj$ - the column of Ionel's initial car position, $Fi$ - the row of the final position, $Fj$ - the column of the final position. The next $N$ lines each contain $M$ numbers of $0$ or $1$.

## Output data

The first line of the output file `car.out` will contain the minimum cost of a route from the initial position to the final position. If no route exists, print $-1$.

## Constraints

$0 \leq N$,
$M \leq 500$

## Example

`car.in`
```
5 5
1 1 1 4
0 1 1 0 1
1 0 1 0 1
0 1 1 0 1
0 1 0 1 1
0 1 1 1 9
```

`car.out`
```
9
```