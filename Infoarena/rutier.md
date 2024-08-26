# Road Transport

The Minister of Transport, Braian Tasescu, has come to the conclusion that he needs to increase his popularity in order to aspire to the position of the country's president. Therefore, he wants to establish a program that ensures the best possible maintenance of a vital road transport system for the country. For now, he is interested in the most important $N$ cities of the country and wants the transport system to consist of $N-1$ roads so that each city is connected to the capital (the city indexed $1$) and the total maintenance cost of the roads is as low as possible. Although he initially found the optimal transport system, in the future $M$ new roads will be built between the $N$ cities, so it is often better to modify the system so that its maintenance cost is minimized.

## Input data

The first line of the input file contains the integer number $N$, and in each of the following $N-1$ lines there will be information about the initial system, with line $i$ containing two integers $K$ and $C$, representing the nearest city to the capital to which city $i$ is connected and the annual maintenance cost of the road that connects the two cities respectively. If a city is directly connected to the capital, then $K=1$. Line $N+1$ contains the number $M$, and the following $M$ lines contain 3 integers $X$, $Y$, $C$, which indicate that a road has just been built between cities $X$ and $Y$ with an annual maintenance cost of $C$.

## Output data

The output file will contain $M$ lines, with line $i$ containing an integer representing the maintenance cost of the system after $i$ more roads have been built.

## Constraints and clarifications

$1 \leq N \leq 50\ 000$

$1 \leq M \leq 150\ 000$

the annual maintenance cost of any road is a natural number at most equal to $1\ 000\ 000$

## Example

`rutier.in`

```
9 
1 4
2 6
1 10
3 6
3 7
5 2
2 3
2 6
6 
8 4 3
3 1 3
8 1 3
3 7 6
6 7 4
5 2 2
```

`rutier.out`

```
37 
34 
33 
33 
30 
26 
```