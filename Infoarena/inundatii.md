## Task

This year, it is very likely that floods will occur in Zaharel's town. Zaharel needs to come up with a plan to protect the $N$ buildings in his town from floods. To simplify the problem, we will consider a building as a point in space. Additionally, the buildings in Zaharel's town have some interesting properties:
- they are numbered with distinct numbers between 1 and $N$
- their coordinates are integers
- building number $i$ dominates building number $i+1$ for any $1 \leq i < N$; formally, this means that $X_i > X_{i+1}$, $Y_i > Y_{i+1}$, and $Z_i > Z_{i+1}$, where $$(X_i, Y_i, Z_i)$$ represents the position of building number $i$

After a long analysis, Zaharel concluded that the safest way to avoid floods is to move the buildings so that building $i$ dominates building $i-1$ for any $1 < i \leq N$. Of course, moving a building is no easy task, so Zaharel wants to minimize the sum of the distances each building is moved.

## Input Data

The input file `inundatii.in` contains:
- The first line contains the number $N$
- The next $N$ lines each contain 3 integers $X_i$ $Y_i$ $Z_i$ separated by spaces, representing the positions of the buildings.

## Output Data

The output file `inundatii.out` will contain a single natural number, representing the sum of the distances each building is moved in the most favorable case.

## Constraints and Clarifications

$1 \leq N \leq 50000$  
$0 \leq X_i, Y_i, Z_i \leq 10^8$  
The coordinates to which the buildings are moved must be integers  
The distance between two points $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$ is considered to be $|x_1 - x_2| + |y_1 - y_2| + |z_1 - z_2|$  

## Example

`inundatii.in`
```
2
8 5 10
5 4 7
```

`inundatii.out`
```
10
```

## Explanation

One possible solution is: 
Move the first building from $(8, 5, 10)$ to $(6, 4, 8)$, the distance being $|8-6| + |5-4| + |10-8| = 2 + 1 + 2 = 5$. 
Move the second building from $(5, 4, 7)$ to $(7, 5, 9)$, the distance being $|5-7| + |4-5| + |7-9| = 2 + 1 + 1 = 5$. 
The sum of distances is $10$, and the solution is valid because the second building dominates the first building ($7 > 6$, $5 > 4$, $9 > 8$).