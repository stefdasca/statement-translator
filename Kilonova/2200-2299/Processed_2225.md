
The natives from the island BuruBuru have just discovered asphalt, so they have connected their $N$ villages (numbered from $1$ to $N$) through $M$ bidirectional roads, each with a given length.

Seeing these technological advances, some colonists decided they want to take control of the island. They start from the village with index $S$ (the place where they landed) and head towards the capital city of the natives, the city $D$, traveling the route of minimal length (the sum of the lengths of the roads forming the route should be minimal).

# Task

The natives want to delay the attack of the colonists, so they want to know the minimum number of roads whose length needs to be increased by at least one unit so that the length of the route from city $S$ to city $D$ increases by at least one unit. Since the natives have not yet discovered the computer, it is your duty to help them!

# Input data

The first line of the file `asfalt.in` contains four numbers $N$, $M$, $S$ and $D$ with the above meanings. The next $M$ lines each contain three numbers $x$, $y$, $c$, each indicating that there is a road between cities $x$ and $y$ of length $c$.

# Output data

The file `asfalt.out` will contain on the first line the minimum number of roads whose length needs to be increased. The following lines will each contain two natural numbers, representing the indices of the cities describing one of the roads that need to be increased.

# Constraints and clarifications

* $1 \leq N \leq 500$
* $1 \leq M \leq 5\ 000$
* $1 \leq c \leq 10^6$
* $1 \leq x, y \leq N$
* any solution that has a minimum number of roads is accepted
* there will be no multiple roads between two cities

# Example

`asfalt.in`
```
4 4 1 4
1 2 1
1 3 2
2 4 2
3 4 1
```

`asfalt.out`
```
2
1 2
1 3
```
