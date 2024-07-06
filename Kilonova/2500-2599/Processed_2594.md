In recent years, the Institute for Compulsive Disorder Research has become overcrowded by discovering and classifying a multitude of strange behaviors. You have been designated to investigate one of these anomalies widespread among innocent people who use the subway.

The subway consists of $N$ stations connected by $N - 1$ bidirectional paths and $M$ trains with linear routes, each having a unique number. The problem refers to the informational boards located in the station where the train numbers passing through that station are displayed in order. One of the patients claims that every time they see a list of integers $C_0, C_1, \dots, C_L$ they cannot help but calculate the sum of the even-indexed numbers $S = C_0 + C_2 + C_4 + \dots + C_{2K} + \cdots$. Such a list can be seen on each of the informational boards located in the stations.

Before any assumption can be made about those affected, it is necessary to calculate the sum for each of the $N$ boards in the stations. Unfortunately, if we calculate them manually, there is a relatively certain chance that we will also be affected by such a disease. Therefore, you must write a program to calculate them for you, so your mind will be protected from the disorder.

# Task

Given a number of stations, $N$, the way they are connected, as well as the $M$ subway trains, calculate the necessary sum for each station.

# Input data

The file `metro.in` contains two integers on the first line, $N$ and $M$. The next $N-1$ lines contain $2$ integers $x_i$, $y_i$ representing the path between stations $x_i$ and $y_i$.

The following $M$ lines describe a subway using three integers $a_i$, $b_i$ and $no_i$ meaning the subway numbered with $no_i$ goes from station $a_i$ to $b_i$.

# Output data

The file `metro.out` must contain $N$ lines. Line $i$ contains a single number, namely the sum calculated for station $i$. If there is no train passing through station $i$, print $0$ on the respective line.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $1 \leq M \leq 200\ 000$
* $1 \leq no_i \leq M$ for all $1 \leq i \leq M$
* It is guaranteed that it is possible to reach any station from any other station.

|#|Score|Constraints|
|-|-|-|
|1|10|$N \le 100$, $M \le 100$|
|2|10|$N \le 5\ 000$, $M \le 5\ 000$|
|3|15|$N \le 100\ 000$, $M \le 1\ 000$|
|4|15|$N \le 1\ 000$, $M \le 100\ 000$|
|5|20|$N \le 100\ 000$, $M \le 100\ 000$|
|6|30|No additional constraints|

# Example

`metro.in`

```
6 4
1 2
2 4
2 6
1 3
5 2
5 6 3
4 5 1
4 3 2
1 2 4
```

`metro.out`

```
2
4
2
1
1
3
```

## Explanation

The boards display the following numbers:

Station $1$: $2, 4$
Station $2$: $1, 2, 3, 4$
Station $3$: $2$
Station $4$: $1, 2$
Station $5$: $1, 3$
Station $6$: $3$