# Bartender

Paftenie decided to become a bartender. Before that, he needs to demonstrate his skill in handling drinks. Paftenie's bar consists of $N$ rooms aligned in a circle. In each room, there is a glass with a drink, each drink having a certain value (between $1$ and $2\ 000\ 000\ 000$). He needs to move the drinks from one room to another such that, in the end, the drinks are sorted according to the rooms. If at the end, in room $i$, there is a drink with value $a_i$, the array of values $a_1, a_2, \ldots, a_N$ is considered sorted if there exists $1 \leq i \leq N$ such that $a_i \leq a_{i+1} \leq \ldots \leq a_N \leq a_1 \leq \ldots \leq a_{i-1}$ (the array is circular). At any moment, Paftenie can hold at most two glasses on the tray. To move the drinks, he can perform the following moves:
- he can take a glass from the room he is in and place it on the tray (costs him $10$ seconds)
- he can place a glass in a room where there is no drink (costs him $10$ seconds)
- he can move from room $i$ to room $j$ with $c$ glasses on the tray ($0 \leq c \leq 2$) (costs him $c \cdot |i-j|$ seconds)

## Task

Help Paftenie sort the glasses in minimum time!

## Input data

The input file `barman.in` contains:
- The first line contains the number $N$ of drinks.
- The next line contains $N$ integers representing the values of the drinks - the $i$-th number represents the value of the drink initially in room $i$ ($a_i$).

## Output data

The output file `barman.out` will contain a single number on the first line representing the minimum time to sort the drinks.

## Constraints and clarifications

$1 \leq N \leq 600$

At any moment, apart from the glasses Paftenie has on the tray, a room can contain at most one glass.

## Example

`barman.in` 
```
4
1 5 2 2
```

`barman.out` 
```
42
```

## Explanation

- $5 \ 2 \ 2$ goes to room $1$ and puts the glass from there on the tray ($10$s)
- $5 \ 2 \ 2$ moves from room $1$ to room $2$ with one glass on the tray ($1$s)
- $2 \ 2$ puts the glass from room $2$ on the tray ($10$s)
- $1 \ 2 \ 2$ places the glass with value $1$ on the table in room $2$ ($10$s)
- $1 \ 2 \ 2$ returns to room $1$ with one glass on the tray ($1$s)
- $5 \ 1 \ 2 \ 2$ places the glass with value $5$ on the table in room $1$ ($10$s)

$\rightarrow 42$ seconds. The array is sorted because $1 \leq 2 \leq 2 \leq 5 (a_2 \leq a_3 \leq a_4 \leq a_1)$