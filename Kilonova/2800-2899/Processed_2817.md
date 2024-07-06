You have just been hired by the airline company “Brătianu Airlines”. You know that there are $N$ cities indexed from $1$ to $N$ between which the company organizes $M$ flight routes. Each flight route is given by the number of the city from which it takes off, the city in which it lands, the duration, and the price of the flight.
Due to a network overload caused by the congestion in the airport, you must manually find a way to identify flights for passengers.

# Task

For two given cities, $S$ and $F$, you must find:
1. A **path**$^{[1]}$ from city $S$ to city $F$ that has the minimum **duration**$^{[2]}$, if it exists.
2. Among all paths of minimum duration from city $S$ to city $F$, what is the minimum **price**$^{[3]}$ of such a path, if it exists.

$^{[1]}$ We call a **path** from city $U$ to city $V$ a sequence $X_1$, $X_2$, ..., $X_k$, where $X_1 = U$ and $X_k = V$, and for any $i$, with $1 \leq i < K$, there is a flight from $X_i$ to $X_{i+1}$.

$^{[2]}$ We define the **duration** of a path $X_1$, $X_2$, ..., $X_k$ as the sum of the durations of the flights from $X_i$ to $X_{i+1}$, with $1 \leq i < K$.

$^{[3]}$ We define the **price** of a path $X_1$, $X_2$, ..., $X_k$ as the sum of the prices of the flights from $X_i$ to $X_{i+1}$, with $1 \leq i < K$.

# Input data

The first line of the input file `zboruri.in` contains five non-negative natural numbers, in this order: $C$, $N$, $M$, $S$, and $F$, where $C$ represents the number of the task that will be solved, and the rest have the meanings from the description.

The next $M$ lines contain descriptions of the $M$ flights, one flight per line. The $i$-th flight, with $1 \leq i \leq M$, is given by four non-negative natural numbers, in this order:
* $U_i$ - departure city;
* $V_i$ - arrival city;
* $T_i$ - flight duration;
* $P_i$ - flight price.

# Output data

The output file `zboruri.out` will contain in the first line:
* For $C = 1$, the sequence $X_1$, $X_2$, ..., $X_k$, representing a path with **minimum duration** from city $S$ to city $F$, if it exists. If no such path exists, the number $-1$ will be printed.
* For $C = 2$, a single natural number $P_{min}$, representing the **minimum price** among the prices of all paths of minimum duration from $S$ to $F$, if it exists. If no such path exists, the number $-1$ will be printed.

# Constraints and clarifications

* $2 \leq N \leq 2 \cdot 10^5$
* $2 \leq M \leq \min(2 \cdot 10^5, N \cdot (N - 1))$
* $1 \leq U_i, V_i \leq N$, with $1 \leq i \leq M$
* $1 \leq T_i, P_i \leq 10^9$, with $1 \leq i \leq M$
* For the first task, if there are multiple paths of minimum duration, any of them will be awarded points.
* 10 points are given by default.

| # | Point    |                    Constraints               |
|:-:|:--------:|:-------------------------------------------:|
| 1 |    30    |                     $C = 1$                 |
| 2 |    20    | $C = 2$; There is a unique path of minimum duration |
| 3 |    40    |               Without additional constraints    |

# Example 1

`zboruri.in`
```
1 6 8 1 4
1 2 3 3
1 6 1 1
2 3 5 1
2 5 2 2
3 4 3 1
5 4 4 2
6 2 2 1
6 5 4 3
```

`zboruri.out`
```
1 2 5 4
```

# Example 2

`zboruri.in`
```
2 6 8 1 4
1 2 3 3
1 6 1 1
2 3 5 1
2 5 2 2
3 4 3 1
5 4 4 2
6 2 2 1
6 5 4 3
```

`zboruri.out`
```
6
```

## Explanation

The flights in both examples can be graphically represented as follows:

~[zboruri.png|align=left|width=70%]

The circles represent the cities, with their indices inside, and the arrows represent the flights, where the *blue* color indicates the flight duration and the *red* color indicates the flight price.

For the first example, the **minimum duration** of a flight is $9$, and all flights with this duration are:
* $1$, $6$, $5$, $4$;
* $1$, $6$, $2$, $5$, $4$;
* $1$, $2$, $5$, $4$. 

**Any** of these is considered *correct*.

For the second example, the paths of minimum duration above have **prices**:
* $1 + 3 + 2 = 6$;
* $1 + 1 + 2 + 2 = 6$;
* $3 + 2 + 2 = 7$.

Thus the **minimum price** of a path of minimum duration is $6$.