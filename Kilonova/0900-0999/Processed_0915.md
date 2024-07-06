```markdown
The rectangular land area is divided into $N$ horizontal strips and $M$ vertical strips of equal width. Thus, $N \times M$ square zones are formed, with each side equal to one unit. The land area is represented as a two-dimensional array with $N$ rows and $M$ columns, where for each zone, a number representing the altitude of that zone is stored. Interestingly, all values $1, 2, \dots, N \cdot M$ appear in the array. The land area is intended for tourism. Because there are extraordinarily beautiful landscapes towards the **East** and **South**, the goal is to find tourist routes that move only towards the **East** and **South** with steps of unit length. A committee, tasked with solving this problem, has determined that a route is attractive if and only if the altitude at the last position of the route is higher than the altitude at the first position of the route. A route can start and end in any of the zones on the land, respecting the previous conditions.

# Task

You are required to determine the maximum number $Z$ of zones that an attractive route can have.

# Input data

In the input file `traseu.in`, the first line contains the numbers $N$ and $M$, as described. On each of the next $N$ lines, $M$ natural numbers represent the elements of the two-dimensional array described. The numbers on the same line of the file are separated by a space.

# Output data

In the output file `traseu.out`, you will write the number $Z$ as described. If there is no attractive route, then write `0`.

# Constraints and clarifications

* $1 \leq N, M \leq 500$;
* For tests worth $40$ points, $N \leq 50$ and $M \leq 50$.

# Example 1

`traseu.in`
```
3 4
12 11 10 6
7 5 4 3
9 2 8 1
```

`traseu.out`
```
4
```

## Explanation

- The attractive routes of length $2$ are: `7-9`, `4-8`, `2-8`.
- The attractive routes of length $3$ are: `5-2-8`, `5-4-8`.
- The attractive routes of length $4$ (maximum) are: `7-5-4-8`, `7-5-2-8`, `7-9-2-8`. 

# Example 2

`traseu.in`
```
3 3
5 8 7
9 6 4
3 1 2
```

`traseu.out`
```
3
```

## Explanation

The attractive routes of length $2$ are: `5-8`, `5-9`, `1-2`.
The attractive routes of length $3$ (maximum) are: `5-9-6`, `5-8-6`, `5-8-7`.
```
