# Chessboard

Eduard, the little shepherd, has a $N \times N$ chessboard. He is looking for a way to partition the chessboard into the maximum number of disjoint rectangular regions (with sides parallel to the coordinate axes), such that all regions have different areas and the number of white squares in a region is equal to the number of black squares. Since he wants to return to his sheep as quickly as possible, Eduard is asking for your help.

## Task

Given the size $N$ of the chessboard, help Eduard find a partition into regions.

## Input data

The input file `sah.in` contains a single integer $N$, the size of the chessboard.

## Output data

The output file `sah.out` will contain $N$ lines with $N$ natural numbers each. The $j$-th number on the $i$-th line will represent the region of the square at coordinates $i, j$.

## Constraints and clarifications

$1 \leq N \leq 1000$  
$N$ is even  
Each square is part of a single region  
Regions must be numbered with consecutive numbers starting from 1

## Example

`sah.in`  
```
4
```

`sah.out`  
```
1 1 1 1
1 1 1 1
2 3 3 3
2 3 3 3
```