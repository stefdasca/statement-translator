The lock is a hydro-technical construction arranged on the route of a navigable waterway, which ensures the passage of vessels between two bodies of water with different levels. A lock consists of a basin called the "sas" or "lock chamber", equipped at both ends with watertight gates and a powerful pumping system for filling or emptying the sas to the desired level. Romanian specialists have built a succession of $N$ locks numbered from $1$ to $N$ on the navigable course of the Danube, which ensure optimal navigation conditions in dry seasons. Thus, if a vessel is at a certain moment in lock $i$ and the water level in the lock differs from the water level in lock $i + 1$, to continue navigating in optimal conditions, either the water level in lock $i$ is adjusted to the level of lock $i + 1$ or the water level in lock $i + 1$ is adjusted to the level of lock $i$.
For example, if for a navigable sector there are $9$ locks for which the water level is as follows:
| Lock      | Water level |
| --------- | ----------- |
| $1$       | $2$         |
| $2$       | $2$         |
| $3$       | $4$         |
| $4$       | $1$         |
| $5$       | $2$         |
| $6$       | $2$         |
| $7$       | $1$         |
| $8$       | $2$         |
| $9$       | $2$         |

the minimum number of locks where water level adjustments are required is $3$, as follows:
* the level in lock $3$ is lowered to level $2$
* lock $4$ is filled to level $2$
* lock $7$ is filled to level $2$

# Task

Knowing the water level in the $N$ locks, determine the minimum number of water level adjustments in the locks that allow a passage through all locks.

# Input data

The input file `ecluze.in` contains on the first line the natural number $N$ which represents the number of locks. The next line contains $h_1, h_2, \dots, h_N$ natural values separated by a space, representing the water level corresponding to each lock.

# Output data

The output file `ecluze.out` will contain on a single line a natural number $M$ representing the minimum number of water level adjustments in the locks that allow a passage through all locks.

# Constraints and clarifications

* $2 \leq N \leq 100\ 000$
* $1 \leq h_i \leq 1\ 000$ ($h_i$ – water level of lock $i$)
* for $20\%$ of the tests, $N \leq 30$

# Example

`ecluze.in`
```
9
1 2 3 3 2 1 1 2 3
```

`ecluze.out`
```
6
```

## Explanation

- lock $1$ is filled to level $2$
- lock $2$ is filled to level $3$
- the level in lock $4$ is lowered to level $2$
- the level in lock $5$ is lowered to level $1$
- lock $7$ is filled to level $2$
- lock $8$ is filled to level $3$