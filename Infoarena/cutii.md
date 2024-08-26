# Boxes

The test cases for this problem are not well constructed to properly differentiate inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem! Given $N$ rectangular boxes by their dimensions ($X$, $Y$ and $Z$). It is known that a box can be placed inside another box only if all of its dimensions are strictly smaller than those of the box it will be placed in. The task is to find the maximum number of boxes that can be selected from the $N$ boxes so that they can be "nested" (one box will contain another box, which in turn will contain another, and so on, down to the smallest box that will not contain anything).

## Task
The first line of the `cutii.in` file will contain $N$ and $T$, representing the number of boxes and the number of tests that will follow, respectively. For each of the $T$ tests, $N$ lines will follow, each containing 3 numbers representing the dimensions of each box.

## Input data
The first line of the `cutii.in` file will contain $N$ and $T$, representing the number of boxes and the number of tests that will follow, respectively. For each of the $T$ tests, $N$ lines will follow, each containing 3 numbers representing the dimensions of each box.

## Output data
The `cutii.out` file will contain $T$ lines, each line containing a number representing the maximum number of boxes that can be selected for each test.

## Constraints and clarifications
1 $\leq$ $N$ $\leq$ 3500 

1 $\leq$ $T$ $\leq$ 100 

The dimensions of the boxes are given as follows: each dimension (from the three possible) takes all values from 1 to $N$ in each of the $T$ tests (the values of one dimension of the boxes in a test will form a permutation of the numbers from 1 to $N$).

The execution time is chosen such that 20% of it will be used for reading and the remaining 80% for calculating the results.

40% of the tests will have $N$ $\leq$ 100 while the rest will have $N$ = 3500 and $T$ = 100.

A box cannot be rotated in any way (its dimensions will maintain their order).

## Example

`cutii.in` 
```
3 2
1 1 1
2 2 2
3 3 3
1 2 2
2 1 1
3 3 3
```

`cutii.out`
```
3
2
```

## Explanations
For the first set of boxes, all boxes are selected because box 2 can be placed in box 3, and box 1 in the second one. For the second set, boxes 1 and 3, or boxes 2 and 3, can each be selected as there is no possibility to take them all.