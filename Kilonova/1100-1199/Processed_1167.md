
~[img.png|align=right|width=20em]

A country has $N$ cities, numbered from $1$ to $N$, arranged in a circle. PAM has just obtained her driver's license and wants to visit all the cities in the country. PAM is afraid to drive through crowded places, so she decided to drive only on the roads with less traffic. There are connecting roads between any two adjacent cities: between city $1$ and city $2$, ..., between city $i$ and city $i+1$, and city $N$ is connected to city $1$.

To avoid getting lost, PAM decided to choose a starting city and travel on those roads in a counter-clockwise direction until she returns to the city she started from. If PAM starts from city $K$, then her route will be: $K, K+1, \ldots, N, 1, 2, \ldots, K$.

PAM's car has a very large tank (in which she can put as much gasoline as she wants). In each city, PAM takes all the gasoline available in the city, and traveling each road requires a certain amount of gasoline.

# Task

Knowing that PAM has, at the beginning of the journey, only the gasoline available in the starting city, and that, when she arrives in a city, she will take all the gasoline available in that city, find a city from which PAM can start her trip so that she does not run out of gasoline.
It is considered that PAM ran out of gasoline if, at the time of departure from a city, she does not have enough gasoline to travel the road leading to the next city. If the gasoline is exactly enough (i.e., at departure she has just as much gasoline as she needs), it is considered that PAM can reach the next city.

# Input data

The input file `masina.in` contains on the first line the number $N$.

The second line contains $N$ natural numbers $a_1, a_2, \dots, a_N$, separated by spaces, where $a_i$ represents the amount of gasoline available in city $i$.

The third line contains a sequence of $N$ natural numbers $b_1, b_2, \dots, b_N$, separated by spaces, where $b_i$ represents the amount of gasoline needed to travel the road between cities $i$ and $i+1$ (or $N$ and $1$ if $i=N$).

# Output data

The output file `masina.out` will contain a single number $s$ which represents a city from which, if PAM starts her trip, she can complete the tour of the country without running out of gasoline.

# Constraints and clarifications

* $3 \leq N \leq 30 \ 000$
* $0 \leq a_i \leq 30 \ 000$
* $1 \leq b_i \leq 30 \ 000$
* If there are multiple solutions, only one is required.

# Example

`masina.in`
```
6
0 3 2 5 10 5
7 8 3 2 1 4
```

`masina.out`
```
4
```
