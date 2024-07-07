
Ionică has collected a lot of CDs with games, music, movies, etc., which are arranged in $n$ boxes, numbered by $1, 2, \dots, n$. His cousin, Florin, who just won a math contest, visits Ionică. To dampen Florin's enthusiasm, Ionică proposes that Florin put some of the CDs into a larger box, ensuring that each box will still contain at least one CD.

To complicate matters, Ionică does not tell Florin how many CDs are in each box. Instead, he tells him that there are a total of $S$ CDs and that if he takes a certain number of CDs from each box and places them into another box, he will eventually have the same number of CDs in all boxes.

# Task

Write a program that, given $n$, $S$, and the number of CDs moved from each box, determines the number $k$ of distinct ways to place the CDs in the larger box, following the rule from the statement.

# Input data

The input file `cd.in` contains on the first line the natural numbers $n$ and $S$ separated by a space, and on the next $n$ lines the pairs of natural numbers $y_i \ c_i$ separated by a space, corresponding to the number of CDs $y_i$ taken from box $i$ and placed into box $c_i$, for $i = 1, 2, \dots, n$.

# Output data

The output file `cd.out` contains on the first line the number $k$ modulo $9 \ 901$.

# Constraints and clarifications

* $2 \leq n \leq 300$
* Each box contains at most $1 \ 000$ CDs.
* $k$ modulo $p$ represents the remainder of the division of $k$ by $p$
* $S$ modulo $n = 0$
* A method of selecting the CDs to be placed in the larger box is different from another if from at least one box a different number of CDs is selected.

# Example

`cd.in`
```
3 12
3 2
2 3
1 1
```

`cd.out`
```
20
```

## Explanation

This results in 6 CDs in the first box, 3 CDs in the second box, and 3 CDs in the third box.
