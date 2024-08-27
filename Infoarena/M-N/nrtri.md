# Counting Triangles

Andrei has $N$ sticks of not necessarily different lengths. He wants to find out in how many ways he can choose three sticks so that they can form a triangle.

## Task

Given the lengths of the sticks, find out in how many ways three of them can be chosen such that a triangle can be formed with them. 

## Input data

The first line of the file `nrtri.in` contains $N$, the number of sticks. The next line contains $N$ numbers separated by spaces representing the lengths of the sticks. 

## Output data

The file `nrtri.out` contains a single number that represents the required number of ways. 

## Constraints

$1 \leq N \leq 800$ 

$1 \leq \text{length of a stick} \leq 30000$

Triangles are considered even if they have an angle of $180$ degrees and the other two angles are $0$ degrees ( $2$ collinear segments coincide with the $3^{rd}$ )

For $75$ points it is guaranteed 

$1 \leq N \leq 150$

## Example

`nrtri.in`
```
4
2 3 7 4
```

`nrtri.out`
```
2
```

## Explanation

The only triangles that can be formed are made up of the following sticks (given by their order numbers): $1, 2, 4$ and $2, 3, 4$