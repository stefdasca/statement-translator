# Div4

George and Peter thought of playing a game. George will think of two natural numbers $N$ and $K$. Peter has to tell him in how many ways he can delete exactly $K$ digits from the number $N$ such that the remaining number is divisible by $4$. The number of ways will be displayed modulo $1000003$.

## Input data

The input file `div4.in` contains on the first line the number $N$, and on the second line the number $K$.

## Output data

The output file `div4.out` contains a single natural number representing Peter's answer modulo $1000003$.

## Constraints and clarifications

$1 \leq N < 10^{100000}$

$1 \leq K < |N|$, where $|N|$ is the number of digits of $N$.

The number $N$ does not contain the digit $0$ (zero).

## Example

`div4.in` `div4.out`

`242` `1` `1`

The only possibility is to delete the digit $2$ at the end of the number, obtaining the number $24$.

`44` `1` `2`

We can delete either the first $4$ from the number or the second one.
