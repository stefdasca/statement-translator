In the mountain camp, a cross-country skiing competition was organized. All competitors covered the same distance and started at the same moment. At the start, $n$ competitors lined up, and for each competitor, the time taken to complete the route, expressed in minutes and seconds, is known.

The start time, including hour, minute, and second, is also known.

# Task

Write a program that determines the hour, minute, and second at which the first competitor reaches the finish line and the hour, minute, and second at which the last competitor reaches the finish line.

# Input data

The input file `schi.in` contains:

* The first line contains 3 natural numbers, separated by a space, representing the hour, minute, and second at which the start was given
* The second line contains the natural number $n$ representing the number of competitors
* The following $n$ lines will each contain two natural numbers $m$ and $s$, separated by a space, representing the time taken by each competitor, expressed in minutes and seconds

# Output data

The output file `schi.out` will contain two lines:

* The first line will contain three natural numbers, separated by a space, representing the hour, minute, and second of the arrival of the competitor who reached the finish line first
* The second line will contain three natural numbers, separated by a space, representing the hour, minute, and second of the arrival of the competitor who reached the finish line last

# Constraints and clarifications

* $1 < n < 100$;
* The start will be given between 8:00 and 20:00;
* $0 \le m < 60$;
* $0 \le s < 60$.

# Example

`schi.in`
```
10 50 3
5
10 20
12 15
8 58
15 3
10 12
```

`schi.out`
```
10 59 1
11 5 6
```

## Explanation

Start time: hour $10$, $50$ minutes, and $3$ seconds.

There were $5$ skiers.

The competitor who reaches the finish line first is the skier who completed the route in $8$ minutes and $58$ seconds and crossed the finish line at: hour $10$, $59$ minutes, and $1$ second.

The competitor who reaches the finish line last is the skier who completed the route in $15$ minutes and $3$ seconds and crossed the finish line at: hour $11$, $5$ minutes, and $6$ seconds.