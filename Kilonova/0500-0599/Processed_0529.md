## Glider Task

A glider is launched on a field consisting of $N$ plots, each one km long, numbered from 1 to $N$, arranged linearly. The glider is launched from the beginning of plot $X$, from zero height. It glides over at most $K$ plots, $K \leq N$, in the increasing order of plot numbers, and then stops.

Each plot has vertical currents, which either raise or lower the glider. For each plot, the number of meters by which the glider changes its height when crossing that plot is known (let's call this number the height difference). This number can be positive if it gains height, or negative if it loses height.

## Task

Given the number $N$ of plots, $K$ - the maximum number of plots the glider can cross starting from zero height, as well as the height differences corresponding to each of the $N$ plots, solve the following three tasks:
1. The maximum height the glider reaches, if it starts from the first plot and crosses **at most *K* plots** (but at least one);
2. The maximum height the glider reaches, if it conveniently chooses a launch plot $X$ and crosses **exactly *K* plots** afterward;
3. The maximum height the glider reaches, if it conveniently chooses a launch plot $X$ and crosses **at most *K* plots** (but at least one).

## Input Data

The input file `planor.in` contains on the first line the numbers $C$, $N$, and $K$, representing the task number (1, 2, or 3), the number of plots, and respectively the maximum number of plots crossed. The second line contains $N$ numbers, representing, in the order from 1 to $N$, the height differences for the $N$ plots. Numbers written on the same line are separated by a space.

## Output Data

The output file `planor.out` will contain a single line with a single number, the answer to task $C$ from the input file.

## Constraints and clarifications

* $1 \leq K \leq N \leq 200\ 000$;
* $-200\ 000 \leq$ height differences $ \leq 200\ 000$;
* The glider can reach a negative height at any moment of the flight;
* For $12$ points, $C = 1$;
* For $4$ points, $C=2$ and $1 \leq N \leq 5\ 000$;
* For $16$ points, $C=2$ and $10\ 000 \leq N \leq 200\ 000$;
* For $20$ points, $C=3$ and $1 \leq N \leq 5\ 000$;
* For $48$ points, $C=3$ and $10\ 000 \leq N \leq 200\ 000$.

## Example 1

`planor.in`
```
1 14 4
4 -5 3 -2 6 3 -2 -1 4 3 6 -4 2 3
```

`planor.out`
```
4
```

## Explanation

Starting from plot $1$ at height $0$ and flying one plot to the right, the glider will reach the height $4$, which is the maximum possible.

## Example 2

`planor.in`
```
2 14 4
4 -5 3 -2 6 3 -2 -1 4 3 6 -4 2 3
```

`planor.out`
```
12
```

## Explanation

Starting from plot $8$ at height $0$ and flying four plots to the right, the glider will reach the height $12$. This is the maximum possible height.

## Example 3

`planor.in`
```
3 14 4
4 -5 3 -2 6 3 -2 -1 4 3 6 -4 2 3
```

`planor.out`
```
13
```

## Explanation

Starting from plot $9$ at height $0$ and flying three plots to the right, the glider will reach the height $13$. This is the maximum possible height.