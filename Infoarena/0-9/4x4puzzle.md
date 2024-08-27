## Task

Young Gigel loves puzzles very much. A few days ago he discovered the traditional $4 \times 4$ puzzle. This puzzle consists of numbers from $0$ to $15$, arranged in a square with $4$ rows and $4$ columns. A move consists of swapping 2 adjacent elements horizontally or vertically, provided that one of the elements is the $0$ element. The goal of the puzzle is to reach the following final state:
```
1  2  3  4
5  6  7  8
9 10 11 12 
13 14 15  0
```
Given the initial state of the puzzle, determine if there is a sequence of moves such that the puzzle can be brought to the final state.

## Input data

The first line of the input file `4x4puzzle.in` contains the number $P$ of puzzles described next. Each puzzle consists of $4$ rows, displaying $4$ numbers each. Before the description of each puzzle, there is a blank line.

## Output data

For each of the $P$ puzzles, you will print in the output file `4x4puzzle.out` one line containing the string "DA" if the puzzle can be brought to the final state, or the string "NU" otherwise.

## Constraints

$1 \leq P \leq 100000$

## Example

`4x4puzzle.in`
```
2

1 2 3 4
5 6 7 8
9 10 11 0
12 13 14 15

1 2 3 4
5 6 7 8
9 10 11 0
13 12 14 15
```

`4x4puzzle.out`
```
DA
NU
```