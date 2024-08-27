# Words 3

Let $C$ be a set of words, all of a fixed length $L$. We say that a string of characters $S$ can be written using the set of words $C$, if for any character in $S$ there is a sequence of $L$ characters from $S$ that is a word from $C$ and contains that character. A string of characters $S$ is given, 

composed only of letters from the English alphabet, where letter cases alternate (## Examples:

`aBcDeF`, `AbCd`). Determine a set $C$ of minimal cardinality that contains only words of length $2$, which can be used to write the string $S$.

## Input data

The input file `cuvinte3.in` will contain the string $S$.

## Output data

The first line of the file `cuvinte3.out` will contain a single natural number $min$ representing the minimal cardinality of the set $C$. The next $min$ lines will contain one word of length $2$ from the determined set $C$. The words will be displayed in alphabetical order.

## Constraints

The length of the string $S$ is less than or equal to $100 \ 000$

It is considered that $a < b < \dots < z < A < B < \dots < Z$

$C$, being a set, will consist only of distinct words

If there are multiple sets of minimal cardinality, the lexicographically smallest one will be shown.

We say that a set $A=(A_1, A_2 \dots A_N)$ of words is smaller than a set $B=(B_1, B_2 \dots B_N)$ if there is a position $1 \leq i \leq N$ such that $A_1=B_1$, $A_2=B_2 \dots A_{i-1}=B_{i-1}$ and $A_i < B_i$.

## Example

`cuvinte3.in`  `cuvinte3.out`

`aAaAbAbAbBbB`  `3`
`aA`
`bA`
`bB`

`pQpQ`  `1`
`pQ`

`LoL`  `2`
`oL`
`Lo`

## Explanation

For the first test, another solution, larger in terms of lexicographic order, is:
$aA$
$bB$
$Ab$