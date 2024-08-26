## Task

Petrica is the president of a country with $N$ cities connected by bidirectional roads such that there exists a unique path between any two of them. These cities are numbered from $1$ to $N$ so that no two cities have the same number. Petrica wants to divide them into four districts by blocking exactly three roads. He also wants the population of the cities to be distributed as uniformly as possible: the difference between the population of the district with the largest population and the population of the district with the smallest population should be as small as possible. Find this difference for President Petrica.

## Input data
The first line of the file `petrica.in` will contain the number $N$ representing the number of cities. The second line contains the population of each city ($N$ integers). The following lines contain two integers $A$ and $B$ indicating: there is a road between cities $A$ and $B$.

## Output data
The first line of the file `petrica.out` will contain a natural number representing the minimum difference Petrica wants to find.

## Constraints and clarifications

$4 \leq N \leq 200$ 

The population of each city is an integer in the range $[1, 10000]$ 

The population of a district is calculated as the sum of the population of the cities in that district 

Two cities are in the same district if one can reach the other by traveling on roads that have not been blocked 

For $50\%$ of the tests, $N \leq 70$ 

## Example

`petrica.in` 

$4$ 

$2 \quad 1 \quad 1 \quad 1$ 

$1 \quad 2$ 

$1 \quad 3$ 

$1 \quad 4$ 

`petrica.out` 

$1$ 

After translating and double-checking, everything seems grammatically and syntactically correct.