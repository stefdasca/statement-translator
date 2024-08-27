# Pyramid

Zoe has a square matrix with $N$ rows and $N$ columns filled with $0$s or $1$s. She wants to count how many pyramids, having only $1$s on the edges, exist in the matrix. A pyramid is a right-angled isosceles triangle with the hypotenuse parallel to two of the edges of the matrix. Below are some examples of pyramids with various sides. Notice that a pyramid can be rotated any number of times by $90^\circ$. Side $1$
Side $2$
Side $3$
Side $4$
Side $2$
Side $3$
Side $1$

$0000000000$

$0100010100$

$0011110000$

$0000000000$

$0000000000$

$0100100100$

$0101011100$

$0000000000$

$0000000000$

$0000000000$

$0000000000$

$0000000000$

## Input data

The input file `piramid.in` will contain:
- The first line will contain the natural number $N$ representing the matrix size.
- The next $N$ lines will each contain $N$ characters $0$ or $1$, not separated by spaces.

## Output data

The output file `piramid.out` will contain a single number $M$, representing the total number of pyramids that meet the conditions specified in the problem statement which are in the matrix from the input file.

## Constraints and clarifications

$1 \leq N \leq 1000$

It is guaranteed that the result will not exceed $10^9$

The minimum pyramid is the one with side $1$ from the example above

## Example

`piramid.in`
`10`
`0000001000`
`0000101100`
`0001011010`
`0010001100`
`0111111100`
`0000100000`
`0001111100`
`0010101000`
`0110010000`
`0010000000`

`piramid.out`
`15`

`piramid.in`
`7`
`1111111`
`1111111`
`1111111`
`1111111`
`1111111`
`1111111`
`1111111`

`piramid.out`
`196`

## Explanations

First example: There are $3$ pyramids with side larger than $1$, and another $12$ (harder to spot) with side $1$.

Second example: Attention! Pyramids will be counted regardless of what they contain inside. The only restriction imposed is that the edges are formed only by elements of $1$.