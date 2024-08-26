## Task

A Romanian tourist embarked on a trip to the Mediterranean Sea. He arrived in one of the cities on one of the three islands he wants to visit. Each island has exactly $N$ cities and all are ports. The tourist wishes to start his journey from the city he is in, visit all the other $3N-1$ cities exactly once, and then return to the city where he started his journey, so he can then head back home. Unfortunately, on each of the three islands live tribes of cannibals, so it is forbidden by the authorities to travel directly between two cities on the same island. Fortunately, there are sea routes between any pair of cities that are not on the same island. There are no sea routes between two cities on the same island. The tourist wants to know how many ways he can plan his trip across the three islands.

## Input data

The input file `rute.in` contains a single integer $N$, representing the number of cities on each of the three islands.

## Output data

In the output file `rute.out` you must print the number of possible ways to plan the trip. Two trips are considered identical if the sequence of the $3N$ visited cities is identical or if the sequence of cities visited in the first trip is identical to the sequence of cities visited in the second trip but read in reverse (for example, if each island had only one city, numbered with the number of the island, the trips $1-2-3-1$ and $1-3-2-1$ would be identical).

## Constraints and clarifications

$1 \leq N \leq 30$

## Example

`rute.in`
```
2
```

`rute.out`
```
16
```