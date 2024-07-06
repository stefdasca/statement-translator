A hybrid car moves along a straight road, using alternately either the thermal engine (gasoline) or the electric motor. The axis of integers can be used to describe the coordinates on the road. The car's movement using the electric motor is free of charge, but some portions of the road require the use of the thermal engine, which imposes the payment of certain tolls.

The list of the $P$ tollable portions of the road is known, numbered from $1$ to $P$, **any two of them being disjoint**. Each portion is described by three integers: $st_i$, $dr_i$, and $c_i$ ($1 \leq i \leq P$), meaning that on the portion of the road located between the coordinates $st_i$ and $dr_i$ (including at the ends $st_i$ and $dr_i$), the thermal engine will be used and a toll of $c_i$ lei will be paid. This toll will be paid at each crossing of the portion, regardless of the direction of travel.

The route the hybrid car has to traverse comprises $N$ milestones placed on the road, numbered from $1$ to $N$, in the order they must be visited. For each of the $N$ milestones, the coordinate of its position on the road is known: $x_1, x_2, x_3, \ldots, x_N$. Movement between two consecutive milestones on the route, i.e., between milestone $i$ and milestone $(i+1)$ (for each $i$: $1 \leq i < N$), is made on the shortest path, respectively on the straight segment connecting the points with coordinates $x_i$ and $x_{i+1}$ on the road. **The hybrid car will start the journey from milestone number $1$, meaning from coordinate $x_1$ on the road.** *It is also known that no milestone on the route is located inside or at the ends of the tollable portions, where thermal engine movement is used.*

# Task

To determine:
1. The order number of the tollable portion that will be crossed the most times in the journey (using the thermal engine). If there are multiple such portions, the one with the minimum index will be chosen, according to the order given in the input file. Also, if no tollable portion will be crossed, this number will be $-1$.
2. The total sum, expressed in lei, that needs to be paid to traverse the established route. If no tollable portion will be crossed, then this sum will be $0$.

# Input data

The input file `hibrid.in` contains on the first line three natural numbers, $C$, $P$, and $N$, separated by a space, with the meanings given in the statement. $C$ can have either the value $1$ or the value $2$, depending on the task to be solved. On the next $P$ lines, there are three integers each, separated by a space: $st_i$, $dr_i$, and $c_i$, with the meaning described above. On the next line, there are $N$ integers, separated by a space, representing, in order, the coordinates of the milestones to be visited: $x_1, x_2, x_3, \ldots, x_N$.

# Output data

The output file `hibrid.out` will contain, on the first line, a single integer, depending on the task to be solved. If $C = 1$, then task $1$ will be solved; otherwise, task $2$ will be solved.

# Constraints and clarifications

* $2 \leq P \leq 100 \ 000$ and $2 \leq N \leq 200 \ 000$;
* $-300 \ 000 \leq st_i < dr_i \leq 300 \ 000$ and $1 \leq c_i \leq 100 \ 000$, for each $i$: $1 \leq i \leq P$;
* $-1 \ 000 \ 000 \leq x_i \leq 1 \ 000 \ 000$, for each $i$: $1 \leq i \leq N$;
* Since they have negligible sizes, there may also be two or more milestones located at the same coordinate on the road;
* Throughout the entire route, the thermal engine (gasoline) is used only to traverse tollable portions that the hybrid car must cross. Otherwise, only the electric motor is used, to reduce pollution;
* For tests worth $49$ points, $C = 1$, and for the remaining tests, $C = 2$;
* For $11$ points, the route will not cross any tollable portion;
* For $8$ points, $0 \leq st_i, x_j$ and $dr_i, x_j \leq 70$, for each $i$ and $j$: $1 \leq i \leq P$, $1 \leq j \leq N$;
* For $12$ points, $|x_{i+1} - x_i| \leq 70$, for each $i$: $1 \leq i < N$ and $|x_i| \leq 300 \ 000$, for each $i$: $1 \leq i \leq N$;
* For $40$ points, $P, N \leq 3 \ 000$;
* For $29$ points, no additional constraints.

# Example 1

`hibrid.in`
```
1 2 4
4 8 10
-10 -9 22
-14 20 -14 0
```

`hibrid.out`
```
2
```

## Explanation ($C = 1$)

There are two tollable portions ($P=2$):
* Portion $1$ includes coordinates: $4$, $5$, $6$, $7$, $8$ and has a toll of $10$ lei at each crossing;
* Portion $2$ includes coordinates: $-10$, $-9$ and has a toll of $22$ lei at each crossing.

The route the hybrid car has to traverse consists of $N = 4$ milestones, located at coordinates: $-14$ (first milestone, **from which the journey starts**), $20$ (second milestone), $-14$ (third milestone; note that it is located at the same coordinate as the first milestone!), and $0$ (fourth milestone).
The first tollable portion will be crossed twice, and the second will be crossed three times. Therefore, $2$ will be printed.

# Example 2

`hibrid.in`
```
2 2 4
4 8 10
-10 -9 22
-14 20 -14 0
```

`hibrid.out`
```
86
```

## Explanation ($C = 2$)

According to the above explanation, $86$ will be printed ($2$ crossings $\times 10$ lei/crossing $+ 3$ crossings $\times 22$ lei/crossing $= 86$ lei, i.e., the total sum paid to traverse the route).