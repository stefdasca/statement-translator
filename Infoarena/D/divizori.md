## Divisors

We will consider a natural number $N$. In the array $A$, we will place all the divisors of $N$. The task is to permute the elements of array $A$ such that for any two consecutive elements $A_i$ and $A_{i+1}$, we have either $A_i = A_{i+1} * p$ or $A_{i+1} = A_i * p$, where $p$ is an arbitrary prime number. The value of $p$ can differ from one pair of elements to another.

## Input data

The input file `divizori.in` contains $N$.

## Output data

The first line of the output file `divizori.out` will contain the length of the array $A$. The second line of the file will contain the elements of $A$. If multiple solutions exist, any of them can be displayed.

## Constraints and clarifications

$2 \leq N \leq 2\ 000\ 000\ 000$

## Example

`divizori.in`

`12`

`divizori.out`

`6`

`1 2 4 12 6 3`