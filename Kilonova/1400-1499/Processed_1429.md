In a city, there is a cubic-shaped hotel with $N$ floors, numbered from $1$ to $N$. The area of each floor $K$ is square and is divided into $N \times N$ identical adjacent rooms, arranged in $N$ rows and $N$ columns, each room being labeled with a triplet of natural numbers $(K, L, C)$ ($K$ is the floor, $L$ is the row, $C$ is the column, $1 \leq K, L, C \leq N$), as shown in the adjacent image.

Among the $N \times N \times N$ rooms of the hotel, one is special because a mouse has been living there for a long time. Being cunning, he knows the label of the room he is in as well as the label of the room where the hotel chef stores food.

~[Poza1.png|width=20em]

~[Poza2.png|align=right|width=8.5em] 

By studying the hotel, the mouse has found that on each floor, from any room, he can enter all the rooms that share a common wall with it (there is a small ventilation hole).

The mouse has also found that from any room, he can enter the room immediately above it (if it exists) and the room immediately below it (if it exists).

Being a well-behaved mouse, he does not enter any room occupied by guests to avoid disturbing them.

The hotel having many guests, the mouse needs to find the shortest route from his room to the room with food, a route that passes through a minimum number of rooms, **all unoccupied**.

# Task

Determine:
1. The number of rooms through which the shortest route of the mouse from his room to the room with food (including his room and the room with food) passes;
2. Labels of the rooms through which the route determined in point 1 passes.

# Input data

The file `traseu.in` contains:
* The first line contains two natural numbers $N$ and $M$ separated by a space, $N$ with the meaning from the statement and $M$ representing the number of rooms occupied by hotel guests;
* The second line contains three natural numbers $K_1$, $L_1$, $C_1$, separated by a space, representing the label of the room where the mouse is;
* The third line contains three natural numbers $K_2$, $L_2$, $C_2$, separated by a space, representing the label of the room where the food is stored;
* Each of the following $M$ lines contains three natural numbers $X$, $Y$, $Z$, separated by a space, representing the labels of the $M$ rooms occupied by guests.

# Output data

The output file `traseu.out` will contain the first line as a natural number $T$ representing the number of rooms through which the shortest route of the mouse from his room to the room with food determined at point 1 passes. Each of the following $T$ lines will contain three natural numbers $X$, $Y$, $Z$, separated by a space, representing the labels of the rooms through which the route determined at point 1 passes, in the order in which the mouse traverses the rooms to get from his room to the room with food.

# Constraints and clarifications

* $2 \leq N \leq 100$
* $1 \leq M \leq 5 \ 000$
* $M < N \cdot N - 2$
* The mouse only enters rooms not occupied by guests.
* The mouse's room is a room not occupied by guests.
* If there are multiple routes of the mouse from his room to the room with food that pass through exactly $T$ rooms, the displayed route will be the smallest route in lexicographical order.
* The label $(X_1, Y_1, Z_1)$ is considered strictly smaller in lexicographical order than the label $(X_2, Y_2, Z_2)$ if only one of the following conditions is satisfied:
  * $X_1 < X_2$;
  * $X_1 = X_2$ and $Y_1 < Y_2$;
  * $X_1 = X_2$ and $Y_1 = Y_2$ and $Z_1 < Z_2$.
* The label $(X_1, Y_1, Z_1)$ is considered equal to the label $(X_2, Y_2, Z_2)$ if $X_1 = X_2$ and $Y_1 = Y_2$ and $Z_1 = Z_2$. We will write their equality as: $(X_1, Y_1, Z_1) = (X_2, Y_2, Z_2)$.
  * The route that passes (in this order) through the rooms with the labels $(X_1, Y_1, Z_1)$, $(X_2, Y_2, Z_2)$, ..., $(X_T, Y_T, Z_T)$ is smaller in lexicographical order than the route $(A_1, B_1, C_1)$, $(A_2, B_2, C_2)$, ..., $(A_T, B_T, C_T)$ if there exists an index $J$ ($1 \leq J \leq T$) such that $(X_1, Y_1, Z_1) = (A_1, B_1, C_1)$, $(X_2, Y_2, Z_2) = (A_2, B_2, C_2)$, ..., $(X_{J-1}, Y_{J-1}, Z_{J-1}) = (A_{J-1}, B_{J-1}, C_{J-1})$ and the label $(X_J, Y_J, Z_J)$ is strictly smaller in lexicographical order than the label $(A_J, B_J, C_J)$.
* $40\%$ of the points are awarded for correctly determining the number $T$ and $100\%$ of the points are awarded for correctly solving both tasks.
* It is guaranteed that there is a solution for both tasks for all test data.

# Example

`traseu.in`
```
3 4
1 1 1 
3 3 3
3 3 1
2 1 1
3 1 1
3 1 3
```

`traseu.out`
```
7
1 1 1
1 1 2
1 1 3
1 2 3
1 3 3
2 3 3
3 3 3
```

## Explanation

~[Poza3.png|align=right|width=23em]

The hotel has three floors ($1$, $2$, and $3$). On each floor, there are $3 \times 3$ rooms. The mouse is in the room labeled $(1,1,1)$ and the room with food is labeled $(3, 3, 3)$.

There are $4$ rooms occupied by guests. These have the labels: $(3, 3, 1)$, $(2, 1, 1)$, $(3, 1, 1)$, $(3, 1, 3)$. The shortest route passes through $T = 7$ rooms. There are multiple such routes. Some examples:

1) $(1,1,1)$, $(1,1,2)$, $(1,1,3)$, $(1,2,3)$, $(1,3,3)$, $(2,3,3)$, $(3,3,3)$;
2) $(1,1,1)$, $(1,1,2)$, $(1,1,3)$, $(2,1,3)$, $(2,2,3)$, $(3,2,3)$, $(3,3,3)$;
3) $(1,1,1)$, $(1,2,1)$, $(1,3,1)$, $(1,3,2)$, $(2,3,2)$, $(3,2,3)$, $(3,3,3)$;

Route 1 from the list above is the smallest in lexicographical order.