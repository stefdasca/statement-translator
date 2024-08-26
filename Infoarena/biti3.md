## Task

Consider all sequences of $N$ bits containing exactly $3$ bits of $1$, which we sort lexicographically (a bit of $0$ being "smaller" than a bit of $1$). Determine the $M$-th sequence in lexicographic order.

## Input data

The file `biti3.in` contains $2$ integers, separated by a space: $N$ and $M$. $N$ represents the total number of bits, and $M$ represents the position of the sequence in lexicographic order that needs to be determined.

## Output data

In the file `biti3.out` you will print the $N$ bits (among which exactly $3$ have the value $1$) of the $M$-th sequence.

## Constraints

$3 \leq N \leq 1666$

$1 \leq M \leq \text{number of distinct sequences of } N \text{ bits, among which exactly } 3 \text{ bits have the value } 1$

## Example

`biti3.in`
$5\ 7$

`biti3.out`
$10110$