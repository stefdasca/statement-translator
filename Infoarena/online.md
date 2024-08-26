# Online

In an imaginary country, a road network must be built between $N$ cities. The Minister of Transport approached $M$ construction companies and asked them to estimate the cost of roads that would connect two cities directly, without passing through others. From the $M$ offers referring to $M$ different roads (possible to construct), the Minister of Transport chose a minimum number of pairs of cities to connect directly by a road, ensuring that from any city it is possible to travel to any other city directly or through other cities with minimal cost. Construction was to begin in $K$ weeks. During this period, the Minister of Transport received a new offer each week, referring to other possible direct roads between two cities and some already offered roads but with different costs. The Minister of Transport must update the project weekly to determine which roads to construct after the $K$ weeks.

## Task

Determine the initial project. Then, based on the new offers received during the $K$ weeks, determine a new project each week to ensure the total cost of construction is minimal.

## Input data

The first line of the input file `online.in` contains two natural numbers $N$ and $M$, separated by a space, representing the number of cities and the number of offers. Each of the next $M$ lines contains three natural numbers, separated by spaces, the first two representing the indices of the two cities that would be connected directly by the respective road, and the third one the cost of that road. The next line contains the natural number $K$, representing the number of weeks during which the project will be improved. The next $K$ lines contain three natural numbers each, having the significance described above.

## Output data

The output file `online.out` will contain the costs of the projects: the initial one and the costs of the $K$ updates. By cost, we understand the sum of the costs of the selected roads.

## Constraints and clarifications

$1 < N \leq 200$

$1 < M \leq 10\ 000$

$1 < K \leq 10\ 000$

$1 \leq \text{cost of a road between two cities} \leq 250$

The roads between cities are bidirectional

## Example

`online.in` `online.out`

```
5 7 
1 2 1 
2 3 7 
1 5 5 
3 4 3 
4 5 4 
1 3 2 
2 4 6 
2 3 
5 2 1 
4 3 10 
1 4 3 
3 10 
8 
8 
```