On a shelf, there is an array of $N$ colored boxes. Each box can be either red or green. The $i$-th box in the array has a volume equal to $V_i$ liters. Two boxes can be swapped in the array if and only if they have different colors.

# Task

Given the initial array of boxes, using at most $2N$ swap operations, sort the array of boxes in ascending order based on their volumes.

# Input data

The first line contains the number $N$, the number of boxes.  
The second line contains $N$ numbers, separated by a space, corresponding to the colors of the boxes, in the order they appear in the initial array. Read $1$ for a red box, and read $2$ for a green box.  
The third line contains $N$ natural numbers corresponding to the volumes of the boxes, in the order they appear in the initial array.

# Output data

The first line will contain $M$, the number of swap operations you performed.  
The next $M$ lines will contain a pair of numbers separated by space ($i$ and $j$) describing a swap operation (swap the box at position $i$ with the one at position $j$). The operations will be displayed in the order in which they were performed.  
If there is no valid sequence of operations that sorts the array of boxes, print the number $-1$ on the first line.

# Constraints and clarifications

* $3 \leq N \leq 2 \ 000$;
* Positions of the boxes are indexed starting from $1$
* $1 \leq V_i \leq 10^9$ for each $i$ from $1$ to $N$
* To receive points on a test:
    - if it is possible to get a sorted array, the number of swaps performed, $M$, should be $\leq 2N$ and obviously, $\geq 0$, all swaps should be valid and should be able to be performed in the specified order, resulting in a sorted array of boxes in ascending order after all $M$ swaps are applied
    - if there is no sequence of operations leading to a sorted array, print $-1$.

## Subtask 1 (12 points)
* $N = 3$
## Subtask 2 (49 points)
* the boxes have distinct volumes
* $1 \leq V_i \leq N$, for each $i$ from 1 to $N$
## Subtask 3 (39 points)
* no additional constraints

# Example 1

`stdin`
```
4
1 2 1 2
4 7 5 2
```

`stdout`
```
2
4 1
2 4
```

# Example 2

`stdin`
```
2
2 2
4 3
```

`stdout`
```
-1
```

## Explanation

For the first example, initially we have: the first box with red color and volume 4, the second box with green color and volume 7, the third box with red color and volume 5, the fourth box with green color and volume 2.

We will perform two operations ($M = 2 \leq 2N = 8$). The first operation swaps the box in position 4 with the one in position 1. We obtain the following array: the first box with green color and volume 2, the second box with green color and volume 7, the third box with red color and volume 5, the fourth box with red color and volume 4.

The second operation swaps the box in position 2 with the one in position 4. We obtain the following array: the first box with green color and volume 2, the second box with red color and volume 4, the third box with red color and volume 5, the fourth box with green color and volume 7.

We observe that the final array is sorted in ascending order based on the volumes of the boxes.

For the second example, to achieve a sorted array we would need to swap the two boxes, but it is impossible since they have the same color.