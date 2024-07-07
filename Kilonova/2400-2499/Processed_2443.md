
# Task
Gigi is passionate about car rides. He loves driving between $N$ cities. These cities are connected by roads of known length. The roads are bidirectional (if there's a road of $5$ km from city $A$ to $B$, then the same road can be used from $B$ to $A$). Even though Gigi is passionate, he does not want to spend all day driving. For this, he found the following solution: he wants to find for each city the shortest interesting route he can take. An interesting route is defined as a route that starts from a city, let's call it $A$, and returns to the same city $A$, but without traveling the same road twice.

Knowing $N$ – the number of cities, $M$ – the number of roads, and the description of the $M$ roads in the format ($u$, $v$, and $k$ – representing a road from $u$ to $v$ with cost $k$), you are required to help Gigi find the shortest interesting route he can take from each particular city.

# Input data

The first line of the input file `plimbare.in` contains $N$ and $M$.
The next $M$ lines contain three numbers $u$, $v$, and $cost$, representing the description of each edge.

# Output data

The first line of the output file `plimbare.out` will contain $N$ numbers, representing the minimum length of an interesting route for each city. If there is no interesting route for a city, then for that city print `-1`.

# Constraints and clarifications

* For $30\%$ of the tests, $N \leq 10$ and $M \leq 15$;
* For $100\%$ of the tests, $N \leq 2\ 000$ and $M \leq 30\ 000$;
* The cost of a route will not exceed $1\ 000\ 000\ 000$;
* The cities are numbered from $0$ to $N - 1$.

# Example

`plimbare.in`
```
5 7        
0 1 5
0 2 4
1 2 14
1 4 1
4 2 4
4 3 2 
2 3 1
```

`plimbare.out`
```
13 13 7 7 7
```

## Explanation

For node $0$, the interesting route with the minimum length is `0-2-3-4-1-0` with length $13$.
For node $1$, the interesting route with the minimum length is `1-4-3-2-0-1` with length $13$.
For node $2$, the interesting route with the minimum length is `2-3-4-2` with length $7$.
For node $3$, the interesting route with the minimum length is `3-2-4-3` with length $7$.
For node $4$, the interesting route with the minimum length is `4-3-2-4` with length $7$.
```
