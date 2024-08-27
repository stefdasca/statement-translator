# Magic2

We will call a magic square a $n \times n$ matrix with natural number elements that has the following property: the sum of the elements of any row is equal to the sum of the elements of any row and to the sum of the elements of any column.

## Task

Determine whether the given 2D matrix is a magic square, knowing that if it is not magic, exactly two elements should be corrected. If the square is not magic, find the positions of the erroneous elements and determine their correct values.

## Input data

The first line of the input file `magic2.in` contains a natural number $n$, representing the dimension of the given matrix. The next $n$ lines contain $n$ natural numbers each, separated by spaces, representing the elements of the matrix.

## Output data

If the given matrix is a magic square, the first line of the output file `magic2.out` will contain `magic`. If the square is not magic, the first line of the output file will contain `nu este magic`. In this case, the next line will contain four natural numbers, separated by spaces, representing the row and column indices of the first erroneous element, followed by the row and column indices of the second erroneous element. The four numbers will be separated by spaces. On the third line of the file, the correct values that should replace the two erroneous elements to make the square magic will be written.

## Constraints and clarifications

$5 \leq n \leq 100$

The elements of the matrix are natural numbers $\leq 100$.

In the output file, first write the data that describes the element located in a row with a smaller order number, and if the two numbers are in the same row, write them in the order of the column indices.

It is guaranteed that there are no ambiguous situations (e.g., all row sums cannot be equal while column sums differ).

## Example

`magic2.in`

`5`

`1 2 3 2 7`

`5 1 4 3 1`

`3 2 2 4 1`

`2 7 1 2 2`

`3 2 2 3 4`

`magic2.out`

`nu este magic`

`1 5 3 3`

`6 4`

## Explanation

The magic sum is $14$, so at position $(1, 5)$ instead of $7$ it should be $6$ and at position $(3, 3)$ instead of $2$ it should be $4$.