Supersf

It was a scorching summer day on Mars$\dots$ and in the shadow of an Apeme, Algostorm, Max Damage, and Voodoo Child meet and look in amazement at a piece of paper with the sequence of numbers $1$, $2$, $3$, $3$, $4$, $5$, $5$, $6$, $6$, and that was about it because the paper was torn$\dots$ Immediately Algostorm said: "Obviously! Each number $W$ appears $X$ times, where $X$ is the number of bits with the value $1$ in $W$'s binary representation, and $W$ goes through the sequence of natural numbers from $1$ to infinity". Voodoo Child quickly responds: "I think I can very quickly calculate what number is at a specific position in this sequence$\dots$". After a few moments of thought, Max Damage says: "I say let's make it a problem and submit it to the Stars of Informatics". And,$\dots$ here we are.

## Task

Given a number $K$, determine the number at position $K$ in the sequence generated as Algostorm described.

## Input Data

The file `supersf.in` contains a single strictly positive integer $K$, written in base $16$ with no spaces between digits, representing the position of the sought-after element in the sequence. 

## Output Data

The output file `supersf.out` contains a single positive integer $N$, representing the sought number (with no spaces between digits), also in base $16$.

## Constraints and Clarifications

$1 \leq K \leq 16\ 200000$ 

For $65\%$ of the tests 

$K \leq 16\ 6000$ 

The digits in base $16$ are $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$, $A$, $B$, $C$, $D$, $E$, $F$ (uppercase only)

## Example

`supersf.in` 
`supersf.out` 
`4` 
`3` 
`17` 
`D` 
`3D961` 
`8447` 
`96D271` 
`F41F4` 

## Explanation

The first elements in the sequence are: $1$ $2$ $3$ $3$ $4$ $5$ $5$ $6$ $6$ $7$ $7$ $7$ $8$ $9$ $9$ $A$ $A$ $B$ $B$ $B$ $C$ $C$ $D$ $D$ $D$ $E$ $E$ $E$ $\dots$ for the rest we have no paper left.