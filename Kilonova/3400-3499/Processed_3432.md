Young ninja Enaz is preparing for the grand finale of shuriken throwing. Depending on the distance the shurikens reach as a result of the throws, competitors receive points. The scoring area is defined by $M$ consecutive, adjacent subzones, each having different lengths and point values. Thus, if a competitor throws a shuriken to a distance covered by a scoring subzone $x$, he will receive $x$ points. However, if the distance is not covered by any subzone, his score will remain unchanged. If the shuriken is on the boundary of a subzone, it is considered to belong to that subzone. However, if a shuriken is on the boundary between $2$ subzones, it is considered to belong to the subzone at a greater distance from the origin. A few hours before the start, Master Uw has a vision. He knows exactly the distances from the origin that the $N$ shurikens thrown by Enaz will reach. With this information, he wonders: Where should the scoring area begin so that Enaz can achieve the highest possible score, and what is this score?

# Task

Display the distance from the origin to the start of the scoring area that gives Enaz the most points, and this maximum number of points. If there are multiple such distances, display the smallest one.

# Input Data

The first line contains the test group number to which the test belongs.  
The second line contains two natural numbers, $N$ and $M$.  
The third line contains $N$ natural numbers, $a_i$ where $1 \le i \le N$, representing the distances from the origin reached by the shurikens thrown by Enaz.  
The next $M$ lines contain two numbers each, one natural number $d_i$ and one integer $p_i$ where $1 \le i \le M$, representing the distance and point value of each subzone in order from the closest to the farthest from the origin.

# Output Data

The first line will contain two numbers, one natural and one integer representing the distance and score required by the task.

# Constraints and Clarifications

* $1 \le N, \ M \le 10^3$
* $1 \le a_i \le 10^{18}$
* $|p_i|, \ d_i \le 10^{15}$
* The distance from the origin to the start of the scoring area $\ge 0$, in other words, the scoring area cannot start before the origin.
* The test groups are as follows:

| #   | Points | Constraints                                                                                |
| --- | ------- | ----------------------------------------------------------------------------------------- |
| 0   | 0       | Example                                                                                   |
| 1   | 7       | $p_i < 0$                                                                                 |
| 2   | 11      | $N=1$                                                                                     |
| 3   | 13      | $M=1$                                                                                     |
| 4   | 39      | $a_i, \ d_i, \ |p_i| \le 10^3$											         |
| 5   | 30      | No additional constraints                                                                 |

# Example

`stdin`
```
0
6 4
8 11 12 5 9 4
2 4
1 -5
3 2
1 3
```

`stdout`
```
4 15
```

## Explanation

~[poza.png|align=left|width=40%]

As seen in the image, if the scoring area starts at distance $4$, then the shurikens at distances $4$ and $5$ will each bring $4$ points, shurikens at distances $8$ and $9$ will each bring $2$ points, the shuriken at distance $11$ will bring $3$ points, and the shuriken at distance $12$ will bring no points as it is outside the scoring area. The total score is 15, this being the maximum.