## Task

Johnie wants to break into a bank, where the safes are placed in $N$ adjacent rooms. Thus, the rooms are arranged in the order $0, 1, 2 \dots N - 1$. To be able to find the safes' codes, Johnie needs light. Initially, he knows which rooms have the light on and which don't. Additionally, he knows that some rooms have switches that can change the state of some lights. Being a skilled thief, Johnie has programmed the room switches so that a switch in room $i$ ($0 \le i \le N - 1$) changes both the bulb in that room and possibly some bulbs in rooms after $i$. Moreover, he knows that for each switch $i$ he needs a time $T_i$ to operate it. Knowing the number of rooms, their initial state, the configuration of the switches (programmed by Johnie), and the time required to operate them, you are asked to determine if it is possible, the minimum time in which Johnie can light up all rooms.

## Input Data

The first line of the file `aprindere.in` contains $N$, the number of rooms, and $M$, the number of switches. The next line contains $N$ digits of $0$ or $1$, $0$ representing a room where the light is off and $1$ a room where the light is on. The following $M$ lines first contain 3 numbers $C$, $T_C$, and $NR_C$, representing the room of the switch, the time needed to operate that switch, and the number of rooms whose bulbs are changed by the switch. Following are $NR_C$ numbers representing the indices of the rooms whose bulbs are changed by the current switch (room $i$ will always be in this set).

## Output Data

The file `aprindere.out` contains a single number, with the above meaning.

## Constraints and clarifications

$1 \leq N \leq 1000$

$1 \leq M \leq N$

$1 \leq NR_i \leq 100$

$1 \leq T_i \leq 1000$

There can be at most one switch in a room

For the test data used, there will always be a solution

## Example

`aprindere.in`

```
5 4
0 1 0 0 1
0 3 2 0 2
1 3 2 1 2
3 1 2 3 4
4 2 1 4
```

`aprindere.out`

```
6
```

## Explanation

The switches in rooms $0$, $3$, and $4$ are operated. The total time is $3 + 1 + 2 = 6$.