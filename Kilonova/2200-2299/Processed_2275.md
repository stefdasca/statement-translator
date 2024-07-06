After the New Year's Eve party, Armando and his friends go for a walk in the forest and arrive at an area where excavations for minerals are being conducted. They decide to place the following bet: the one who digs the area with the most minerals will receive all the minerals they find that morning. Armando, being a cunning boy, thinks of asking for your help, which is why he provides you with the following information about the area where he wants to dig:

* The area has the shape of a parallelepiped with width $l$, length $L$, and height $H$, and is divided into $l \cdot L \cdot H$ cubes of $1 \text{ m}^3$;
* Initially, they consider that each cube of $1 \text{ m}^3$ contains $0$ minerals, after which they conduct $Q_1$ tests and find out, sequentially, new information about the number of minerals in an analyzed parallelepiped subzone. Specifically, following an analysis, the known number of minerals in each cube of the respective subzone increases by a value $v$.

# Task

Armando has $Q_2$ subzones about which he wants to know whether they are worth digging, so he wants to know how many minerals he would obtain from each. A subzone is (uniquely) determined by two diagonally opposite corners $(x_1, y_1, z_1)$, $(x_2, y_2, z_2)$, with $x_1 \leq x_2$, $y_1 \leq y_2$ and $z_1 \leq z_2$.

# Input data

The first line contains five natural numbers, $l$, $L$, $H$, $Q_1$ and $Q_2$ (with meanings from the statement). The next $Q_1$ lines contain seven natural numbers, $x_1$, $y_1$, $z_1$, $x_2$, $y_2$, $z_2$, $v$ which represent the subzone and the value by which the number of known minerals in each cube of the respective subzone increases. The next $Q_2$ lines contain six natural numbers, $x_1$, $y_1$, $z_1$, $x_2$, $y_2$, $z_2$, which represent the subzones for which Armando is wondering what the number of known minerals is.

# Output data

Print, in order, on separate lines, the answers to the $Q_2$ queries.

# Constraints and clarifications

* $1 \leq l, L, H \leq 300$;
* $1 \leq Q_1, Q_2 \leq 500\ 000$;
* $1 \leq x_1 \leq x_2 \leq l$;
* $1 \leq y_1 \leq y_2 \leq L$;
* $1 \leq z_1 \leq z_2 \leq H$;
* $1 \leq v \leq 100\ 000$;
* The parallelepiped is considered to have the corners at $(1, 1, 1)$ and $(l, L, H)$;
* For $30$ points, $Q_1, Q_2 \leq 30$;
* For the remaining $70$ points, there are no additional constraints.
* If you use `std::cin` for input, it is recommended to use:
```cpp
std::cin.tie(0)->sync_with_stdio(false);
```

# Example 1

`stdin`
```
10 11 12 5 6
1 1 1 3 4 5 7
1 2 3 4 8 3 4
3 5 11 7 10 12 104
5 10 2 6 11 8 1005
9 7 8 10 10 10 232
1 2 1 7 8 9
2 3 4 9 7 8
9 10 11 10 11 12 
2 2 2 3 3 4
5 3 2 10 9 11
3 4 3 5 6 5
```

`stdout`
```
427
288
0
100
5736
45
```

# Example 2

`stdin`
```
6 6 6 2 1
3 2 2 5 4 3 3
3 5 5 4 6 6 10
1 1 1 6 6 6
```

`stdout`
```
134
```
