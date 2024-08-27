## Task

Miruna inherited from her aunt Tamara an orchard that can be represented as a matrix with $N$ rows and $M$ columns. The orchard is located at the base of a mountain inhabited by $K$ marmots. Since winter has arrived, it is time for the marmots to descend to lower altitudes to shelter from the cold. Each day, a marmot arrives at Miruna's orchard and wants to build a burrow. Each marmot selects a point with coordinates $X_i$ and $Y_i$. Its burrow will consist of all field positions found at a Manhattan distance less than or equal to a given number $L$ from the position $(X_i, Y_i)$. If there is at least one position in the burrow that is already part of a previously built burrow, the marmot will refuse to settle in Miruna's orchard and will leave into the world.

## Input data

The input file `marmote.in` will contain on the first line 4 integers $N$, $M$, $K$, and $L$ having the meanings described in the statement. The next $K$ lines will contain two integers each $X_i$ and $Y_i$, the values associated with the marmot with index $i$.

## Output data

In the output file `marmote.out` you will print in ascending order the indices of the marmots that will build their burrow in Miruna's orchard. These values will be printed one per line.

## Constraints

$1 \leq N \leq 1000$  
$1 \leq M \leq 1000$  
$1 \leq K \leq 100000$  
$1 \leq L \leq \min(N, M)$  
$1 \leq X_i \leq N$  
$1 \leq Y_i \leq M$  

The Manhattan distance between two points $(X_1, Y_1)$ and $(X_2, Y_2)$ is equal to $|X_1 - X_2| + |Y_1 - Y_2|$ 

## Example

`marmote.in`  
```
10 12 6 3
3 6
5 9
7 1
9 4
4 11
2 10
```

`marmote.out`  
```
1
4
5
6
```