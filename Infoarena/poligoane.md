# Polygons

Mitruţ has $N$ sticks of equal lengths and doesn't really know what to do with them. You give him the idea to form convex polygons out of them, and now he's asking you how many ways he can group them. Mitruţ advises you to look at the example to better understand what he is asking for.

## Task

You are given $T$ tests. For each test, you need to display the number of ways the sticks can be grouped to form regular convex polygons modulo a given number.

## Input data

The input file `poligoane.in` contains the number $T$ in the first line. Each of the following $T$ lines contains two numbers $N_i$ and $MOD_i$.

## Output data

The output file `poligoane.out` contains $T$ lines. Line $i$ will contain the required number for $N_i$ modulo $MOD_i$.

## Constraints

$1 \leq T \leq 10$  
$3 \leq N_i \leq 2\ 000$  
$1 \leq MOD_i \leq 1\ 000\ 000$  
For $20\%$ of the tests, $N_i \leq 80$  
For another $40\%$ of the tests, $N_i \leq 1\ 000$

## Example

`poligoane.in`  
7  
3 7  
6 13  
4 17  
11 23  
12 19  
13 31  
799 666013  

`poligoane.out`  
1  
2  
1  
6  
9  
10  
29846  

## Explanation

From $3$ sticks, a single convex polygon can be formed: a triangle. For $6$ sticks, there are two options: a hexagon or two triangles. From $4$ sticks, only a square can be formed. For $11$ sticks, the grouping options are as follows: $11$, $8 + 3$, $7 + 4$, $6 + 5$, $4 + 4 + 3$, $5 + 3 + 3$, meaning we can either form a polygon with $11$ sides, an octagon and a triangle, a hexagon and a pentagon, etc.