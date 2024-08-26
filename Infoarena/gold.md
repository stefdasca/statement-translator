## Task

Determine in how many ways the two mines can be set such that the division is fair.

## Input data 
The first line of the file `gold.in` contains $N$, the number of mines. 
The second line contains the value $P$, with the meaning from the statement. 
The 3rd line will contain $N$ positive natural numbers, the $i$-th number representing the amount of gold from the $i$-th mine. 
Starting from the 4th line, the positions of the mines will be described with reference to an orthogonal coordinate system: each line will contain a pair of integers $(x, y)$, more precisely on line $i+3$ the coordinates for the $i$-th mine will be provided.

## Output data 
The first line of the file `gold.out` contains the number of different ways to choose two mines among the $N$ so that the division is fair.

## Constraints and clarifications
$4 \leq N \leq 1\ 024$
$0 \leq P \leq 98\ 765$
The amounts of gold in the mines are natural numbers in the range $[1, 10\ 000]$
The coordinates of the mines are integers in the range $[-16\ 000, 16\ 000]$
Any three mines are non-collinear 

## Example

`gold.in`
```
7
5
4 7 8 6 4 6 7
3 10
2 3
8 1
10 4
7 1
7 3
9 8
```

`gold.out`
```
3
```