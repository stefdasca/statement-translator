# Roads

In a country, there are $n$ cities and a total of $m$ roads that can be traveled in both directions. Between any two cities, there can be at most one road. Unfortunately, the crime rate in this country is very high and there are numerous highway robberies. For this reason, the country's leaders have decided to place guards on each road. Due to the introduction of a single tax rate, the budget funds are limited. To reduce expenses, each guard must oversee two roads. A guard can only oversee two roads that intersect, and it is desired that each street is overseen by exactly one guard and each guard oversees exactly two roads. The network of roads is built such that from one city, one can reach any other. You will have to verify if the country can be guarded in such a way that the leaders' wishes are respected and, if possible, to determine the roads overseen by each guard.

## Input data

The first line of the input file `drumuri.in` contains two natural numbers $n$ and $m$, representing the number of cities and the number of roads, respectively; these numbers are separated by a space. The following $m$ lines contain two integers, separated by a space, representing two cities between which there is a road.

## Output data

The output file `drumuri.out` will contain on the first line the value $1$ if there is a solution, or the value $0$ if there is no solution to the problem. If there is a solution, then on the next $m / 2$ lines, three integers will be written; thus, on line $i + 1$, the numbers $x$, $y$, and $z$, separated by a space, will be written, with the meaning: guard $i$ oversees the road between cities $x$ and $y$, as well as the road between cities $y$ and $z$.

## Constraints and clarifications

$1 \leq n \leq 10\ 000$

$1 \leq m \leq 30\ 000$

## Examples

`drumuri.in`

``` 
5 6
1 2
2 3
3 1
3 4
4 5
5 3
```

`drumuri.out`

``` 
1
3 1 2
3 4 5
3 5 2
```

`drumuri.in`

``` 
3 3
1 2
2 3
3 1
```

`drumuri.out`

``` 
0
```