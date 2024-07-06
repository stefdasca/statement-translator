```
On a chessboard of size $N \\cdot N$, there is a dice (with edge length equal to the edge length of the square defining a square of the chessboard). This dice can roll according to a sequence of commands read from a file, each read character having the following meanings:

* $u$ roll in the square above (up);
* $d$ roll in the square below (down);
* $l$ roll in the square to the left (left); 
* $r$ roll in the square to the right (right).

The following are known:
* the initial position of the dice given by the coordinate point (row, column);
* the values on the faces of the dice given by a sequence: top, bottom, left, right, front, back, in this order;
* the sequence of movements given by the characters ‘u’, ‘d’, ‘l’, ‘r’.

# Task: 

Determine the sum of the values that the faces will have, as a result of the movement sequence, in the following order: top, bottom, left, right, front, back, as well as the set of values that are on the top face of the dice at each of its moves. The first position is considered the initial position.

The sequence of dice movements is executed as long as the dice by a move remains on the chessboard. If as a result of a move the dice would go outside the board, the results obtained up to that point will be displayed.

# Input data:

The input file named `zar.in` contains: $N$, with the meaning of the board size; $l_p$, $c_p$ - meaning the initial row, initial column for the dice position; $v_1$, $v_2$, $v_3$, $v_4$, $v_5$, $v_6$ - the values of the dice faces, values between $1$ and $6$; $h$ - number of characters representing the movement sequence
$c_1$, $c_2$, $c_3$, ..., $c_h,$ - the characters ‘u’, ‘d’, ‘l’, ‘r’ meaning the next move of the dice.

# Output data:

The output file named `zar.out` contains

- the first line contains 6 values separated by space: $suma_{sus}$, $suma_{jos}$, $suma_{stanga}$, $suma_{dreapta}$, $suma_{fata}$, $suma_{spate}$, meaning the sum of the points on the specified faces, in this order.
- the second line contains $h+1$ values representing the values that are on the top face through the proposed movement sequence. The first position is the initial value.

# Constraints and clarifications

* the movement sequence can have up to $1 \\ 000$ characters ‘u’, ‘d’, ‘l’, ‘r’;
* $4 \\leq N \\leq 100$

# Example 1

`zar.in`
```
8
7 3
1 6 5 2 4 3
19
uuuuuurrrrdddlldduu
```

`zar.out`
```
72 68 77 63 67 73
1 4 6 3 1 4 6 5 1 2 6 4 1 3 2 4 6 3 6 4
```

# Example 2

`zar.in`
```
8
7 3
1 6 5 2 4 3
9
uuuuuuuuu
```

`zar.out`
```
25 24 35 14 27 22
1 4 6 3 1 4 6
```
```