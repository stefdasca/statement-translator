## Task

Catrinel has a necklace with $N$ magic pearls that can have two colors (red or black). Catrinel loves her necklace very much, but she also likes diversity, so she can change her necklace using the following operation: choose a black pearl, change the colors of the neighboring pearls (the necklace is circular and a pearl can have at most two neighbors; the left and right neighbors) to the opposite color (from red to black and vice versa), and remove the chosen black pearl from the necklace. Being curious by nature, Catrinel wonders if using the described operation she can remove all the pearls from the necklace.

## Input data

The first line of the input file `colier.in` contains $T$ the number of tests. The following $T$ lines will contain the descriptions of the tests. Line $i + 1$ contains the natural number $N$ representing the number of pearls in the necklace and the description of the necklace through a sequence of $1$ and $0$, representing the colors black and respectively red, unseparated by spaces.

## Output data

The file `colier.out` will contain $T$ lines, each containing "DA" or "NU" (without quotes), whether there exists a sequence of operations such that Catrinel can remove all the pearls from the necklace or not.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 10^5$

For tests worth 20 points, it is guaranteed that $N \leq 20$

For tests worth 50 points, it is guaranteed that $N \leq 1000$

A pearl from a necklace with only one pearl has no neighbors

A pearl from a necklace with two pearls has one neighbor

A pearl from a necklace with more than two pearls has two neighbors

## Example

`colier.in`
```
6
1 1
1 0
2 10
2 11
3 011
4 1001
```

`colier.out`
```
DA
NU
DA
NU
DA
NU
```

## Explanation

For the 5th test, the operations will look like this:
```
0 1 1 -> 1 0 -> 1 -> empty necklace
```
(the bold values represent the chosen black pearl for the operation)