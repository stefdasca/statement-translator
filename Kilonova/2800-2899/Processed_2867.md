Winter is a profitable season for hotels in Bansko. Their profit is so high that Constanțeanu' thought of building his own hotel. The challenge is quite big because he knows that the hotel foundation will cost $F$ lei, building a floor (ground floor is also considered a floor) will cost $E$ lei, and building a room will cost $C$ lei. He also knows that a floor can have at most $K$ rooms.

The news of the new hotel spread quickly through the city, so fast that Constanțeanu' received $N$ booking offers before he even started construction. For the booking offer number $i$, $i \in \{1, \ldots, N\}$, $T_i$ is known, the number of reserved rooms, and $V_i$, the amount clients are willing to pay for the accommodation. Constanțeanu' has only one problem, namely that if his hotel has fewer than $T_i$ rooms, then he will lose the entire reservation and will not receive any money.

# Task

Constanțeanu' wants to know the maximum profit (the difference between the money spent to build the hotel and the maximum money collected from the reservations) and the minimum number of rooms that yield the maximum profit (as he doesn't want to work more than necessary).

# Input data

The first line of the input file `hotel.in` contains $4$ numbers, in this order and separated by a space: $F$, $E$, $C$, $K$.
The second line contains the number $N$ of received reservations.
The next $N$ lines each contain $2$ numbers, $T_i$ and $V_i$, separated by a space.

# Output data

Print a single line in the output file `hotel.out`, which will contain $2$ numbers separated by space. The first will be the maximum profit, and the second the minimum number of rooms that need to be built to achieve this profit.

# Constraints and clarifications

* $1 \leq N, T_i \leq 1\ 000\ 000$;
* $0 \leq F, E, C, V_i \leq 1\ 000\ 000\ 000$;
* $1 \leq K \leq 1\ 000\ 000\ 000$;
* The maximum profit can be negative (Constanțeanu's business will not have a very happy future);
* Constanțeanu' is very determined, he will build at least one room;
* Although some of the offers received were written for irony (requiring thousands or even millions of rooms), Constanțeanu' will take each offer seriously.

| #   | Score  | Constraints                             |
| --- | ------ | --------------------------------------- |
| 1   | 30     | $N, F, E, C, K, V_i, T_i \leq 1\ 000$   |
| 2   | 20     | $N, T_i \leq 1\ 000$                    |
| 3   | 20     | $F, E=0$                                |
| 4   | 30     | No additional constraints               |

# Example

`hotel.in`
```
50 20 10 5
4
5 90
3 40
7 10
10 30
```

`hotel.out`
```
10 5
```

## Explanation

The cost of building a hotel with $5$ rooms is $50+20+10\cdot5 = 120$ lei (building the foundation, the ground floor, and $5$ rooms).
The revenue of a $5$-room hotel is $90+40=130$ lei (will be able to accept only the $5$-room and $3$-room offers).
This profit is maximum.