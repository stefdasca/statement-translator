On a square meadow made up of $L \times L$ square parcels with a side of $1 \\text{meter}$, Easter eggs were hidden. Some eggs are more valuable than others. $N$ bunnies are positioned in parcels situated on the edge of the meadow and participate in the contest "My Basket is the Most Valuable". Initially, no two bunnies share the same parcel. They wear shirts with distinct numbers from $1$ to $N$. Since they are very well trained, the bunnies strictly follow these rules:
1. All bunnies start searching for eggs simultaneously, beginning with the parcel they occupy.
~[oua1.png|align=right]
2. The initial movement directions of the bunnies (represented in $\\text{Figure} \\ 1$) are as follows: those on the northern edge move south, those on the western edge move east, those on the southern edge move north, and those on the eastern edge move west;
3. In each parcel, a bunny stays for one minute, during which it will search for and possibly collect an egg and then jumps to the parcel indicated by its movement direction;
4. Collecting an egg changes the direction of movement;
~[oua2.png|align=right]
5. The direction of movement changes as follows: if the bunny comes from the North, it will head West, if it comes from the South, it will head East, if it comes from the East, it will head North, and if it comes from the West, it will head South. An example of movement is represented in $\\text{Figure} \\ 2$ for a bunny starting from parcel $(1, 4)$;
6. If two or more bunnies arrive at the same egg simultaneously, it will be collected by the one with the smallest number on its shirt.

The contest ends when there are no more bunnies on the meadow.

# Task

Write a program that displays the total number of eggs collected by the $N$ bunnies, the most valuable basket (its value), and the duration (in minutes) of the contest.

# Input data

The input file `oua.in` contains:
The first line contains $2$ natural numbers, $L$ and $P$ separated by a space, $L$ representing the number of rows and columns of the array used to represent the parcels, and $P$ the number of eggs on the meadow.
Each of the next $P$ lines contains $3$ natural numbers, separated by a space, representing the coordinates of the parcel $(i, j)$ where an egg is found $(1 \\leq i \\leq L, 1 \\leq j \\leq L)$ and its value $(v)$.
The next line contains the number $N$ of bunnies, and each of the next $N$ lines contains pairs of natural numbers representing the coordinates of the parcels where the bunnies are initially found, in the order of the numbers on their shirts.

# Output data

The output file `oua.out` will contain:
The first line contains $3$ natural numbers separated by a space, representing the total number of eggs collected by the $N$ bunnies, the most valuable basket (its value), and the duration (in minutes) of the contest.

# Constraints and clarifications

* $2 \\leq L \\leq 50$
* $0 \\leq N \\leq 100$
* $0 \\leq P \\leq 2 \ 500$
* $1 \\leq v \\leq 30$
* A bunny exits the meadow if it reaches outside the matrix.
* At any moment, multiple bunnies can exist in the same parcel, except during the first minute.

# Example

`oua.in`
```
5 6
1 4 10
2 2 1
2 3 5
3 3 6
5 1 4
5 2 2
2
2 1
3 5
```

`oua.out`
```
5 11 10
```

## Explanation

~[oua3.png|align=right]
The first bunny stays $10$ minutes on the meadow, collects $3$ eggs, with a total value of $7$, and follows the path $(2, 1) - (2, 2) -
(3, 2) - (4, 2) - (5, 2) - (5, 1) - (4, 1) - (3, 1) - (2, 1) - (1, 1)$
The second bunny stays $6$ minutes on the meadow, collects $2$ eggs, with a total value of $11$, and follows the path $(3, 5) - (3, 4) - (3, 3) - (2, 3) - (2, 4) - (2, 5)$