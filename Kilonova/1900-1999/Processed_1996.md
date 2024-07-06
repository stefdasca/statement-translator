# Task

Gigel and Costel are two experienced policemen. They have been working together for many years and have often been nominated for the "Policemen of the Year" award. This year, they are determined to win it, and to do so, they need to collect as much money as possible from fines.

Each day, Gigel and Costel can issue three types of fines for the following events:

|Type|Description|Collected Amount|Application Duration|
|-|-|-|-|
|1|For pedestrians crossing unlawfully|$S_1$|$T_1$|
|2|For vehicle drivers breaking traffic laws|$S_2$|$T_2$|
|3|For heavy vehicle drivers with illegal cargo transport|$S_3$|$T_3$|

Fines of type 1 and 2 can be issued by a single policeman (either Gigel or Costel). For a fine of type 3, Gigel and Costel need to work together (one checks the transport documents while the other inspects the cargo).

The duration of applying a fine represents the time needed by the policemen to check documents, write the report, etc. If a policeman issues a fine at moment $x$, and the duration of applying the fine is $y$, the policeman who issued the fine will become available again only at moment $x+y$. The policemen do not work overtime; they are on duty from minute $1$ until minute $T$ exclusively, so they must be free to go home at minute $T$. Since the new traffic code no longer allows policemen to stop drivers and make them wait, to issue a fine of type 1 or 2, at least one policeman must be free, and to issue a fine of type 3, both policemen must be free at the moment the event occurs.

The two policemen keep watch and observe traffic events. If they cannot issue fines for all events that occur in traffic, they must choose those that bring them the most money overall.

Write a program to determine the maximum sum they can collect from fines during one shift.

# Input data

The input file `politie.in` contains:
- The first line contains the natural number $T$, representing the minute at which the two policemen are free to go home.
- The second line contains two natural numbers $S_1 \ T_1$ (the amount collected and the duration of applying a type 1 fine).
- The third line contains two natural numbers $S_2 \ T_2$ (the amount collected and the duration of applying a type 2 fine).
- The fourth line contains two natural numbers $S_3 \ T_3$ (the amount collected and the duration of applying a type 3 fine).
- The fifth line contains a natural number $N$ (the number of traffic events).
- Each of the next N lines contains two natural numbers $type$, $time$ ($type$ can be $1$, $2$, or $3$ and represents the type of fine that can be issued; $time$ represents the time at which the event occurred, expressed in minutes from the start of the shift).

The numbers on the same line are separated by a space. The events are in chronological order.

# Output data

The output file `politie.out` contains a single line with the maximum sum that can be collected.

# Constraints and clarifications

* $0 < T, T_1, T_2, T_3 < 201$
* $0 < S_1, S_2, S_3 < 51$
* $0 < N < 501$
* Obviously, there are events that occur simultaneously in traffic.

# Example

`politie.in`
```
300
10 20
30 30
50 25
8
1 5
3 10
3 20
1 130
2 142
2 160
3 180
2 280
```

`politie.out`
```
140
```

## Explanation

Both apply the type 3 fine from minute $10$, then Costel alone applies the type 1 fine from minute $130$, then Gigel alone applies the type 2 fine from minute $142$, then both apply the type 3 fine from minute $180$.