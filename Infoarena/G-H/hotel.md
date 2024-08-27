# Hotel

The "Informatics" hotel is one of the most luxurious hotels in Galaciuc. Throughout the year, many groups of tourists arrive at this hotel or leave at the end of their stay, so the exact situation of free and occupied rooms is quite hard to determine, especially since the hotel has a large number of rooms. But this year, the hotel owner has decided he needs a change. Therefore, he has hired you to write an efficient program to meet his needs.

## Task

Write a program that efficiently handles the following 3 types of instructions:
- type 1: the arrival of a new group of tourists A group of tourists with $M$ members wants to occupy $M$ consecutively numbered free rooms. The program will be provided with the number $i$ of the starting room of the sequence of rooms occupied by the group and the number $M$ of group members. It is guaranteed that any room $i,i+1,\dots,i+M-1$ is free at that moment.
- type 2: the departure of a group of tourists When they leave, tourists leave in groups (not necessarily the ones they came with). A departing group with $M$ members leaves $M$ consecutively numbered previously occupied rooms. The program will be provided with the number $i$ of the starting room of the sequence of freed rooms and the number $M$ of group members. It is guaranteed that all rooms numbered $i,i+1,\dots,i+M-1$ are already occupied by tourists.
- type 3: the owner's query The hotel owner may occasionally ask what is the maximum length of a consecutively numbered sequence of free rooms. He needs this number to know the maximum possible number of group members that could be accommodated at the "Informatics" hotel.

## Input data

The first line of the file `hotel.in` will contain the numbers $N$ and $P$, representing the number of rooms in the hotel (numbered from $1$ to $N$), respectively the number of upcoming instructions. Each of the next $P$ lines will contain a number $c$, representing the type of instruction described on that line:
- if $c$ has the value $1$, it will be followed (on the same line) by 2 other numbers, $i$ and $M$, representing the number of the first room allocated to the newly arrived group and the number of group members
- if $c$ has the value $2$, it will be followed (on the same line) by 2 other numbers, $i$ and $M$, representing the number of the first room to be freed by the departing group, as well as the number of group members leaving the hotel
- if $c$ has the value $3$, it will not be followed by any other number on that line; however, the program will have to display in the file `hotel.out` the maximum length of a consecutively numbered sequence of free rooms.

## Output data

In the file `hotel.out`, print on separate lines, for each instruction of type $3$, the maximum length of a consecutively numbered sequence of free rooms, taking into account the instructions of types $1$ and $2$ present in the input file before the type $3$ instruction being answered. Before the first instruction, all rooms are free.

## Constraints and clarifications

$3 \leq N \leq 100\ 000$

$3 \leq P \leq 200\ 000$

At any moment, only one tourist can be accommodated in a room.

## Example

`hotel.in`
```
12 10
3
1 2 3
1 9 4
3
2 2 1
3
2 9 2
3
2 3 2
3
2 3 2
3
```

`hotel.out`
```
12
4
6
10
```