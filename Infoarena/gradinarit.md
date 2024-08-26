## Task

Gigel is a young farmer who has a vegetable garden where he grows tomato seedlings $(R)$ and cucumber seedlings $(C)$. If you are not familiar with growing vegetables, here is how things stand:

- The plots are generally rectangular.
- The distance between rows is equal, so a rectangular plot can accommodate a maximum of $N$ rows, regardless of the type of seedlings in each row.
- In each row, the distance between two adjacent seedlings is equal, so a row can accommodate a maximum of $M$ vegetable seedlings, regardless of their type.

Unfortunately for Gigel, all his seedlings have been invaded by pests, and he has learned that treatments are different depending on the type of seedling. Such a treatment kills the pests for the corresponding seedling but kills both the pests and the different seedlings (i.e., the treatment for tomatoes destroys all the pests but also the cucumber seedlings, etc.).

Each treatment is quite expensive, so Gigel can only afford $X$ doses of treatment (it costs the same regardless of the vegetable). A dose of treatment can be used for any number of seedlings in the same row, but it cannot be paused for use either to move from one row to another or to treat non-consecutive seedlings in the same row because the non-use time of the treatment is too long, and it spoils quickly if not used continuously. Since the doses of treatment are limited, Gigel can treat a seedling with the correct treatment and it will survive, with the wrong treatment or not treat it in which case the respective seedling will die.

Help Gigel maximize the number of seedlings that will survive after the treatment under the conditions specified by the problem.

## Input data

The input file `gradinarit.in` contains:
- the first line contains two integers: $N$ - the number of rows, $M$ - the number of seedlings in each row, and $X$ - the number of available doses of treatment
- on the next $N$ lines there are $M$ numbers each, which represent the order of the seedlings in the respective row coded by a sequence of characters `'R'` and `'C'` separated by a space

## Output data

In the output file `gradinarit.out` write a single line containing an integer that represents the maximum number of seedlings that can survive after treatment.

## Constraints and clarifications

$0 \leq N, M \leq 60$ \\
$0 \leq X \leq 5000$ 

## Example

`gradinarit.in` 
```
5 7 3
C R C R R R R
C R C R C R R
C R R C C C R
C R C R R R R
C C R C R R R
```

`gradinarit.out`
```
14
```