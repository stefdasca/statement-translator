## Task

The secret organization of detective dogs that run the world has devised a security plan for Tinichea county. Currently, the county contains $N$ cities numbered from $1$ to $N$ and there are $M$ roads, where it is possible to travel from one city to another through a road. According to a decree issued by the president, travel on any road is allowed only in one direction. For the county to be secured, it must be possible to travel from any city to any other city using only roads and obviously, only in the direction where travel is allowed. Due to a lack of funds, the organization aims to build a minimum number of roads so that the county is secured.

## Input data

The first line of the input file `plan.in` contains the numbers $N$ and $M$ with the meaning from the statement. The next $M$ lines contain two numbers $x$ and $y$, meaning that there is a road on which it is possible to travel from city $x$ to city $y$.

## Output data

The first line of the output file `plan.out` contains a natural number $MIN$, the minimum number of roads that need to be constructed. On the next $MIN$ lines, there are two numbers $a$ and $b$, meaning that a road was built on which it is possible to travel from city $a$ to city $b$.

## Constraints

$1 \leq N \leq 255$

$1 \leq M \leq 1500$

If we ignore the direction of travel on roads (i.e., if it were possible to travel in both directions on each road), then it is possible to travel from any city to any other city.

If there are multiple possible placements of the roads, any can be displayed.

If the minimum number of roads that need to be built is correctly displayed, 20$\%$ of the score is obtained.

## Example

`plan.in` `plan.out`

```
3
6
1 2
2 3
2 3
2 1
1 2
1 1
```

```
1
3 1
```

## Explanation

If a road is built from city $3$ to city $1$, it is possible to travel from any city to any other city. Another possible solution could be building a road from city $3$ to city $2$.