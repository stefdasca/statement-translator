# NASA plans a new Rover mission to Mars in 2020. The main objective of this mission is to determine, with the help of a new Rover, if life existed on Mars in the past. Until the mission is launched, the Rover is subjected to various tests in NASA laboratories. In one of these tests, the Rover has to traverse a surface shaped like a grid with $N$ rows and $N$ columns. It starts from the area with coordinates $(1,1)$ and has to reach the area with coordinates $(N,N)$, being able to move at each step from the current area to one of the neighboring areas to the north, south, east, or west. For each area with coordinates $(i,j)$ the stability of the terrain in that area, $A_{ij}$, is known. Knowing that the Rover has a weight $G$, an area with terrain stability at least equal to $G$ is considered a safe area for the Rover to move through, while an area with terrain stability less than $G$ is considered a dangerous area for the Rover.

# Task

1. Determine the minimum possible number of dangerous areas that the Rover has to traverse to get from area $(1,1)$ to area $(N,N)$.
2. Determine the maximum weight a Rover can have to get from area $(1,1)$ to area $(N,N)$ without traversing any dangerous areas for it.

# Input data

The input file `rover.in` contains: 

The first line contains the natural number $V$, which can only be $1$ or $2$. If $V$ is $1$, the second line of the input file contains two natural numbers $N$ and $G$ with the given meaning, and if $V$ is $2$, the second line of the input file contains only the number $N$.
The next $N$ lines contain $N$ numbers $A_{i,j}$, representing the stability of the terrain in the area $(i,j)$. 

# Output data

The output file is `rover.out`.

If the value of $V$ is $1$, then the output file will contain on the first line a natural number representing the minimum number of dangerous areas that a Rover of weight $G$ has to traverse.

If the value of $V$ is $2$, then the output file will contain on the first line a natural number representing the maximum weight of a Rover that can get from area $(1,1)$ to area $(N,N)$ without traversing any dangerous areas for it.

# Constraints and clarifications

* $1 \\leq N \\leq 500$
* $1 \\leq G \\leq 5 \ 000$
* $1 \\leq A_{ij} \\leq 10 \ 000$
* Areas with coordinates $(1,1)$ and $(N,N)$ are not dangerous areas for the Rover.
* The Rover will not pass through the same area multiple times.

| $V$ | Points |
| - | ------- |
| $1$ | 45      |
| $2$ | 45      |

# Example 1

`rover.in`
```
1
5 5
5 1 3 4 7
5 2 1 8 5
2 9 5 3 3
4 1 1 1 9
5 1 6 1 8
```

`rover.out`
```
3
```

## Explanation

The minimum number of dangerous areas traversed from position $(1,1)$ to position $(5,5)$ is $3$.

A possible route is:

~[turnuri_1.png]

# Example 2

`rover.in`
```
2
5
5 1 3 4 7
5 2 1 8 5
2 9 5 3 3
4 1 1 1 9
5 1 6 1 8
```

`rover.out`
```
2
```

## Explanation

The maximum weight of a Rover that can get from area $(1,1)$ to area $(5,5)$ without passing through dangerous areas for it is $2$.

A possible route is:

~[turnuri_2.png]

