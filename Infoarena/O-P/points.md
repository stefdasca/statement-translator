# Points

Given $n$ points in a plane, determine the number of ways to choose three of these points such that the area of the triangle determined by them is an integer.

## Input data

The input file `points.in` contains on the first line the number $n$ of points in the plane. Each of the next $n$ lines contains two numbers, separated by spaces, representing the coordinates of a point.

## Output data

The output file `points.out` will contain a single line which will contain the number of ways to choose three points such that the area of the triangle determined by them is an integer.

## Constraints and clarifications

$3 \leq n \leq 10\ 000$  
The coordinates of the points are integers between $0$ and $1\ 000$  
The area of the triangle determined by three collinear points is considered to be $0$  
No two points have the same coordinates.

## Example

`points.in`  
`4`  
`0 0`  
`0 2`  
`2 2`  
`2 0`  

`points.out`  
`4`