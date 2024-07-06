**Tsunami** is the _tidal wave_ that propagates through the waters of the oceans/seas as a result of underwater eruptions and/or very strong submarines or coastal earthquakes.

Researchers want to prevent the effects of potential tidal waves by marking and classifying areas with a high risk of flooding.

The studied territory was divided into $n \times m$ identical squares (zones), resulting in a digitized map represented as a two-dimensional array with $n$ rows and $m$ columns. Each element of the array stores the elevation (height) of the land in the corresponding unit square. Water zones have an elevation of $0$, while land zones have elevations greater than $0$.

Any tsunami is classified based on the height of the tidal wave, on a scale from $1$ to $10$. Researchers want to mark high-risk zones that can be affected by a potential tsunami.

Initially, the tidal wave appears in all areas with an elevation of $0$ neighboring at least one land zone. A territorial area can be affected if it has an elevation strictly less than the height of the tidal wave and is in the vicinity of the water or an affected area. Two unit squares are neighboring if they have a common side.

# Task

Given the digitized map of the monitored zones, determine the number of land zones affected by a tsunami of height $h$.

# Input data

The input file `tsunami.in` contains on the first line three natural numbers $n, m,$ and $h$ separated by a space, representing the dimensions of the map and the height of the tidal wave. The following $n$ lines contain $m$ natural numbers separated by a space, representing, in order, the elevations of the $n \cdot m$ unit territorial squares of the map.

# Output data

The output file `tsunami.out` contains a single value that represents the number of unit squares affected by a tsunami of height $h$.

# Constraints and clarifications

* $2 \leq n, m \leq 1\ 000$
* $1 \leq h \leq 10$
* The monitored area **does not** contain interior lakes (unit squares that are neighboring, having an elevation of $0$, completely surrounded by unit squares with elevations strictly greater than $0$)
* Elevations are natural numbers $\leq 1\ 000$

# Example

`tsunami.in`
```
6 7 3
0 0 4 2 5 0 0
1 0 0 7 3 6 0
2 3 0 5 2 2 0
0 7 5 4 0 0 0 
0 5 2 3 0 2 0 
0 4 4 8 0 2 0
```

`tsunami.out`
```
6
```

## Explanation

The flooded areas are bolded in the two-dimensional array:

~[img.png|width=20em]