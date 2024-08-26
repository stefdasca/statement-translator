## Task

People in Romania drink a lot of beer. For each city $i$ among the $N$ cities of the country (numbered from $1$ to $N$), the amount of beer $B_i$ required by its inhabitants is known. To meet the total demand, a famous beer producer company wants to establish $K$ breweries in $K$ different cities in Romania. From these breweries, beer will be transported to other cities using the existing road network. Each road connects $2$ distinct cities and has a certain length. Due to recent floods, the road network in Romania has the structure of a tree: there is exactly one path between any pair of cities. Let's consider a city $i$ and a brewery placed in a city $X$, which is the closest brewery to $i$. The transportation cost of beer from city $X$ to city $i$ is $dist(i,X) * B_i$, where $dist(i,X)$ is the distance between city $i$ and city $X$. The beer producer company wants to choose the placement of the $K$ breweries in such a way that the maximum transportation cost of beer to any city in the country is minimized.

## Input data

The first line of the input file `berarii.in` contains the integer $T$, representing the number of upcoming tests. The first line of each test contains $2$ integers: $N$ and $K$. The next $N$ lines contain the quantities of beer required in each city: the $i$-th of these lines contains the value $B_i$. The following $N-1$ lines each contain $3$ integers: $A$, $B$ and $L$, indicating that there is a road of length $L$ between cities $A$ and $B$.

## Output data

For each of the $T$ tests, in the order given in the input file, you will print in the output file `berarii.out` a single line containing the minimum possible value for the maximum transportation cost of the beer, in the case of an optimal placement of the breweries.

## Constraints and clarifications

$1 \leq T \leq 21$

$1 \leq N \leq 100 \ 000$

$1 \leq K \leq N$

$1 \leq B_i \leq 10 \ 000$

The length of any road is an integer from the interval $[1, 10 \ 000]$.

## Example

`berarii.in`
```
1
4
2
3
4
2
7
1 2 10
2 3 21
2 4 57
```

`berarii.out`
```
42
```

## Explanation

The tree is illustrated in the figure below. The cities where breweries will be built are colored in yellow. The maximum transportation cost of beer, equal to $42$, is obtained between city $3$ and the brewery placed in city $2$.