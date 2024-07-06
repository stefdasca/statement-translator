A worker is entrusted with a difficult mission. He must varnish all the corridors of a castle. For this, he receives a map in which the corridors and the $N$ intersection points of these corridors are represented (numbered from $1$ to $N$). Some intersection points are considered by the worker as "special points" because they are the only points that allow him to exit and enter the castle, through doors.

Because the varnishing operation must be carried out in the shortest time, the worker is required to traverse any corridor only once, meaning only when it is being varnished. Under these conditions, the worker must varnish all the corridors, eventually using the castle's "special points," starting from any corridor intersection he wishes and ending the operation at the same point.

# Task: 

Determine a cyclic route through which the operation is satisfied.

# Input data

The input file `castel.in` contains the following lines:

* The first line contains the number $N$.
* The second line contains the number of corridors $M$.
* The next $M$ lines contain pairs of two numbers representing pairs of points between which there is a corridor that needs to be varnished.
* The next line contains the number $P$ representing the number of "special points."
* The last line contains the string of "special points" separated by spaces.

# Output data

The output will be done in the file `castel.out` in the following format: The first line will contain the message `DA` or `NU`, depending on whether there exists or not a cyclic route that meets the requirements. In the affirmative case, the file will contain on the second line a string of numbers representing the points in the order of appearance on the route, separated after the case by the sequence of characters `-` (space minus space) or `*` (space asterisk space).

A sequence of the type $i$ `-` $j$ means that the worker has traversed and varnished the corridor between points $i$ and $j$.

A sequence of the type $i$ `*` $j$ means that the worker has left the castle through the "special point" $i$ and returned to the castle through the "special point" $j$.

# Constraints and clarifications

* $1 \leq N \leq 5\ 000$;
* $1 \leq M \leq 10\ 000$;
* Half of the tests used for evaluation will have the size $N \leq 100$;
* If there are multiple solutions, any of them will be displayed. 

# Example 1

`castel.in`
```
6
6
1 2
2 3
3 4
4 1
2 5
4 6
5
1 2 5 4 6
```

`castel.out`
```
DA
1 – 2 - 5 * 6 - 4 - 3 - 2 * 4 – 1
```