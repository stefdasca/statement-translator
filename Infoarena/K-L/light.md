Light

Avi has become the mayor in his hometown, and one of the first problems he faces is public lighting. The main street can be considered as an axis with the origin at point $O$. Along the road, there are $N$ main objectives, and Avi knows that the $i$-th objective is at a distance $a_i$ from point $O$ and stretches over a length $b_i$. The company EPT (Electricity For Dummies) has made him an offer: he will receive up to $nr$ lighting poles for the same price, each with the same lighting radius, whichever the mayor requests. Each pole can illuminate a segment of integer length $R$, but in a strange way: it can illuminate $R_1$ units of road to its left and $R_2$ units to its right, as long as $R_1+R_2 = R$. $R_1$ and $R_2$ can be adjusted when setting up each pole, but $R$ is fixed from the factory. Knowing that a larger lighting radius entails a higher cost over time, Avi asks you to determine the minimum radius for which he can ensure the lighting of the main objectives.

## Task

Knowing the starting positions and the distance each objective covers, determine the minimum radius $R$ that the poles can have to completely illuminate each objective, as well as the minimum number of poles required.

## Input data

The input file `light.in` will contain on the first line the number $N$ of objectives and $nr$ - the maximum number of poles, and on the next $N$ lines, 2 values each, $a_i$ and $b_i$, the distance to point $O$ of objective $i$, respectively its length.

## Output data

The output file `light.out` will contain on a single line 2 values, $R_{min}$ and $nr_{min}$, representing the portion illuminated by each pole, and the minimum number of poles required.

## Constraints and clarifications

$1 \leq N \leq 100000$

$0 \leq a_i \leq 1000000000$

$1 \leq b_i \leq 1000000000$

$1 \leq nr \leq 1000000$

## Examples

`light.in`
```
4 4
1 4
6 4
16 2
15 2
```
`light.out`
```
3 4
```

`light.in`
```
1 4
6 4
16 2
15 2
```
`light.out`
```
4 3
```

## Explanation

In the first case, pole 1 will illuminate the portion $(1, 4)$, pole 2 the portion $(4, 7)$, pole 3 the portion $(7, 10)$, and pole 4 the portion $(15, 18)$.

In the second example, the first pole will illuminate the portion $(1, 5)$, the second pole the portion $(6, 10)$, and the third pole the portion $(15, 19)$.