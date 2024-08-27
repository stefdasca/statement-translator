# Demolish

Patratel has made a serious profit from his ostrich business and now wishes to expand. With the money he has, he intends to build a farm in a region. The region is rectangular and has a length of $M$ kilometers and a width of $N$ kilometers, and the farm must also be rectangular with sides parallel to those of the region. However, there are $F$ farms of other wealthy people already built in the region, also rectangular with sides parallel to the region. Patratel is a picky person (like his ostriches, after all), and he wants a farm of $DX$ kilometers in length and $DY$ kilometers in width. The construction of such a farm is not always possible because it depends on the position of the other $F$ farms. Each farm has a demolition cost (the cost Patratel has to pay to demolish that farm). He wants to place his farm in the region such that the sum of the demolition costs of the farms intersected by his farm is minimal. Two farms intersect if and only if a point on the sides of the first farm is strictly inside the second farm (i.e., they do not intersect if only their sides touch).

## Task

Determine the minimum cost Patratel has to pay to build his farm.

## Input Data

The first line of the file `demolish.in` contains five natural numbers $M$, $N$, $F$, $DX$, and $DY$ (in this order), as described above. Each of the next $F$ lines contains another set of five numbers, $$(x1, y1, x2, y2, C)$$, where $(x1, y1)$ represents the coordinates of the bottom-left corner of a farm in the region, $(x2, y2)$ the coordinates of the top-right corner of that farm, and $C$ the demolition cost of that farm. For such a set, we always have:
$$0 \leq x1 < x2 \leq M$$ 
$$0 \leq y1 < y2 \leq N$$ 
$$0 \leq C \leq 200000$$ 

## Output Data

The first line of the file `demolish.out` contains $COST$, the required minimum cost. The second line contains four integers separated by a space, $$(x1, y1, x2, y2)$$, representing the position of the farm in the region: $(x1, y1)$ - coordinates of the bottom-left corner and $(x2, y2)$ - coordinates of the top-right corner of the farm built by Patratel to achieve the minimum cost $COST$. If there are multiple placement options, the one with the minimum $x1$ will be displayed, and if there are still multiple options, the one with the minimum $y1$ will be displayed.

## Constraints and Clarifications

$$4 < M, N < 500001$$ 
$$0 < DX < M + 1$$ 
$$0 < DY < N + 1$$ 
$$F < 30001$$ 
Obviously, the already built farms in the region do not intersect
Any two farms do not intersect if they only touch their sides
There may be two farms among $F$ that have the same demolition cost

## Example

`demolish.in`

```
12 10 6 7 8
2 3 5 8 3
5 7 7 9 7
8 4 12 8 22
7 1 9 2 4
0 0 1 2 10
1 9 2 10 6
```

`demolish.out`

```
14
1 0 8 8
```

## Explanation

The minimum cost is obtained if the farm is positioned according to the coordinates $(1, 0, 8, 8)$, intersecting farms $1$, $2$, and $4$, which need to be demolished. The sum of the demolition costs is $3 + 7 + 4 = 14$. Another possible placement that also leads to a cost of $14$ is $(1, 1, 8, 9)$, but this does not meet the condition of minimal coordinates.