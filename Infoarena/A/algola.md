# Algola

In the Algola organization, an emergency has been declared. All its members, located in different cities around the country, need to reach the headquarters as quickly as possible. The $N$ cities on the country's map are numbered from $1$ to $N$, with city $1$ being the headquarters. The streets connecting the cities are bidirectional, and each street can be traversed in one unit of time by any member of Algola. Each street has a safety limit representing the maximum number of members that can travel on it in one unit of time. Traversing a street can only begin at whole time moments.

## Task

Given the map of the cities and the number of members of the organization in each city, calculate the minimum time $T$ needed for them to reach the headquarters (where $T$ is the moment the last member arrives at the headquarters).

## Input data

The first line of the file `algola.in` contains two integers separated by a space, $N$ and $M$, representing the number of cities on the map and the number of streets between them. The second line contains $N$ numbers separated by spaces $A_1, A_2, \dots, A_N$ where $A_i$ represents the number of members in city $i$. The next $M$ lines contain three integers separated by spaces $X, Y, L$, with the meaning: between cities $X$ and $Y$ there is a street with a safety limit of $L$.

## Output data

The output file `algola.out` will contain a single line with the number $T$ representing the minimum time in which the members of the organization reach the headquarters.

## Constraints and clarifications

$1 \leq N \leq 50$

$1 \leq M \leq 300$

The traversal time of a city is $0$

All members will be able to reach the headquarters

The safety limits of the streets are positive integers in the range $[1,10]$

All members learn about the emergency at moment $0$

The organization has at most 50 members

Members of the organization can stay in any city for an unlimited period

For $20\%$ of the tests, the path from each city to the headquarters is unique; for another $30\%$ of the tests, the total number of members of the organization will be a maximum of $4$

## Example

`algola.in`
```
4 4
0 5 6 5
1 2 3
1 3 5
4 2 2
4 3 5
2
```

`algola.out`
```
2
```