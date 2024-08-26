# The Game

Gigel received a box of $sticks$ as a gift. The $sticks$ have different lengths, not necessarily distinct. Gigel wants to divide the $sticks$ into two groups such that the $sticks$ in one group, placed one after another, form a "line" whose length is as close as possible to the "line" formed by the $sticks$ in the other group. The length of the line of $sticks$ is equal to the sum of the lengths of the $sticks$ that form the line.

## Task

Determine the lengths of the two lines formed by the $sticks$ placed in the two groups, such that the difference between the length of the "line" formed by the $sticks$ in the first group and the length of the "line" formed by the $sticks$ in the second group is minimized.

## Input data

The first line of the file `$jocul.in$` contains the natural number $n$, representing the total number of $sticks$. 
The next $n$ lines contain one natural number each, representing the lengths of the $sticks$ received by Gigel.

## Output data

The first line of the output file `$jocul.out$` should contain two natural numbers, corresponding to the lengths of the first and second "lines" of $sticks$ after their distribution into the two groups.

## Constraints and clarifications

$5 \leq n \leq 1000$ 

$1 \leq length_i \leq 100 \ (i = 1, 2, \dots, n)$, the lengths are given in $mm$

If the two numbers differ, they will be written in ascending order in the file.

## Example 

`jocul.in`

```
7
28
7
11
8
9
7
27
```

`jocul.out`

```
48
49
```