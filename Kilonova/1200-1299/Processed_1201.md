On the planet UZABU, a meteor shower will occur. Scientists know that each meteorite is rectangular, having sides parallel to the coordinate axes (and on the planet UZABU, the coordinate axes have the same meaning as on Earth). The soil of the planet is represented by the $OX$ axis. Meteorites fallen on the planet are useful for agriculture. If a falling meteorite touches another meteorite, both will be destroyed, and the resulting crater will destroy the planet's soil. 
Knowing the coordinates of the plates given by four numbers $(x_1, y_1, x_2, y_2)$, with the meaning: **(left_top_x, left_top_y, right_bottom_x, right_bottom_y)**, scientists need to destroy some of the meteorites so that they do not overlap when reaching the soil.

# Input data

The input file `meteor.in` has the structure:
- The first line contains $N$ representing the number of meteorites
- The next $N$ lines each contain four numbers separated by a space, representing the coordinates of the top left and bottom right corners of the rectangular plate.

# Output data

The output file `meteor.out` contains a single value $k$ representing the maximum number of remaining plates.

# Constraints and clarifications

* The number of meteorite plates $N: 0 < N \leq 500$
* The coordinates of each meteorite are integers $0 < x, y \leq 32 \ 000$
* Two plates that stick together when falling do not get destroyed

# Example

`meteor.in`
```
10
5 10 18 2
15 22 27 12
35 30 40 25
43 30 45 25
32 20 45 12
50 20 60 15
20 30 30 25
65 20 82 15
48 13 75 2
78 14 100 3
```

`meteor.out`
```
6
```