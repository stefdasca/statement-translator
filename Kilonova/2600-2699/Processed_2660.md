A group of Olympiad participants are planning to visit the city of Ortogonal located in RUDA (United Kingdom of the Two Axes). Whenever they plan a trip, they study the hotels and restaurants in the city. From previous experiences, they know they will eat a lot of pizza and that walking back from the restaurant to the hotel will be difficult.
Therefore, on the map of Ortogonal city, they plot a Cartesian coordinate system and identify the hotels and restaurants on the map.

The streets in Ortogonal city are either parallel to the Ox axis or parallel to the Oy axis, with the distance between any two consecutive parallel streets being equal to $1$. If they walk from the coordinate point $(x_1, y_1)$ to the coordinate point $(x_2, y_2)$ the distance traveled will be $|x_1 - x_2| + |y_1 - y_2|$. However, when you are stuffed with pizza, you want to walk as little as possible. Therefore, our Olympians will use trams for transport.

The tram lines are on some of the streets, so they are either parallel to Ox or parallel to Oy.

In Ortogonal city, there are no stations; the tram can be taken from anywhere on a tram line and can be exited from the tram anywhere on the tram line.

# Task

Knowing the location of the tram lines in Ortogonal city, write a program to answer $Q$ questions of the following form: "What is the minimum walking distance to travel from the coordinate point $(x_1, y_1)$ to the coordinate point $(x_2, y_2)$?"

# Input data

The input file `tramvaie.in` contains on the first line the natural numbers $N$, $M$ and $Q$, representing the number of tram lines parallel to Ox, the number of tram lines parallel to Oy, and the number of questions, respectively.

The second line contains $N$ integers representing the ordinates where the tram lines parallel to Ox are located.

The third line contains $M$ integers representing the abscissas where the tram lines parallel to Oy are located.

The next $Q$ lines contain 4 integers $x_1$, $y_1$, $x_2$, $y_2$, representing the coordinates of the two points for which we need to determine the minimum walking distance to get from one point to another.

# Output data

The output file `tramvaie.out` will contain $Q$ lines. Each line $i$ will contain a single natural number, representing the answer to the $i$-th question from the input file.

# Constraints and clarifications

* $1 \leq N, M, Q \leq 100\, 000$
* The coordinates of the tram lines and the points between which we travel are integers between $0$ and $10^9$.
* There will not be two tram lines parallel to Ox with the same ordinate.
* There will not be two tram lines parallel to Oy with the same abscissa.
* It is recommended not to use `x1` or `y1` as variable names.

|#| Points | Restrictions                                               | 
|-|---------|------------------------------------------------------------|
|1|   12    | All numbers in the input file are at most $1\, 000$            |
|2|   24    | $N, M, Q \leq 1\, 000$                                          |
|3|    7    | $N = M = 1$                                                    |
|4|   57    | No additional restrictions                                      |

# Example

`tramvaie.in`
```
2 3 4
3 12
10 11 2
1 1 14 14
2 9 7 8
8 2 12 4
6 8 5 7
```

`tramvaie.out`
```
3
3
2
2
```

## Explanation

The city is shown in the figure:

~[ex1.png|width=30em]

Between the red points (the first pair of points from the input file) the minimum walking distance is $3$.

This can be achieved by walking east from $(1, 1)$ to the tram line parallel to Oy located at abscissa $2$ (the walking distance being $1$), then taking the tram to the coordinate point $(14, 12)$ from where you walk north to $(14, 14)$.

Between the blue points the minimum walking distance is also $3$. This can be achieved by taking the tram from $(2, 9)$ (which is on a tram line) to the coordinate point $(10, 8)$ and then walking west to the coordinate point $(7, 8)$.

For the purple points, the minimum distance is $2$ and can be achieved by walking north to the tram line parallel to Ox located at ordinate $3$, then taking the tram to the coordinate point $(12, 3)$ and then walking north to the coordinate point $(12, 4)$.

For the green points, the shortest path that involves the least walking is the one that does not use any trams.

The length is $|6 - 5| + |8 - 7| = 2$.