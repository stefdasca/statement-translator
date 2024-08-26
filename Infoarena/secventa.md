# The Sequence

The tests for this problem are not well-designed to accurately distinguish inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem! Gigel has an array of $N$ integers. Everyone knows that a sequence is a subarray of numbers that appear in consecutive positions in the original array. Gigel has defined the base of a sequence as the minimum value of the elements from that sequence.

## Task

Given a natural number $K$, determine for Gigel a sequence of length at least $K$ with the maximum base.

## Input data

The input file `secventa.in` contains on the first line the numbers $N$ and $K$, separated by a space. The second line contains the elements of the array separated by spaces.

## Output data

The output file `secventa.out` must contain a single line with three numbers: the starting position and ending position of the sequence of length at least $K$ with the maximum base, and the maximum value of the base.

## Constraints and clarifications

$1 \leq K \leq N \leq 500\,000$

The elements of the array are integers in the range $[-30\,000, 30\,000]$

If there are multiple solutions for which the maximum base is obtained, then the sequence with the smallest starting position is chosen, and in case of a tie, the one with the smallest ending position.

## Example

`secventa.in`
```
8 3
-1 2 3 1 0 4 8 6
```

`secventa.out`
```
6 8 4
```

## Explanation

The sequence that starts at position $6$ and ends at position $8$ (of length $3$) is $(4, 8, 6)$ which has a base of $min(4, 8, 6) = 4$. There is no other sequence with length greater than or equal to $3$ that has a higher base.