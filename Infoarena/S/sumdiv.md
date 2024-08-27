Sum of Divisors

Given two natural numbers $A$ and $B$. Let $S$ be the sum of all natural divisors of $A^B$.

## Task

Display the remainder of the division of $S$ by $9901$.

## Input data

The first line of the input file `sumdiv.in` contains the two numbers $A$ and $B$, separated by at least one space.

## Output data

The first line of the output file `sumdiv.out` will contain the remainder of the division of $S$ by $9901$.

## Constraints

$0 \leq A \leq 50\ 000\ 000$

$0 \leq B \leq 50\ 000\ 000$ (fifty million)

## Example

`sumdiv.in`

$
2\ 3
$

`sumdiv.out`

$
15
$

## Explanation

$2^3 = 8$. 

The natural divisors of $8$ are: $1$, $2$, $4$, $8$.

Their sum is $15$.

The remainder of the division of $15$ by $9901$ is $15$ (which should appear in the output file).