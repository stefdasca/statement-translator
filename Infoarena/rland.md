# Rland

Two good friends decided to buy plots of land in a neighborhood of the city where they live. The city is represented by an $N \times N$ square matrix, where each square of the matrix represents a unit area of the city. For each unit area of the city, its value, which is an integer between $-150$ and $150$, is known. The first of the two friends wants to buy a rectangular plot of land with $P$ rows and $Q$ columns, fully contained within the city, which has the maximum possible value. The value of the land is represented by the sum of the values of the unit areas it includes (numbering $P \cdot Q$). The second friend also wants to buy a rectangular plot of land, which must have exactly $Q$ columns (the same number of columns as the plot his friend wants to buy) and at most $P$ rows (meaning the number of rows of the land can be $1, 2, \dots, P$). Of course, he too wants his land to be fully contained within the city and to have the maximum possible value. The value of the land is given by the sum of the values of the unit areas it includes (numbering $L \cdot Q$, $1 \leq L \leq P$).

## Task

## Input data

The first line of the file `rland.in` will contain the numbers $N$, $P$, and $Q$ (separated by spaces). The next $N$ lines will contain $N$ integers (separated by spaces), representing the values of the unit areas that are part of the city.

## Output data

The first line of the file `rland.out` will contain the number $S$, representing the maximum value of the land the first friend wants to buy. The second line will contain the number $X$, representing the maximum value of the land the second friend wants to buy.

## Constraints and clarifications

$4 \leq N \leq 150$

## Example

`rland.in`
```
4 2 3 
-1 -1 -1 -1 
-1 1 -1 -1 
-1 -1 -1 4 
-1 -1 -1 -1 
```

`rland.out`
```
1 
2 
```

## Explanation

The first friend will buy the land that has its top-left corner at row 2 and column 2 (considering rows and columns numbered from $1$ to $N$). The second friend will buy a plot of land with one row, having its top-left corner at row 3 and column 2.