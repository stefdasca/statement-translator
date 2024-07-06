~[turism.png|align=right]

In the city of Z, there are $n$ tourist attractions, numbered from $1$ to $n$. To help tourists visit the city, the city hall has bought a special bus with $k$ seats, which will go through the $n$ tourist attractions starting from the attraction numbered $1$, then the attraction numbered $2$, $\\dots$, up to the attraction numbered $n$ and then returns to attraction $1$, creating a circular route. At each station, a certain number of passengers are waiting, and for each passenger, we know the number of stations they wish to travel.

Passengers can board the bus only if there are free seats, in the order they are waiting at the station, and those who cannot board leave the station, and at the next stop at that station, other passengers will be waiting. For each station crossed, the ticket cost is $1$ leu. The bus will make, for the last boarding of passengers, one final tour in which passengers only disembark and no one boards. We need to determine the number of complete tours made and the total amount collected for the tours made.

# Task

Determine the values representing the total amount collected and the number of complete tours made.

# Input data

The input file `turism.in` contains on the first line three natural numbers: $n$ (the number of stations), $k$ (the number of seats), and $m$ (the number of stops) separated by a space. The next $m$ lines contain sequences of values representing the number of passengers at that station and for each passenger the number of stations they will travel if there is room in the vehicle, separated by a space.

# Output data

The output file `turism.out` contains on a single line the number that represents the total amount collected and the number of tours made.

# Constraints and clarifications

* $0 < n \leq 200$;
* $n \leq m \leq 10\ 000$;
* $2 < k \leq 100$
* $0 < $ number of stations a passenger travels $ \leq n$
* the bus stops at each station
* at each station, there are at most $k$ passengers

## Example

`turism.in`
```
10 8 16
9 4 2 6 8 1 1 1 3 2
2 1 3
2 1 1
2 1 2
2 10 7
2 10 1
2 2 2
2 2 2
2 2 6
2 4 1
2 4 1
4 3 1 1 1
3 1 1 1
8 5 7 4 10 2 3 2 5
4 1 10 1 1
4 1 1 1 10
```

`turism.out`
```
138 3
```

## Explanation

At the first station, the first $8$ passengers board the bus, at the second station, $3$ disembark (the $3$ who chose to travel only $1$ station) and $2$ board, and so on until all $16$ stops of the bus are completed. The total amount collected is: $138$