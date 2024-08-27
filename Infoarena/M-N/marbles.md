Marbles

Gigel has $N$ colored marbles that he places on the $Ox$ axis of a Cartesian coordinate system. He performs the following operations on them: $0$ $i$ $j$ represents an operation to move the marble located at coordinate $i$ to coordinate $i+j$. It is guaranteed that there is no other marble between coordinates $i$ and $i+j$. $1$ $i$ $j$ represents a query operation. Thus, Gigel wonders what is the maximum number of marbles of the same color that are between coordinates $i$ and $j$ inclusive. 

## Task

Help Gigel by providing the answers for the query operations. 

## Input data

The input file `marbles.in` contains numbers $N$ and $M$ on the first line, the number of marbles, and the number of operations performed, respectively. The next $N$ lines contain two integers $a_i$ $b_i$ representing the coordinate where marble $i$ is initially located, and its color, respectively. Then follows $M$ lines, each describing an operation performed by Gigel. 

## Output data

The output file `marbles.out` will contain the answer for each query operation. 

## Constraints and clarifications

$1 \leq N \leq 100 \ 000$  
$1 \leq M \leq 100 \ 000$  
The color of a marble will be a natural number in the range $[1, 64]$  
The coordinates of the marbles at any point in time, as well as all numbers in the input file, will be signed 32-bit integers.  
There will not be $2$ marbles at the same coordinate 

## Example

`marbles.in`
```
5 3
1 1
4 1
5 2
11 1
15 3
1 4 13
0 4 -1
1 4 13
```

`marbles.out`
```
2
1
```

## Explanation

Initially, between coordinates $4$ and $13$ there are two marbles that are colored with $1$. After moving the marble from position $4$ to position $4 - 1 = 3$, between coordinates $4$ and $13$ there remain only two marbles, both being colored differently.