# Sea2

There will be a great battle at sea between $N$ ships. The ships are considered as points and are given by their Cartesian coordinates $x$ and $y$. For reasons hard to understand, ships can only attack ships that are to the left and below (more precisely, a ship at position $x_1, y_1$ can attack another ship at position $x_2, y_2$ if and only if $x_1 > x_2$ and $y_1 > y_2$). Because this battle is taking place in the Bermuda Triangle area, the ships appear (teleport) one by one into the battle zone. The ships are numbered $1, 2, \dots, N$ in the order of their appearance. When a ship appears, if there is another ship that appeared already and can attack the new ship, the new ship is destroyed instantly. If not, the new ship remains at sea and destroys all the ships it can attack.

## Task

Given the coordinates where the ships appear one by one, determine for each ship if it is destroyed at the moment of its appearance and if it is not destroyed, state the total number of ships left at sea after its appearance.

## Input data

The first line of the input file `sea2.in` contains the natural number $N$ representing the number of ships that will appear at sea. Each of the following $N$ lines contains a pair of integers separated by a space, representing the coordinates $x$ and $y$ of the ship corresponding to that line (more precisely, on line $i$ are written the coordinates of the ship $i-1$, for any $i$ from $2$ to $N+1$).

## Output data

The output file `sea2.out` will contain $N$ lines, each line with an integer. Line $i$ will contain $-1$ if the ship $i$ is destroyed at the moment of its appearance, or a strictly positive integer representing the number of ships at sea after the appearance of ship $i$ otherwise.

## Constraints

$1 \leq N \leq 200000$  
The coordinates are strictly positive integers less than or equal to 260000  
There will be no two ships with the same $x$ coordinate or the same $y$ coordinate

## Example

`sea2.in`
```
5
4 1
8 6
7 5
3 4
9 3
```

`sea2.out`
```
1
1
-1
-1
2
```

## Explanation

Ship $1$ remains at sea  
Ship $2$ remains at sea and destroys ship $1$  
Ship $3$ is destroyed by ship $2$  
Ship $4$ is destroyed by ship $2$  
Ship $5$ remains at sea, along with ship $2$