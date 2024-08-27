## Task

The Great Ones of the City, recurring characters in the history of Algoritmiada finals, are back in the public eye. Feeling threatened by the traditional opposition party "The Great Ones of the Commission", they plan to take a stroll through the City to attract electoral capital. The City consists of $N$ intersections and $M$ bidirectional streets connecting these intersections. Each street is associated with a positive popularity gain. The Great Ones of the City can start the walk from any intersection and can traverse each street as many times as they want, but the walk must end at the starting intersection.

Unfortunately, due to rampant corruption during the last term of the Great Ones of the Commission, the City's streets are in a questionable state. So questionable that frequently used streets can deteriorate even during the walk, having a negative effect on the popularity coefficient associated with that street. Specifically, during the first traversal of a street with a coefficient equal to $X$, the popularity of the Great Ones of the City will increase by $X$. For subsequent traversals, the popularity will increase by $(-X$, $-2X$, $-4X$, $-8X\ldots)$. Knowing this, the Great Ones of the City will try to maximize the total popularity gain by intelligently planning their walk.

You, of course, being well-connected, are working in the campaign staff of the Great Ones of the Commission. Find out the maximum popularity gain the Great Ones of the City can achieve during their walk, so the Commission can easily estimate how many votes will need to be falsified in the upcoming elections.

## Input data

The input file `mmo.in` will contain on its first line the values $N$ and $M$, representing the number of intersections in the city and the number of streets respectively. The next $M$ lines will contain three positive integers $x$ $y$ $c$, signifying the existence of a bidirectional street connecting intersections $x$ and $y$ with an associated popularity coefficient equal to $c$.

## Output data

The output file `mmo.out` will contain the required value.

## Constraints and clarifications

$1 \leq N \leq 18$

$1 \leq x$, $y \leq N$

$1 \leq M \leq N * (N - 1) / 2$

$1 \leq c \leq 10^5$

There exists at most one street connecting two intersections. 

Moreover, there are no streets with endpoints in the same intersection.

It is guaranteed that any city is accessible from any other city through the existing streets.

## Example

`mmo.in`

```
2 1
1 2 3
```

`mmo.out`

```
0
```

## Explanation

The walk starts in city $1$, passes through $2$ and returns to city $1$.