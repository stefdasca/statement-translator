Julieta's city has a square layout and only has streets in the North-South and East-West directions, all at equal distances, named as in the drawing: the vertical street $0, 1, 2, 3, \dots$, respectively the horizontal street $0, 1, 2, 3, \dots$.

Julieta lives at the intersection of the streets: vertical $x$ and horizontal $y$ (position $(x, y)$). Romeo is in the Southwest corner of the city (position $(0, 0)$) and wants to reach Julieta, we do not know exactly why, but that's his business.

On top of all the well-known troubles of the poor boy, there are others as well:

* The city slopes upwards to the North, which makes it harder to go in that direction.
* He can only go North or East, because if "she" saw him going West or South, she would think he is moving away from her for good.

~[Poza1.png|align=right]

We call an __elementary segment__ the distance between two adjacent parallel streets.

If Romeo goes East, he consumes $1J$ ($J=joule= $a unit of energy) for each elementary segment traveled. Due to the slope, if he goes North $k$ consecutive elementary segments, he consumes ($1+2+3+ \ldots +k $ )$ \ J$.

Romeo wants to reach Julieta (__only moving in the specified directions__) with a __minimum energy consumption__.

For example: if the coordinates are: $x=4$ and $y=3$, then the adjacent drawing shows one possible path (but not with minimal energy consumption). In the drawing, we have a first horizontal elementary segment (consumption$=1J$), then North two elementary segments (consumption: $1+2 = 3J$). Followed by $3$ segments East (consumption: $1+1+1 = 3J$) and the last portion of one vertical segment (consumption: $1J$). Total energy consumption: $1+3+3+1=8J$.

# Task

Write a program that reads $x$ and $y$ and displays the __minimum number of__ $J$ consumed for the entire trip from position $(0, 0)$ to position $(x, y)$, only moving in the specified directions.

# Input data

The input file `romeo.in` contains the numbers $x$ and $y$ on the first line, separated by a space.

# Output data

The output file `romeo.out` contains a single line with the number of $J$ consumed for the total distance covered from the starting position to the final one.

# Constraints and clarifications

* $x$ and $y$ are natural numbers
* $0 \leq x, y \leq 40 000$
* Each line in the input file and the output file ends with a newline character.

# Example

`romeo.in`
```
3 2
```

`romeo.out`
```
5
```

# Explanation

~[Poza3.png|align=right]

The input data points to a city like in the drawing. 

One possible path (it is not unique) is given by the bold line. The first vertical segment consumes $1J$, the horizontal portion $3J$ and the last vertical segment (the right one), another $1J$, so we will display the number $5$, which represents $1J+3J+1J=5J$.