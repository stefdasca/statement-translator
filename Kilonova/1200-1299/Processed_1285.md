
An expressway is considered laid out in a straight line with $N$ access points (entrance and exit).

At each access point, there are waste collection containers, all containers have the same capacity and at each access point, there can be multiple such containers. The company responsible for cleaning has only one means of transporting the containers. This means of transport can load exactly $K$ containers.

Access to the expressway by the means of transport is restricted to avoid disturbing the traffic and for this reason, every time it accesses the expressway, it must collect exactly as many containers as the capacity of the vehicle, but from one collection point it must take exactly one container, so if it enters the expressway at access point $P$, where $P \leq N-K+1$, then it must take containers from the access points numbered $P, P+1, P+2, \dots, P+K-1$, in these access points the number of remaining containers decreases by $1$.

The company must find all possible values for $K$ so that it can collect all the containers.

# Task

Find all possible values for $K$ such that all containers are collected.

# Input data

The input file `auto.in` will contain on the first line the natural number $T$, representing the number of data sets.

Next, the data sets will follow, each on two lines. The first line of a set contains the number $N$, having the meaning from the statement.

The next line contains $N$ natural numbers separated by a space, representing the number of containers at each access point.

# Output data

The output file `auto.out` will contain $T$ lines, on line $i$ there will be the answer for the $i$-th data set. The possible values for $K$ will be displayed in ascending order, separated by a space.

# Constraints and clarifications

* $2 \leq T \leq 30$
* $2 \leq N \leq 9\ 000$
* $1 \leq K \leq N$
* $0 \leq$ the number of containers at each access point $ \leq 10\ 000$

# Example

`auto.in`
```
2
8
1 2 3 4 2 0 0 0
3
1 1 1
```

`auto.out`
```
1 2
1 3
```
