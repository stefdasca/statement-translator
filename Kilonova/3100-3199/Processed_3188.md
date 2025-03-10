# First Come, First Served

You are in the Bricodeque store. This store wants to have as many paying customers as possible. Additionally, it wants each customer to spend as little time as possible in line at the checkout.

Starting today, the store wants to implement a new sorting algorithm for customers at the checkout lanes, but it is malfunctioning and you are asked to create another code.

You are given the number of customers the store will have today, a number $N$, and the time at which each customer will arrive at the checkout area. The store has $K$ checkout lanes. Each checkout lane has a limit $LIM$ of people who can stand in line until the customer at the front pays. If a checkout lane is full, it is considered closed until the person at the front pays. If all checkout lanes are closed, the customer will leave for another store. This is undesirable, so we must do everything possible to have as few customers as possible leave the store.

Each customer will be in line for $T$ seconds until they pay. If there are $P$ people in front of them, they will wait until their turn at the checkout counter. Only when they are first in line will the $T$ seconds start.

# Input data

The first line contains $4$ numbers: $N$, $K$, $T$ and $LIM$, with the meanings described above. Then there will be $N$ lines, where for each customer $i$, $i=\overline{1,N}$, the time they arrive at the checkout area is given.

# Output data

On the first line, there will be $2$ numbers: the first is the maximum number of customers who have paid, and the second is the time at which the last customer left the line. On the next $N$ lines, there will be $2$ numbers: the index of the customer in the given order, and the checkout lane they lined up at. If all checkout lanes are closed, -1 will be printed.

# Constraints and clarifications

* $N \leq 100 \ 000$
* $K \leq 10 \ 000$
* $LIM \leq 100$
* $T \leq 100$
* The time at which a customer arrives at the checkout area $\leq 1 \ 000$
* If there are multiple customers arriving at the same time at the checkouts, priority will be given to the one with the smaller index when reading.
* If a customer $X$ can only enter one checkout, and the person in front of them leaves at the same time, then customer $X$ can line up.

# Example 1

`stdin`
```
10 2 3 2
1
1
1
2
3
3
4
5
5
7
```

`stdout`
```
7 13
1 1
2 2
3 1
4 2
5 -1
6 -1
7 1
8 2
9 -1
10 1
