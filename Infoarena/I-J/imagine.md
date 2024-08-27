## Image

An image is presented as a matrix with dimensions $2^k \times 2^k$ in which each element of the matrix is either white or black. Because the dimensions of the matrix can be very large, the following encoding of the image is used: a completely white image is associated with the code $a$, a completely black image is associated with the code $n$, any other kind of image is associated with the code $(q_1 q_2 q_3 q_4)$ where $q_1$, $q_2$, $q_3$, and $q_4$ are the codes associated with the four quadrants of the image: $q_1 q_2 q_3 q_4$. The following operations can be performed on an image: $S$ - counterclockwise rotation, $D$ - clockwise rotation, $O$ - symmetry about the horizontal axis, $V$ - symmetry about the vertical axis, $I$ - inversion of colors.

## Task

Given the code of an image and a sequence of operations, determine the code of the image after the respective operations.

## Input data

The input file `imagine.in` contains the code of the image on the first line and a sequence of operations on the second line.

## Output data

The output file `imagine.out` contains a single line that includes the code of the image obtained after the performed operations.

## Constraints and clarifications

$1 \leq$ length of the image code $\leq 10\ 000\ 000$

$0 \leq$ number of operations $\leq 10\ 000\ 000$

## Example

`imagine.in`
```
(n(anna)a(naan)) 
DOI 
```

`imagine.out`
```
((anna)(naan)na) 
```

## Explanation

The initial image and the images after each operation.