# Cubes3

At the Snow White kindergarten, the children received $N$ cubes from a sponsor. The sponsor promised an additional prize to the children who build the tallest tower of cubes possible. He mentioned that this tower must be stable, meaning that a cube with a certain side cannot be placed on top of a cube with a larger side. Also, a cube with a certain weight cannot have a heavier one placed on top of it. Help the children at the kindergarten to build the tallest possible tower, which means one where the sum of the side lengths of the stacked cubes is the highest possible.

## Input data

The input file `cuburi3.in` contains on the first line the natural number $N$, representing the number of cubes. On the next $N$ lines, there are two natural numbers $l$ and $g$ (separated by a space), where $l$ represents the side of the cube and $g$ specifies its weight. There are no two identical cubes, meaning no two cubes have the same side length and weight.

## Output data

The output file `cuburi3.out` will contain on the first line two natural numbers separated by a space: $k$ and $Max$, where $k$ represents the number of cubes used to build the tower, and $Max$ represents the height formed from the side lengths of the stacked cubes. On each of the next $k$ lines, a natural number will be written, specifying the index of the cube in the sequence of cubes as read from the input file. On the first of these $k$ lines, the cube at the base of the tower will be specified, and on the last line, the cube at the top of the tower will be indicated.

## Constraints and clarifications

$1 \leq N \leq 4000$  
$1 \leq l, g \leq 20000$  

## Example

`cuburi3.in`  
```
5
10 3
20 5
15 6
15 1
10 2
```

`cuburi3.out`  
```
3 40 
2 
1 
5 
```