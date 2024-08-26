# Esir

Let us consider a sequence consisting of $N$ non-negative integers. Suppose these elements are $S_1$ $S_2$ $\dots$ $S_N$, in the order they occur in the sequence. Such a sequence is called an esir (Euclidean sequence) if the sequence $S_1 + 1$ $S_2$ $S_3$ $\dots$ $S_{N-1}$ $S_N - 1$ can be obtained by rotating the first sequence $0$ or more times (to the left or to the right). For example, the sequences $2$ $2$ $2$ $3$ and $1$ $2$ $1$ $2$ $2$ are esir sequences, but the sequence $1$ $2$ $1$ $2$ is not. Determine an esir with $N$ elements, for which the sum of the elements ($S_1 + S_2 + \dots + S_N$) is equal to $K$.

## Input data

The first line of the input file `esir.in` contains the integers $N$ and $K$, separated by a space.

## Output data

The output file `esir.out` will contain, in order, the $N$ elements of the determined esir sequence.

## Constraints

$2 \leq N \leq 1000$

$1 \leq K \leq 30\ 000$

The greatest common divisor of the numbers $N$ and $K$ is $1$.

## Example

`esir.in`
`
9 16
`

`esir.out`
`
1 2 2 2 1 2 2 2 2
`