# Polygon

After a crazy night full of crimes, a police officer is working on compiling some statistics. He has a map of the city with the points where the crimes occurred as well as an area in the shape of a polygon (not necessarily convex) on the map that is of maximum interest.

## Task

Given the polygon that describes the area of interest and the points of crime, you must find out the number of crimes that occurred in that area.

## Input data

In the input file `polygon.in`, the first line contains the integers $N$ and $M$ separated by a space, where $N$ is the number of vertices of the polygonal area and $M$ is the total number of crimes that occurred last night. The next $N$ lines contain two integers each representing the coordinates of the vertices of the polygon given in the order of traversal of its sides in either one of the two possible directions. The next $M$ lines contain the coordinates of the crimes that occurred the previous night.

## Output data

In the output file `polygon.out`, the first line contains the number of points that are inside or on the edge of the given area. The line ends with the "end of line" character.

## Constraints and clarifications

$3 \leq N \leq 800$ 

$1 \leq M \leq 60\,000$ 

The coordinates of the points will be integers between $0$ and $60\,000$ 

The polygon does not self-intersect

## Example

`polygon.in`  
`4 3`  
`0 0`  
`0 100`  
`100 100`  
`100 0`  
`50 50`  
`100 50`  
`100 110`  

`polygon.out`  
`2`