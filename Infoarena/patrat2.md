# Patrat2

Gigel is playing with $n$ identical square tiles, each with a side length of $1$. At some point, he wants to form new squares from the $n$ tiles by combining multiple squares.

## Task

Help Gigel form the largest possible square by combining tiles from the $n$ tiles with a side length of $1$. Then, from the remaining tiles, form the next largest possible square, and so on, until all tiles are used up.

## Input data

The input file `patrat2.in` contains a single natural number $n$, representing the number of tiles.

## Output data

In the output file `patrat2.out`, the dimensions of the formed squares must be written. Each number will be written on a new line. The numbers written in the file must form a decreasing sequence.

## Constraints and clarifications

$1 \leq n \leq 10 ^ {4}$

## Example

`patrat2.in`
```
72 
```

`patrat2.out`
```
8 
2 
2 
```

## Explanation

$72 = 8 \cdot 8 + 2 \cdot 2 + 2 \cdot 2$