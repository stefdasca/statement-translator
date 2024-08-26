Fold

Shepherd Ion decided to build a new pen for his sheep. The field where Ion wants to build the pen is rectangular, divided into $n*m$ plots, and slightly uneven. For each plot, we know if it is at the normal level or is uneven. The pen must have a rectangular shape, with sides parallel to the sides of the field, and is supported by four stakes located at the four corners. The four stakes can be driven into the ground only in leveled plots.

## Task

For the shepherd, it would be very important to know how many possible placements exist for the pen, but he is tired of counting sheep, so he asks for your help in counting the rectangles.

## Input data

The input file `fold.in` contains on the first line two integers $n$ and $m$ separated by a single space which represent the dimensions of the field. Each of the next $n$ lines contains $m$ numbers, separated by a space, which can have the values $0$ for uneven terrain or $1$ for normal level.

## Output data

The output file `fold.out` must contain a single line which will contain a single number representing the number of placement possibilities.

## Constraints and clarifications

$1 \leq n \leq 250$

$1 \leq m \leq 2000$

## Example

`fold.in`
```
3 3 
0 1 1 
1 1 1 
1 1 1 
```

`fold.out`
```
5
```