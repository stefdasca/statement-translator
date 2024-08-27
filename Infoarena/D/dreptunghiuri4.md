## Task

You are given $N$ rectangles in a plane, with sides parallel to the coordinate axes. The task is to calculate the area in the plane covered by exactly $K$ rectangles.

## Input data

The input file `dreptunghiuri4.in` will contain on the first line the numbers $N$ and $K$ as defined in the statement. The following $N$ lines will each contain 4 numbers representing the coordinates of 2 opposite corners of each respective rectangle.

## Output data

The output file `dreptunghiuri4.out` will contain a single number, representing the area in the plane covered by exactly $K$ rectangles.

## Constraints

$1 \leq N \leq 1000$  
$1 \leq K \leq 1000$  
The coordinates of the rectangles will be integers less than or equal to $1 \ 000 \ 000 \ 000$

## Example

`dreptunghiuri4.in`  
```
3 2 
0 0 2 2 
1 1 3 3 
2 2 4 4 
```
`dreptunghiuri4.out`  
```
2 
```

## Explanation

The rectangles $1 \ 1 \ 2 \ 2$ (formed from the intersection of the first two) and $2 \ 2 \ 3 \ 3$ (formed from the intersection of the last two) are the only ones that are formed at the intersection of exactly $2$ of the original rectangles and together have an area of $2$.