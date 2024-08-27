## Wedding

$N$ newlyweds are invited to a high-society event. There, they must sit at a rectangular table that has $N$ seats on each side. This means that $N$ of the $2 \cdot N$ guests will sit on one side of the table, while the rest will sit on the other side. Additionally, it is known that each pair of newlyweds must sit next to each other at the table, meaning they should either sit next to each other on the same side of the table or face each other. For a given $N$, determine the number of possible ways to seat the $N$ couples at the table.

## Input data

The input file `nunta.in` contains a single line that contains the natural number $N$.

## Output data

The single line in the output file `nunta.out` contains the number of ways to seat the $N$ couples at the table.

## Constraints and clarifications

$1 \leq N \leq 999$

For $40\%$ of the tests, $N < 45$

For $70\%$ of the tests, $N < 78$

Two arrangements are not considered different if it is possible to renumber the couples in the first arrangement to obtain the second one.

## Example

`nunta.in` 
```
3
```

`nunta.out` 
```
3
```

## Explanation

The $3$ distinct seating arrangements are:

The arrangements below are identical, because it is possible to renumber the couples from the first arrangement to obtain the second: