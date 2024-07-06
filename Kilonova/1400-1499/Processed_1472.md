In ancient times, Earth was inhabited by an unusual civilization governed by very rigorous mathematical rules. This civilization consisted of multiple city-states similar to ancient cities. Each city grew gradually starting from a single square-shaped neighborhood with an area of one hectare, around which new neighborhoods of one hectare would be added each year as follows:

* In the first year, the initial neighborhood was formed,
* In the second year, the city expanded by forming $4$ new neighborhoods in all four cardinal directions,
* In the following year, the city expanded by $8$ new neighborhoods arranged around the already formed neighborhoods, and so on, with the city expanding by another row of neighborhoods each year.

| First year | Second year | Third year | Fourth year | Fifth year |
| :-: | :-: | :-: | :-: | :-: |
| ~[Poza111.png] | ~[Poza22.png] | ~[Poza44.png] | ~[Poza33.png] | ~[Poza55.png] |

The expansion of a city stops when it meets another city or if, even without meeting another city, it reaches the edge of the map on any of the four cardinal points. Two cities meet when the areas occupied by them touch or when there is only one hectare between the marginal neighborhoods of the two cities.

| Situations where city areas touch | Situations where there is one hectare space between city areas |
| :-: | :-: |
| ~[Poza6.png] | ~[Poza7.png] |

# Task

1. The size of the area (in hectares) that it would occupy after $t$ years, if it did not meet any other city and did not reach the edge of the map.
2. The time elapsed until all $N$ cities have stopped expanding, starting from the initial neighborhoods whose coordinates are read from a file, and the area of the map remaining unoccupied, expressed in hectares.

# Input data

The input file `civilizatie.in` contains:

The first line contains a natural number $p$. For all input tests, $p$ can only have the value $1$ or $2$.

The second line contains two natural numbers $x$ and $y$ representing the dimensions of the map.

The third line contains the natural number $t$.

The fourth line contains the natural number $N$.

The following $N$ lines contain two numbers $i$ and $j$ representing the initial coordinates of the $N$ cities.

# Output data

If the value of $p$ is $1$, then only the first task will be solved.

In this case, the output file `civilizatie.out` will contain a single natural number, representing the area (in hectares) of a city after $t$ years, if it did not meet any other city and did not reach the edge of the map.
If the value of $p$ is $2$, then only the second task will be solved.

In this case, the output file will contain:

On the first line, a natural number representing the area of the map remaining unoccupied after all $N$ cities have stopped expanding.
On the second line, a natural number representing the time elapsed until the last city stopped expanding.

# Constraints and clarifications

* $1 \leq N \leq 2 \ 000$
* $1 \leq x, y, t \leq 100 \ 000$
* For $30$% of the tests, it is guaranteed that $x, y \leq 500$
* For the correct solution of the first task, $20$ points are awarded, while for the correct solution of the second task, $80$ points are awarded.

# Example 1

`civilizatie.in`

```
1
7 9
9
2
3 2 
4 6
```

`civilizatie.out`

```
145
```

## Explanation

$p = 1$, the file will contain the area that could be occupied by a city in $9$ years.

Note: For this test, only the first task is solved.

# Example 2

`civilizatie.in`

```
2
7 9
5
2
3 2
4 6
```

`civilizatie.out`

```
33
4
```

# Example 3

`civilizatie.in`

```
2
10 10
5
3
2 2
2 4
3 2
```

`civilizatie.out`

```
97
1
```

## Explanation

$p=2$, so only the second task is solved.

In this case, the $3$ civilizations will not be able to expand at all, so the other $97$ hectares remain unoccupied.