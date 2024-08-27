## Task

Gigel, the young farmer from the previous stage, has the same vegetable garden, but he has managed to diversify his activities and is now growing more types of vegetables coded by letters from $'A'$ to $'Z'$. If you are not skilled in vegetable cultivation and have forgotten the statement from the previous stage, the situation is as follows:
- The plots are generally rectangular.
- The distance between rows is equal, so a rectangular plot can accommodate a maximum of $N$ rows, regardless of the type of seedlings on each row.
- On each row, the distance between two adjacent seedlings is equal, so a row can accommodate a maximum of $M$ vegetable seedlings, regardless of their type.

Again, Gigel's seedlings are invaded by pests, and treatments still vary depending on the type of seedling, but have the same price regardless of their type. However, this time treatments have evolved and kill pests for the corresponding seedling only if it is the last treatment applied to that particular seedling (i.e., the tomato treatment kills tomato pests as long as no other treatment was applied later). Furthermore, a treatment of a certain type does not kill the pests or harm the crop of different types of seedlings.

A dose of treatment can be used for any number of consecutive seedlings on the same row, but it cannot pause usage either when moving from one row to another, nor to treat non-consecutive seedlings on the same row because the downtime is too long, and it spoils quickly if not used continuously. Since treatment doses are expensive, Gigel wants to find out the minimum number of treatment doses he needs to buy to save all the seedlings in his garden under the conditions specified in the problem.

## Input data

The input file `gradinarit2.in` contains:
- The first line contains two integers: $N$ - the number of rows, $M$ - the number of seedlings on each row.
- The following $N$ rows contain $M$ characters each that represent the order of seedlings on the respective row, coded by a sequence of characters from $'A'$ to $'Z'$, separated by a space.

## Output data

In the output file `gradinarit2.out` print a single line that contains an integer representing the minimum number of treatment doses bought to save all the seedlings in the garden.

## Constraints and clarifications

$0 \leq N \leq 60$

$0 \leq M \leq 60$

The types of seedlings are coded from $'A'$ to $'Z'$.

## Example

`gradinarit2.in`

```
2 10
A B B C C B B A A A
A B B A A C C A D A
```

`gradinarit2.out`

```
7
```