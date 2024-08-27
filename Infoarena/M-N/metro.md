## Metro

In recent years, the Institute of Compulsive Disorder Research has become overcrowded, discovering and classifying a multitude of strange behaviors. You have been assigned to investigate one of these anomalies spread among innocent people who use the subway. The subway consists of $N$ stations connected by $N-1$ bidirectional paths and $M$ trains with linear routes, each having a unique number. The problem concerns the informational panels located in the station, which display the subway numbers passing through that station in order. One of the patients claims that every time he sees a list of integers $C_0, C_1, \dots, C_L$, he cannot help himself and calculates the sum of the numbers with even indices $S = C_0 + C_2 + C_4 + \dots + C_{2K} + \dots$. Such a list can be seen on each of the informational panels located in the stations. Before any assumptions can be made regarding those affected, we need to calculate the sum for each of the $N$ panels in the stations. Unfortunately, if we calculate them by hand, there is a relatively sure chance that we too may become affected by such a disorder. Thus, you need to write a program that will calculate them for you, protecting your mind from the disorder. Given a number of stations, $N$, the way they are connected, and the $M$ subways, calculate the necessary sum for each station.

## Input data

The file `metro.in` contains two integers on the first line, $N$ and $M$.

The next $N-1$ lines contain two integers $x_i, y_i$ representing the path between stations $x_i$ and $y_i$.

The next $M$ lines describe a subway using three integers $a_i, b_i$ and $o_i$, meaning that the subway numbered $o_i$ goes from station $a_i$ to $b_i$.

## Output data

The file `metro.out` should contain $N$ lines.

Line $i$ contains a single number, namely the sum calculated for station $i$.

If there is no train passing through station $i$, print $0$ on the respective line.

## Constraints

$1 \leq N \leq 200\ 000$

$1 \leq M \leq 200\ 000$

$1 \leq o_i \leq M$ for all $1 \leq i \leq M$

It is guaranteed that you can reach any station from any other station.

## Example

`metro.in`
```
6 4
1 2
2 4
2 6
1 3
5 2
5 6
3 4
5 1
4 3
```

`metro.out`
```
2
4
2
4
2
1
```

## Explanation

The panels display the following numbers:

Station $1$: $2 4$

Station $2$: $1 2 3 4$

Station $3$: $2$

Station $4$: $1 2$

Station $5$: $1 3$

Station $6$: $3$