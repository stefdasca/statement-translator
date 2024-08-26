# Patrol

A country has $N$ cities and $M$ direct, bidirectional connections between these cities. Each city charges a known accommodation fee. A criminal starts from the city numbered $1$ and wants to reach the city numbered $N$, using the existing connections. As things are never that simple, there are also $P$ policemen who are searching for him. A policeman has a well-defined patrol route. His route is actually a simple path (where all cities are distinct). He will travel back and forth on this path, meaning he starts on the defined path, then returns on the same path, and so on. For example, if a policeman's patrol route is $4 7 5$, he will always travel on $4 7 5 7 4 7 5 7 4 \dots$. Traveling on a connection between any two directly connected cities takes one unit of time, for both the criminal and any of the policemen. Staying in a city does not require additional time. The criminal starts from the city numbered $1$ and desires to reach the city numbered $N$, paying a minimum fee for staying in the cities he passes through, avoiding meeting any policeman. A meeting can occur when the criminal and one of the policemen are in the same city at the same time, or on the same connection between cities at the same time. Departure from city $1$ occurs at moment $1$, when all the policemen begin their patrol.

## Task

Determine the minimum total accommodation cost in cities in order to fulfill the specified conditions.

## Input data

The input file `patrol.in` has the following structure:

$N$ $M$ $P$

$C[1]$ $C[2] \dots C[n]$

$A[1]$ $B[1]$

$A[2]$ $B[2]$

$\dots$

$A[M]$ $B[M]$

$L[1]$ $T[1,1] \dots T[1,L[1]]$

$L[2]$ $T[2,1] \dots T[2,L[2]]$

$\dots$

$L[P]$ $T[P,1] \dots T[P,L[P]]$

the number of cities, connections, and policemen

the accommodation costs for each city

the line $A[i]$ $B[i]$ indicates that there is a direct connection between cities $A[i]$ and $B[i]$

the first number on the line indicates the length of the patrol route, followed by the actual description of the route

In total, the input file contains $M+P+2$ lines.

## Output data

The first line of the output file `patrol.out` contains the minimum cost paid. It is guaranteed that there is always a solution.

## Constraints and clarifications

$3 < N \leq 1\ 024$

$4 < M \leq 16\ 000$

$P \leq 512$

$2 \leq L[i] < 8$

The accommodation costs are natural numbers in the range $[1, 1\ 600]$

At any moment, the criminal must keep moving (he cannot stay in the same place)

The total cost will also include the fees charged in the departure and arrival cities

It is possible for more than one policeman to be in the same city at the same time

## Example

`patrol.in`

```
7 6 1
10 4 9 1 2 5 2
1 2
2 3
2 4
2 6
4 5
6 7
5
7 6 2
4 5
```

`patrol.out`

```
34
```

## Explanation

The criminal's path is $1 2 3 2 6 7$. It is observed that, for example, at time $2$, the criminal cannot head towards city number $6$ because he would meet the policeman on the connection between cities $2$ and $6$. Additionally, if he headed towards city number $4$, he would eventually be caught by the policeman.