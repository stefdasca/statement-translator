# Sums

Haralambie is a diligent student, so he decided to do his next math homework: He received a sequence of $N$ positive natural numbers (not necessarily distinct) on a sheet of paper. He took all pairs of numbers from this sequence, added them together, and wrote the results on another sheet, resulting in a new sequence of numbers. However, he lost the first sheet and now wants to find the initial sequence of numbers.

## Task

Help Haralambie reconstitute the initial sequence of numbers.

## Input data

The file `sume.in` contains on the first line $P$, and on the next line $P$ natural numbers less than or equal to $20\ 000\ 000$.

## Output data

The file `sume.out` will contain on the first line $N$, and on the second line the $N$ numbers from the initial sequence separated by a space.

## Constraints and clarifications

$3 \leq P \leq 25000$

If there are multiple solutions, only one will be printed in the file.

If there is no solution, $-1$ will be printed in the file.

The $P$ numbers in the input file are in random order!

## Example

`sume.in`
```
3 4 5
```

`sume.out`
```
3
3 1 2
```

`sume.in`
```
15 
5 7 15 10 8 8 16 11 9 18 13 11 21 19 14 6
```

`sume.out`
```
6
2 3 5 13 8 6
```