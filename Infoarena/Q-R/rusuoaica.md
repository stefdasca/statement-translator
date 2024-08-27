# Rusuoaica

Rusuoaica, a great architect in the making from Manchester, received a complicated task from her college, so she is obviously asking for help. She needs to design the subway network of the iGorj land. It is known that the City Hall of iGorj has already built $N$ subway stations and dug $M$ tunnels. However, they have not installed train tracks on the dug tunnels. Also, due to lack of funds, it is possible that the City Hall has not dug enough tunnels, so it is possible that there are two subway stations that are not connected by an underground path. In the design of the subway network, Rusuoaica can make the following decisions:
- install train tracks on an already existing tunnel, paying the respective tunnel cost
- build a new tunnel with tracks between 2 subway stations, paying the cost $A$
- sell an already dug tunnel to the Society of Cultural iGorjenesti, turning it into an underground museum; the respective tunnel cost will be collected

Rusuoaica will not dig new tunnels between two stations where there already exists a tunnel with a cost equal to or lower than $A$. Also, Rusuoaica will prioritize buying tunnels with a cost less than or equal to $A$. Rusuoaica needs to find the minimum design cost of the network such that one can reach any station from any other station using only the subway. The cost can also be negative (sold tunnels will bring a higher profit than what will be spent to complete the project).

## Input data

The input file `rusuoaica.in` will contain on the first line 3 numbers $N$, $M$, and $A$ (as described in the statement), and on each of the following $M$ lines, 3 numbers $t_1$, $t_2$, and $t_3$ representing that there is already a tunnel from station $t_1$ to station $t_2$ with a respective cost of $t_3$.

## Output data

The output file `rusuoaica.out` will contain on the first line a single number representing the required cost.

## Constraints and clarifications

1 $\leq$ $N$ $\leq$ 100,000

1 $\leq$ $M$ $\leq$ 400,000

Both $A$ and the tunnel costs are natural numbers less than 200

For 30 points:

1 $\leq$ $N$ $\leq$ 1,000

For another 20 points, all tunnel costs are 0

A tunnel with the cost $A$ can be built between 2 stations even if one has already been dug

A tunnel with tracks built with the cost $A$ cannot be sold after purchase

All tunnels are bidirectional

## Example

`rusuoaica.in`
```
7 10 5
2 1 7
3 2 2
4 2 4
5 2 1
5 4 2
6 2 4
6 4 8
5 6 5
7 3 5
7 6 8
```

`rusuoaica.out`
```
-16
```

## Explanation

Rusuoaica will buy the tunnels $(2, 3, 2)$, $(2, 5, 1)$, $(2, 6, 4)$, $(4, 5, 2)$, $(7, 3, 5)$, sell the rest of the tunnels, and dig a new tunnel between $(1, 2)$.