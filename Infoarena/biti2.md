Biti2

Professor Richard, on an expedition in the Valley of the Kings, discovered an inscription on the bricks of a pyramid in the form of a binary sequence: $01101001100101101001011001101001 \dots$ He observed that the sequence is constructed as follows: the first character is $0$, then at every position representing a power of $2 \ ( 1, 2, 4, 8, 16 \dots )$ the current sequence is inverted ($0$ becomes $1$ and $1$ becomes $0$) and added to the current sequence.

## Task

Because some characters have been erased over time, Professor Richard will give a list with $N$ positions for which you have to find out what character it represents.

## Input data

The first line of the input file `biti2.in` will contain $N$, the number of positions for which you have to find the character in the binary sequence. Each of the next $N$ lines contains the value of these positions.

## Output data

Each of the first $N$ lines of the output file `biti2.out` will contain the value $0$ or $1$ corresponding to the character at the given positions.

## Constraints and clarifications

$1 \leq N \leq 10$

The first character of the sequence is at position $0$

Each position for which you have to find the character in the sequence is within the range $\[ 0, 102500 \]$

## Example

`biti2.in`

`3`

`0`

`2`

`13`


`biti2.out`

`0`

`1`

`1`