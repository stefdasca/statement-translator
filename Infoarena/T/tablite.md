## Task

The prison warden has decided to change all the identification plaques of the prisoners. This operation involves writing a natural number on each plaque, which must adhere to certain rules. The number on each plaque should have exactly $N$ digits whose sum is exactly $S$. Additionally, the warden stipulates that two neighboring digits $a$ and $b$ must not be divisible, with $Max(a,b)$ modulo $Min(a,b)$ different from $0$, except for the digits $0$ and $1$ which can be adjacent to any digit.

## Input data

The input file contains $N$ and $S$.

## Output data

The output file will contain the remainder of the number of plaques that meet the warden's requirements when divided by $60106$.

## Constraints and clarifications
- $1 \leq N \leq 1\ 000$
- $1 \leq S \leq 1\ 000$

Note, the numbers cannot start with the digit $0$! 

## Example

`tablite.in`
`tablite.out`
`3 5`
`13`

## Explanation

The plaques can have one of the following numbers: $104$, $113$, $131$, $140$, $203$, $212$, $230$, $302$, $311$, $320$, $401$, $410$ and $500$.