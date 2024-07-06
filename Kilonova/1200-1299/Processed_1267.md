Ben10, the great hero, is once again in the position of saving the world. This time he must defuse a powerful bomb, whose explosion could destroy humanity. The difficulty of the task lies in the fact that the bomb is protected by a complicated device, with a cipher, composed of $N \times N$ buttons arranged in the form of a grid with $N$ rows and $N$ columns, each button having a natural number inscribed on it, as seen in $\text{Figure} \ 1$.
~[cifru.png|align=center]
The device contains several movable frames (represented in the figure by differently hatched concentric squares), which can rotate by $90$, $180$, $270$, or $360$ degrees to the left or right, thus changing the arrangement of the numbers inscribed on the device's buttons. For the example in $\text{Figure} \ 1$, we have a number of $3$ frames, represented in the figure by different background colors.
The bomb is defused if the sum of the elements on the first row (the northern one) of each frame is maximum (the hatched area in $\text{Figure} \ 2$). We agree to call this portion of the grid the northern zone.

# Task

Write a program to determine the sum of the elements in the northern zone of the grid, when the frames of the cipher have been brought into the position that defuses the bomb, as well as the configuration of the grid.

# Input data

The input file `cifru.in` contains:
The first line contains the natural number $N$, representing the number of rows and columns of the grid.
Each of the following $N$ lines contains $N$ natural numbers, separated by spaces, representing the numbers inscribed on the device's buttons.

# Output data

The output file `cifru.out` will contain on the first line a natural number $S$ representing the maximum possible sum obtained in the northern zone of the grid. On the following $N$ lines, the elements of the grid obtained by rotating the frames into the position that defuses the bomb will be printed (each $N$ elements separated by a space).

# Constraints and clarifications

* $1 \lt N \lt 101$
* The numbers inscribed on the cipher's buttons are natural numbers between $0$ and $1 \ 000$.
* A frame is composed of at least $2$ rows and $2$ columns.
* It is guaranteed that, for each frame, the maximum sum can be obtained on a single side.

# Example

`cifru.in`
```
5
5 1 1 1 4
5 0 0 0 2
5 1 0 2 2
5 2 3 4 2
7 3 3 3 8
```

`cifru.out`
```
36
7 5 5 5 5
3 4 3 2 1
3 2 0 1 1
3 0 0 0 1
8 2 2 2 4
```

## Explanation

The cipher in the example is composed of two frames. The first frame, the outer one, was rotated by $90$ degrees to the left, and the second frame was rotated by $180$ degrees to the left or right.
The sum of the bold elements is $36$, being the highest possible sum obtained by rotating the two frames in all possible ways.

