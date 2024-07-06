A fifth-grade student, Rareș, decided to study the train schedules passing through the train station in his city, for one day. The station has $2$ tracks, numbered $1$ and $2$, on which trains arrive and depart. On that day, $T$ trains arrive at the station. For each of these $T$ trains, Rareș knows the track $L$ on which it will arrive, the arrival time, i.e., the hour $H$ and the minute $M$, as well as the duration $S$ of the stop (expressed in minutes). He decided that the study period of the $T$ trains will begin at the arrival time of the first train at the station and will end at the departure time of the last train of these $T$.

From the waiting room, Rareș can see both tracks. However, Rareș has a problem: when a train is at the station on track $1$, he cannot see the train stopped at the same time on track $2$. For example, if a train arrives at the station on track $1$ at $14:21$ and stops for $5$ minutes, then the train will depart the station at $14:26$. Thus, during the time interval [$14:21-14:26$], Rareș cannot see what happens on track $2$. The train on track $2$ will become visible starting with the next minute, i.e. from $14:27$.

# Task

Write a program that determines for a number $T$ of trains passing through the station during the study period on that day:

* the maximum number of trains $Z$ that have stopped on the same track;
* the number $X$ of trains that Rareș sees;
* the maximum duration $Y$ (expressed in consecutive minutes), over the study period, during which Rareș did not see any train.

# Input data

The input file `tren.in` contains on the first line the number $T$ of trains, and on each of the following $T$ lines, in the order of the trains' arrival at the station, four natural numbers $L$, $H$, $M$, and $S$, separated by a space, representing the track $L$ the train arrives on, the arrival time (hour $H$ and minute $M$), and the stop duration $S$.

# Output data

The output file `tren.out` contains on the first line, separated by a space, the required values $Z$, $X$, and $Y$ (in this order).

# Constraints and clarifications

* $2 \leq T \leq 100$; $0 \leq H \leq 23$; $0 \leq M \leq 59$; $1 \leq S \leq 9$;
* At the same time, multiple trains cannot arrive/depart;
* At the same time, a train cannot depart and another arrive;
* On the same track, multiple trains cannot stop at the same time;
* For finding the correct number $Z$, 20% of the points are awarded for each test;
* For finding the correct number $X$, 40% of the points are awarded for each test;
* For finding the correct number $Y$, 40% of the points are awarded for each test.

# Example

`tren.in`
```
8
1 14 20 3
2 14 21 1
2 14 24 4
1 14 40 8
2 14 41 1
2 14 43 1
2 14 45 5
1 14 56 1
```

`tren.out`
```
5 5 11
```

## Explanation

On track $1$, $3$ trains have stopped, and on track $2$, $5$ trains have stopped, thus $Z = 5$.

At $14:20$, Rareș sees the train arriving on track $1$ and it will stop until $14:23$. He does not see the train arriving on track $2$ at $14:21$ and departing at $14:22$. He sees the train arriving on track $2$ at $14:24$ because, at the moment of arrival, no train is on track $1$. Also, he sees the train arriving at $14:40$ on track $1$, but does not see the next $2$ trains arriving on track $2$ because the train on track $1$ departs at $14:48$. He also sees the last train on track $2$ as it arrives before the train on track $1$ departs and leaves after it. In total, he has seen $5$ trains.

In the time intervals [$14:29-14:39$] and [$14:51-14:55$], Rareș does not see any trains, the maximum duration being $11$ minutes (determined by the train departing at $14:28$ and the next train arriving at $14:40$).