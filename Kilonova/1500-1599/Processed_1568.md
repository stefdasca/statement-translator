We are situated just before the start of the famous Le Mans endurance race. As you know, in an endurance race, the car that covers the greatest distance during the race is considered the winner.

This year, the International Automobile Federation (**FIA**) has made some major changes regarding the conduct of the race. This year the race will last exactly $T$ seconds and $N$ teams will participate, each team having one car, and each car can start from any of the $M$ positions on the starting grid.

Moreover, **FIA** has imposed some rules that have displeased the participating teams:
* Each car is required to move at a constant speed throughout the race. Thus, the $i$-th car will move at a speed of $v[i]$ meters per second.
* If a car starts from position $j$ on the starting grid, it is at a distance of $p[j]$ meters after the starting line, and this distance is considered as already traveled during the race.

# Task

As a sign of protest against the new regulations, the teams have decided to line up on the starting grid so that the maximum difference between the distances covered by any two cars is as small as possible.

# Input data

The first line of the file `lemans.in` will contain 3 numbers:

* $T$ — the duration of the race expressed in seconds;
* $N$ — the number of cars;
* $M$ — the number of starting positions on the grid.

The second line contains $N$ numbers separated by spaces, representing the array $v$ of car speeds.

The third line contains $M$ numbers separated by spaces, representing the array $p$ — the distances from the starting line of the starting positions on the grid.

# Output data

The file `lemans.out` will contain on the first line a single number, representing the minimum possible value of the maximum difference between the distances covered by any two cars. The second line will contain $N$ numbers between $1$ and $M$ separated by spaces, the $i$-th number representing the starting position on the grid of the car number $i$.

# Constraints and clarifications

* $2 \leq N, M \leq 10^3$;
* $1 \leq T \leq 10^3$;
* $1 \leq v[i] \leq 10^6, \forall i \in \{1, 2, \dots, N\}$;
* $0 \leq p[i] \leq 10^9, \forall i, j \in \{1, 2, \dots, M\}$;
* Two or more cars can start from the same position on the starting grid;
* There can be positions on the grid not occupied by any car;
* There can be multiple distributions of cars on the starting grid that offer an optimal solution. Any correct solution is accepted.

|#|Score|Constraints|
|-|-|-|
|1|8|$M = 1$|
|2|9|$M = 2$|
|3|10|$N, M \leq 7$|
|4|19|$v[i] \leq 10^3$ and $p[i] \leq 10^6$|
|5|23|$N, M \leq 100$|
|6|31|no additional constraints|

# Example

`lemans.in`
```
5 4 3
2 3 4 5
7 1 11
```

`lemans.out`
```
5
3 1 2 2
```

## Explanation

The minimum possible distance is $5$ and can be achieved as follows:

* Car $1$ starts from position $3$, hence it will cover $p[3] + v[1] \cdot 5 = 11 + 2 \cdot 5 = 21$ meters;
* Car $2$ starts from position $1$, hence it will cover $p[1] + v[2] \cdot 5 = 7 + 3 \cdot 5 = 22$ meters;
* Car $3$ starts from position $2$, hence it will cover $p[2] + v[3] \cdot 5 = 1 + 4 \cdot 5 = 21$ meters;
* Car $4$ starts from position $2$, hence it will cover $p[2] + v[4] \cdot 5 = 1 + 5 \cdot 5 = 26$ meters.