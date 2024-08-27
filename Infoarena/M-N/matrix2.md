# Matrix2

The tests for this problem are not well constructed enough to correctly differentiate inefficient or incorrect solutions. Click here if you want to help us improve the quality of the tests for this problem!

Ionel is a major movie producer and has already become famous (you have heard of him, right?). Recently, while working on a new film, he encountered a problem he could not solve, so he is asking for your help. He received sponsorship from a very important company, and therefore he needs to advertise it in his new film. To do this, he thought of placing the movie in a frame where he felt the sponsor's name would look good. What he doesn't know exactly is where to position the company's name. He provides you with the frame description in the form of a binary matrix with $N$ rows and $M$ columns where $0$ represents an empty pixel, and $1$ represents a pixel that is part of the film's décor and must not be covered in any way. The sponsor's name will be rectangular in shape and must be placed parallel to the coordinate axes. It is also known that the amount of money received from the sponsor will be directly proportional to the area of this rectangle, so Ionel would like the area to be maximized.

## Input data

The first line of the `matrix2.in` file will contain 2 numbers, $N$ and $M$, representing the number of rows and the number of columns of the matrix, respectively. On the next $N$ lines, the file will contain $M$ digits of 0 or 1 representing the matrix from the problem statement.

## Output data

The `matrix2.out` file will contain a single number, representing the area of the rectangle.

## Constraints and clarifications

$1 \leq N$
$M \leq 1000$

## Example

`matrix2.in`

`
4 5 
1 0 0 0 1 
1 0 0 0 1 
1 1 1 0 1 
1 0 0 1 0
`

`matrix2.out`

`6`