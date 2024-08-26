# Criminal Problem

Because he ate too many candies, Algorel began to play with them. He has $N^2$ candies that he arranges in such a way that they form a matrix of dimensions $N \times N$. After arranging them, he looks proudly at them and then starts changing their arrangement repeatedly. An operation is defined as a rearrangement of the matrix elements according to the following rule: first, establish an order of the candies starting from the top left corner of the matrix in a spiral shape; then arrange them, in the established order, into a new matrix filling the first row from left to right, then the second row from left to right, and so on (see the attached drawing). $P$ of the $N^2$ candies are more special: they contain alcohol. Algorel's parents know the initial position of each special candy and how many operations he performed. To monitor him as closely as possible, they want to know the position of each special candy after each operation performed by Algorel.

## Input data

The first line of the file `penal.in` contains 3 natural numbers $N \ M \ P$ - $N$ represents the side of Algorel's candy matrix, $M$ represents the number of operations he performed, and $P$ represents the number of special candies. The second line of the file contains $P$ pairs of natural numbers separated by spaces, representing the initial positions of the special candies.

## Output data

The output file `penal.out` will contain $M$ lines, each containing $P$ pairs of natural numbers separated by spaces representing the positions of the special candies after each operation. The order of the candies on each line must be the same as in the input file.

## Constraints

$1 \leq N \leq 40000$

$1 \leq P \leq \min(100, N^2)$

$1 \leq M \leq 1000$

For 30% of the tests $N \leq 50$,

while for 60% of them $N \leq 1000$.

The positions of the special candies are valid.

There are no two special candies in the same position.

## Example

`penal.in`
```
3 2 3
1 1
2 3
3 2
```

`penal.out`
```
1 2
1 2
2 3
1 1
3 1
3 2
```