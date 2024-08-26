# Interplanetary Journey

A spaceship needs to travel from planet $1$ to planet $2$, then from planet $2$ to planet $3$, and so on until it reaches planet $N$. When traveling from planet $K$ to planet $K+1$, the spaceship has two options: normal speed or hyperspeed. Using normal speed, the travel time from planet $K$ to planet $K+1$ is $N_k$ time units. Using hyperspeed, the travel time between planets $K$ and $K+1$ is $H_k$ time units. The pilot of the spaceship is interested in consuming as little fuel as possible during the voyage. He knows that the formula for fuel consumption is: $N_{TOTAL} + \frac{H_{TOTAL}}{4}$, where $N_{TOTAL}$ is the total time units at normal speed, and $H_{TOTAL}$ is the total time units at hyperspeed. For example, suppose there are $5$ planets. From planet $1$ to planet $2$ the spaceship travels $60$ time units using normal speed. From planet $2$ to planet $3$ the spaceship travels $3$ time units using hyperspeed. From planet $3$ to planet $4$ the spaceship travels $40$ time units using normal speed. From planet $4$ to planet $5$ the spaceship travels $7$ time units using hyperspeed. $N_{TOTAL} = 60 + 40 = 100$ and $H_{TOTAL} = 3 + 7 = 10$. The fuel consumption is $100 + \frac{10}{4} = 102.5$.

## Task

Determine the minimum fuel consumption needed for the journey from planet $1$ to planet $N$.

## Input Data

The first line of the input file `calatorie.in` contains the number of tests $T$. The following lines describe the $T$ tests. The first line of each test contains the number of planets $N$. The next $N-1$ lines contain $2$ integers, $N_k$ and $H_k$, for $K = 1, 2, \dots, N-1$.

## Output Data

For each test, print in the output file `calatorie.out` a single line that respects the following format: Minimum consumption = $XXX.$, where $XXX$ should be replaced by the number found by your program.

## Constraints and clarifications

$1 \leq N \leq 50$

$1 \leq T \leq 155$

$1 \leq N_k \leq 10^8$

$1 \leq H_k \leq 10$

## Example

`calatorie.in`  
```
2
4
1000 3
5000 2
8000 4
6
10000 1
3547 2
36782 7
2178 4
67428 9
```

`calatorie.out`  
```
Minimum consumption = 2296.
Minimum consumption = 52507.
```