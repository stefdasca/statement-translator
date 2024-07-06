In the Land of Stuf-Vodă, there exists a metro line with $N$ stations, numbered $1, 2, \dots, N$ placed in a straight line at equal distances, from left to right. MetroStuf has $K$ metros that travel on this line. These metros depart from station $1$ towards station $N$. The travel time of a metro between two consecutive stations is one minute.

However, Stuf-Vodă wants to keep his people as happy as possible, so he wants to find an optimal departure scenario for the metros from station $1$ to station $N$, such that people wait as little as possible. There are given $M$ pairs of the form $(S_i, T_i)$ with the meaning: in station $S_i$ at minute $T_i$ a person arrives. The *cost of a metro* is defined as the longest waiting time of a person who boarded that metro. Stuf-Vodă realized that the people in his land are happier when the *sum of the metro costs* is smaller. A person always boards the first metro that arrives at the station.

# Task
Given $N$, $M$, $K$ and $M$ pairs of the form $(S_i, T_i)$ with the above significance, it is required to calculate the departure times of the metros from station 1 to station $N$, so that the sum of the metro costs is minimized.

# Input data

The first line of the file `metrouri.in` will contain three numbers: $N$, $M$, and $K$ separated by spaces, with the significance from the statement. The following $M$ lines will each contain two numbers, $S_i$ and $T_i$, with the meaning that at time $T_i$ a person arrives at station $S_i$.

# Output data

The file `metrouri.out` will contain a single number, namely the sum of the costs of the $K$ metros.

# Constraints and clarifications

* $1 \leq N, M, K \leq 100\ 000$
* The metros travel only in one direction and once they reach station $N$ they stay there until the end of the day
* For $30\%$ of the tests $N \leq 200, M \leq 1\ 000, K \leq 100$
* For $60\%$ of the tests $N \leq 10\ 000, M \leq 20\ 000, K \leq 300$
* $1 \leq S_i \leq N$
* $0 \leq T_i \leq 1\ 000\ 000$
* MetroStuf opens at minute $0$ (people cannot arrive at stations earlier than this time), but the metros can depart from station $1$ before this moment.
* Any number of people can board a metro.

# Example

`metrouri.in`
```
5 5 3
1 5
2 7
1 8
5 6
4 4
```

`metrouri.out`
```
3
```

## Explanation

Metro $1$ departs from station $1$ at minute $2$, metro $2$ departs at minute $6$, and metro $3$ at minute $8$. The cost of metro $1$ is $1$, the cost of metro $2$ is $1$, and the cost of metro $3$ is $0$. The sum of the costs of the metros is $2$.