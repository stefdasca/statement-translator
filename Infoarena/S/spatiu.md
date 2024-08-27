## Task

Bulbuka boarded a rocket and got lost in an infinite bidimensional space. Before Houston realized there was a problem, Bulbuka had already moved $N$ times. All that is known at this moment is that the rocket started at coordinates $(0,0)$ and that at each step, the rocket can move from any point to the adjacent four directions of integer coordinates (for example: $(0,0) \rightarrow (0,1)$ or $(0,-1)$ or $(1,0)$ or $(-1,0)$). The problem is further compounded because the only radar that was on is broken: instead of showing the exact location of the rocket at any given moment, it recorded a series of possible steps Bulbuka might have taken. These steps are as follows: $1$ -­ up or left (example: $(0,0) \rightarrow (0,1)$ or $(-1,0)$) $2$ -­ down or right (example: $(0,0) \rightarrow (0,-1)$ or $(1,0)$) $3$ -­ up or right (example: $(0,0) \rightarrow (0,1)$ or $(1,0)$) $4$ -­ down or left (example: $(0,0) \rightarrow (0,-1)$ or $(-1,0)$) $5$ -­ up or left or down or right You, being the best programmer among those present, volunteered to calculate the number of different positions where Bulbuka could be, based on the information provided by the broken radar.

## Input data

The input file `spatiu.in` contains the first line, which contains $T$, the number of tests. Next, for each test, there is a single line containing the number $N$, followed by a space and $N$ numbers from the set $\{1, 2, 3, 4, 5\}$ representing the steps described. These numbers are not separated by spaces.

## Output data

The output file `spatiu.out` will contain $T$ lines, and each line will contain a natural number representing the number of calculated different positions.

## Constraints

$T = 20$

$1 \leq N \leq 10^5$

## Example

`spatiu.in`

```
2
3 315
2 24
```

`spatiu.out`

```
9
4
```

## Explanation

In the first test:

After the first step, the possible locations are: $(0,1)$ or $(1,0)$

After the second step, the possible locations are: $(-1,1)$, $(0,2)$, $(0,0)$ or $(1,1)$

After the third step, the possible locations are: $(-2,1)$, $(-1,0)$, $(-1,2)$, $(0,-1)$, $(0,1)$, $(0,3)$, $(1,0)$, $(1,2)$, $(2,1)$

In the second test:

After the second step: $(-1,-1)$, $(0,-2)$, $(0,0)$ or $(1,-1)$