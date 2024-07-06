In the Apuseni Mountains, due to unfavorable weather conditions recently, transportation on public roads has become a problem. Sections of the roads have collapsed, bridges and footbridges have been broken, trees have fallen onto the roads, and many other issues. As a result, groups of houses have been isolated, and people can no longer reach the city to procure their necessities. To reach the city, people have built a cable car that connects isolated regions, which has been designed to be spacious enough so that all people in a station can board at any moment.
For each of the $n$ stations of the cable car, the altitude (measured in meters) and the number of people boarding the cable car at that station are known. It is also known that the cable car consumes $3$ liters/m of fuel when going up and $1$ liter/m of fuel when going down. The distances between stations are practically equivalent to the altitude differences between stations. A station where the type of movement changes from upward to downward or vice versa is called a special station.

# Task

Write a program that determines how many people reach the city with the cable car, what the cable car's fuel consumption for transport is, and how many special stations exist.

# Input data

From the first line of the input file `telecabina.in` read the value $n$, representing the number of stations (including the city). From the next $n$ lines of the input file, read $n$ pairs of natural numbers `a b`, one pair per line, where $a$ represents the station's altitude, and $b$ the number of people boarding the cable car at that station. Between $a$ and $b$ there is exactly one space.

# Output data

The first line of the output file `telecabina.out` will contain the number of people who reach the city. The second line of the output file will contain the cable car's fuel consumption for transport. The third line of the output file will contain the number of special stations.

# Constraints and clarifications

* $1 \leq n \leq 40$;
* $1 \leq a \leq 2\ 000$;
* $0 \leq b \leq 20$;
* The altitudes of any two consecutive stations are different.
* In the last station (in the city), no person boards.

# Example

`telecabina.in`
```
6
1200 3
1204 2
1199 8
1197 0
1202 10
1205 0
```

`telecabina.out`
```
23
43
2
```

## Explanation

In the cable car, board in turn $3$ people, then $2$, then $8$, then $0$, then $10$, a total of $23$ people.

The fuel consumption from station $1$ to station $2$ is $4 \cdot 3 = 12$ liters (ascends $4$ meters), from station $2$ to station $3$ is $5 \cdot 1 = 5$ liters (descends $5$ meters), from station $3$ to station $4$ is $2 \cdot 1 = 2$ liters (descends $2$ meters), from station $4$ to station $5$ is $5 \cdot 3 = 15$ liters (ascends $5$ meters) and from station $5$ to station $6$ is $3 \cdot 3 = 9$ liters (ascends $3$ meters). The total is $43$ liters.

There are $2$ special stations: station $2$, because from station $1$ the cable car ascends, and towards station $3$ the cable car descends, and station $4$, because from station $3$ the cable car descends, and towards station $5$ the cable car ascends.