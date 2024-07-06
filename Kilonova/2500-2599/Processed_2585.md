Miss R is a young woman very passionate about medicine. Constantly preparing for admission to UMF, she notices an obstacle - Stress.

Miss R has a house with $N \cdot M$ rooms, arranged in $N$ rows (numbered from $1$ to $N$) and $M$ columns (numbered from $1$ to $M$), of which $B$ rooms are inaccessible (access is not allowed in these). We denote by $[i, j]$ ($1 \leq i \leq N, 1 \leq j \leq M$) the room located at row $i$ and column $j$.

Because the Universe is unfriendly, it wants to hinder Miss R and thus sends Stress into her house in room $[X, Y]$, which is an accessible room.

Stress can move to any room adjacent to the room he is in (located on the same row in an adjacent column or on the same column in an adjacent row) or he can use one of his aces up his sleeve. Stress has $Q$ aces.

When using ace number $i$ ($1 \leq i \leq Q$), Stress can move from room $[L1_i, C1_i]$ to room $[L2_i, C2_i]$. Any move (using an ace or to an adjacent room) takes one second and the move cannot be made if it means returning to the last room that was visited. It is guaranteed that if there is an ace up the sleeve from room $[L1, C1]$ to room $[L2, C2]$, there will not be another ace from room $[L2, C2]$ to room $[L1, C1]$.

Miss R is initially in room $[1, 1]$. When she notices that Stress has entered the house, she panics and follows a path illustrated by a string of characters that describe the directions of movement:
* L - from room $[i, j]$ will move to room $[i, j - 1]$
* R - from room $[i, j]$ will move to room $[i, j + 1]$
* U - from room $[i, j]$ will move to room $[i - 1, j]$
* D - from room $[i, j]$ will move to room $[i + 1, j]$

It is guaranteed that Miss R will not pass through inaccessible rooms.
Stress and Miss R cannot remain stationary in rooms; each of them must make a move every second.


# Task
Knowing that the goal of Stress is to catch Miss R, write a program to determine the minimum time in which Stress can reach the same room as Miss R.

# Input data

The input file `drar.in` contains on the first line the numbers $N \ M \ Q \ X \ Y \ B$, representing the dimensions of Miss R's house, the number of aces up Stress's sleeve, the coordinates of the room where Stress enters, respectively the number of inaccessible rooms.
The next $B$ lines contain the inaccessible rooms, one room per line. The following $Q$ lines describe the aces, one ace per line, in the form of the $4$ numbers $L1_i \ C1_i \ L2_i \ C2_i$, ($1 \leq i \leq Q$) with the meaning from the statement. The last line of the file contains the string of characters that describes how Miss R moves. The numbers written on the same line are separated by a space.

# Output data

The output file `drar.out` will contain a single line on which will be written the minimum time in which Stress can reach the same room as Miss $R$ or the value $-1$ if this is not possible.

# Constraints and clarifications

* $1 \leq N, M \leq 200$
* $1 \leq X \leq N, 1 \leq Y \leq M$
* $0 \leq Q \leq 1 \ 000$
* $0 \leq B \leq N \cdot M$
* $1 \leq L1i, L2i \leq N, 1 \leq C1_i, C2_i \leq M$
* $1 \leq$ length of the path $\leq 200$

|#|Score|Constraints|
|-|-|-|
|1|10|$X = Y = 1$|
|2|30|$1 \leq N, M \leq 6, 0 \leq Q \leq 3$|
|3|30|$7 \leq N, M \leq 50$|
|3|30|No additional constraints.|

# Example

`drar.in`
```
6 6 4 5 2 5
2 1
4 4
2 4
3 2
2 6
6 4 2 2
3 4 2 3
5 1 2 5
3 5 3 3
RRRRDD
```

`drar.out`
```
6
```