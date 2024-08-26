## Drum4

The tests for this problem are not well constructed enough to correctly separate inefficient or wrong solutions. Go here if you want to help us improve the quality of the tests for this problem! In country $X$, we have $N$ cities and $M$ one-way roads. Since this country is very young, it is not known whether it is possible to travel from any city to any other city in the country. To solve this dilemma, we need your help. If it is not possible to travel from any city to any other city, you are asked for the minimum number of roads that need to be built to make this possible.

## Input data

The input file `drum4.in` contains on the first line 2 numbers $N$ and $M$, the number of cities, and the number of roads, respectively. The next $M$ lines contain 2 numbers $x$ and $y$ representing a road from city $x$ to city $y$.

## Output data

The output file `drum4.out` must contain the minimum number of roads that need to be built so that we can travel from any city to any other city.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$ 

$1 \leq M \leq 200\ 000$ 

$1 \leq x,y \leq N$ 

## Example

`drum4.in` 

`4 3` 

`1 2` 

`2 1` 

`1 3` 

`drum4.out` 

`2` 

## Explanation

Connect city $4$ to city $1$ and city $3$ to city $4$.