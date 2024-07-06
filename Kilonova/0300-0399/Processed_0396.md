The team of archaeologists discovered an ancient map of the Northern Region, which was inhabited by a civilization led by very strict mathematical rules. According to this map, the Northern Region was divided into $n$ rows and $m$ counties, each county occupying a square area of one hectare.

However, discoveries have also shown that this civilization was attacked from the southwest by a dangerous bacterium, which acted as follows: in the first year, it infected the county in the bottom left corner of the map; in the second year, it infected the two counties adjacent to the first; in the third year, it infected the three counties adjacent to the previous two, and so on, with the infection stopping when the bacterium reached the top or right edge of the map.

- First year:

~[bacterie-1.png]

- Second year:

~[bacterie-2.png]

- Third year:

~[bacterie-3.png]

- Fourth year:

~[bacterie-4.png]

- ...

# Task 

Write a program that determines the number of counties remaining uninfected after the bacterium's expansion stops.

# Input data

The input file `bacterie.in` contains the dimensions of the map $n$ and $m$, separated by a space.

# Output data

The output file `bacterie.out` will contain the number of counties remaining uninfected after the bacterium's expansion stops.

# Constraints and clarifications

* $1 \\leq n \\leq 1 \\ 000 \\ 000 \\ 000$, $1 \\leq m \\leq 1 \\ 000 \\ 000 \\ 000$, natural numbers.

# Example

`bacterie.in`
```
3 5
```

`bacterie.out`
```
9
```

## Explanation

The map of the Northern Region contains $3$ rows of $5$ counties each, totaling $15$ counties. The expansion of the bacterium stopped after $3$ years, as it reached the top edge. There were $9$ counties left uninfected.

~[bacterie-5.png]