# King Gefghev's Journey

King Gefghev faces a new problem of national interest. The kingdom he rules contains $N$ cities, numbered from $1$ to $N$, connected by $N-1$ bidirectional paths. Each path has a certain length expressed in meters. Between any two cities, there is at most one path, and it is possible to travel from any city to any other city using only the existing paths. King Gefghev enjoys traveling, so he takes a $M$-day vacation and plans to arrange $M$ journeys. At the beginning of each day, Gefghev chooses a starting city $x$ and wants to travel, starting from that city, a path of maximum length. The path the king takes is actually a sequence of distinct cities $(a_1, a_2, a_3, \dots a_{k-1}, a_k)$ such that there is a path between any two cities $a_i$ and $a_{i+1} (i < k)$ and $a_1 = x$. The length of the path is given by the sum of the lengths of the paths that make it up. Since he doesn't want to get bored, King Gefghev wants to travel a different path each day. Two paths $d_1 = (a_1, a_2, a_3, \dots a_{k-1}, a_k)$ and $d_2 = (b_1, b_2, b_3, \dots b_{p-1}, b_p)$ are different if:

* $k \neq p$, or
* $k = p$ and there is at least one position $q$ such that $a_q \neq b_q$.

# Task

Write a program that determines the length of the path traveled by King Gefghev in each of the $M$ journeys.

# Input data

The input file `regat.in` contains:
- The first line contains two integers $N$ and $M$ separated by a single space, with the meaning described above.
- The next $N-1$ lines each contain three numbers $a$, $b$ and $c$ separated by a single space, indicating that there is a path from city $a$ to city $b$, and this path has a length of $c$ meters.
- The next $M$ lines each contain a number between $1$ and $N$, on the line $N+1+i$ containing the city from which the king begins his $i$-th journey.

# Output data

The output file `regat.out` will contain $M$ natural numbers, where on line $i$ will contain the length of the path traveled by the king in the journey of day $i$.

# Constraints and clarifications

* $1 \leq N, M \leq 100 \ 000$
* The lengths of the paths are natural numbers in the range $[1, 10 \ 000]$
* The king can start multiple journeys from the same city
* The king will always have the possibility to carry out all the journeys
* For $20\%$ of the tests $N \leq 700$
* For $40\%$ of the tests, each journey starts from a different city

# Example

`regat.in`
```
8 5
1 2 3
2 3 5
3 4 14
2 6 3
2 7 9
7 8 10
5 6 20
1
2
1
4
3
```

`regat.out`
```
26
23
22
42
28
```

## Explanation

The first journey starts in city $1$ and ends in city $5$. The length of the path is $26$. There is no other city at a strictly greater distance than $26$. The second time the king starts a journey from city $1$, it can end in either city $4$ or $8$, with the length of the road being $22$.