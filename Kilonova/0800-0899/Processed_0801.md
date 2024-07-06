The Institute of Earth Physics studies the effects of a potential earthquake using computer simulations. The flat map of buildings in a certain territory is represented using GPS coordinates on a plane, longitude, and latitude, relative to a reference point considered to have coordinates ($0, 0$), as shown in the figure below.

Each building on the map has two GPS coordinates, (Longitude, Latitude) and a degree of earthquake resistance.
An earthquake can occur at any point on the map, called the earthquake center, and has a certain intensity. The shock wave propagates in the form of concentric squares with the earthquake center, called levels (level $0$ represents the earthquake center, level $1$ the first concentric square, level $2$ the second concentric square, and so on). The intensity weakens at each concentric square from the earthquake center by one unit. Buildings are affected by the earthquake only if their degree of earthquake resistance is less than or equal to the earthquake intensity at the building's position.

~[cladiri.png]

# Task

Write a program that reads the coordinates of the earthquake center and its intensity at that point, as well as the coordinates of the buildings and their degree of earthquake resistance, and then determines the total number $N$ of affected buildings; the maximum number $M$ of buildings affected at one level; the numbers of the levels with $M$ buildings affected, in ascending order of these levels.

# Input data

The input file `cladiri.in` contains in the first line, three natural numbers $Long \\ Lat \\ Intensity$, separated by a space, representing the coordinates of the earthquake center and its corresponding intensity. Each of the subsequent lines, until the end of the file, contains three natural numbers $Long \\ Lat \\ Grad$, separated by a space, representing the coordinates of a building, and its degree of earthquake resistance.

# Output data

The output file `cladiri.out` will contain three lines. The first line will contain the natural number $N$ representing the total number of affected buildings. The second line will contain the natural number $M$ representing the maximum number of buildings affected at one level. The third line will contain the numbers of the levels with $M$ buildings affected, in ascending order of these levels.

# Constraints and clarifications

* $0 \\leq$ Long, Lat, Grad, Intensity $\\leq 10 \\ 000$;
* $0 <$ number of buildings $\\leq 100 \\ 000$;
* Buildings can be located at the earthquake center.
* There are no multiple buildings with the same coordinates.
* $52$% of the score can be obtained on input tests with $0 \\leq Long, Lat, Grad, Intensity \\leq 100$
* Partial scores are awarded from the score assigned to each test, as follows: $25$% for requirement a), $25$% for requirement b), and $50$% for requirement c).

# Example 1

`cladiri.in`
```
12 7 11
10 9 2
10 7 3
13 5 1
8 11 4
8 7 6
15 4 3
15 9 10
13 10 1
16 8 4
```

`cladiri.out`
```
8
3
2 4
```

## Explanation

The total number $N$ of affected buildings is $8$.

The maximum number $M$ of buildings affected at the same level is $3$, and it is reached at levels $2$ and $4$.

# Example 2

`cladiri.in`
```
3 3 3
1 3 5
2 4 7
3 2 9
```

`cladiri.out`
```
0
0
```

## Explanation

The earthquake intensity is $3$ and it cannot affect the $3$ buildings, so we have $N=0$ affected buildings, and the maximum number of buildings affected at one level is obviously $M=0$.