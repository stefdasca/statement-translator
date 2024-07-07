
You are a participant at the National Olympiad of Informatics. The program of the Olympiad includes some entertainment activities. One of them is visiting a museum. This museum has a rectangular matrix structure with $M$ rows and $N$ columns; from any room, you can reach the neighboring rooms in the north, east, south, and west directions (if these rooms exist). For the position ($i, j$) moving north means going to position ($i-1, j$), east to ($i, j+1$), south to ($i+1, j$), and west to ($i, j-1$).

This museum has some special rules. Each room is marked with a number between $0$ and $10$ inclusive. Multiple rooms can be marked with the same number. Rooms marked with the number $0$ can be visited for free. You can enter a room marked with the number $i$ for free, but you cannot leave it unless you show the supervisor a ticket with the number $i$. Fortunately, any room with the number $i$ offers for sale a ticket with the number $i$; once bought, this ticket is valid in all rooms marked with that number. Tickets may have different prices, but a ticket with the number $i$ will have the same price in all rooms where it is offered for sale.

You enter the museum through the North-West corner (position ($1, 1$) of the matrix) and want to reach the exit located in the South-East corner (position ($M, N$) of the matrix). Once you get there, you receive a free ticket that allows you to visit the entire museum. Positions ($1, 1$) and ($M, N$) are marked with the number $0$.

# Task

Given the structure of the museum, determine a strategy for traversing the rooms so that you reach the room ($M, N$) paying as little as possible. If there are multiple options, choose one in which the minimum number of rooms is traversed (to save time and have more time to visit the entire museum).

# Input data

The first line of the input file `muzeu.in` contains two integers $M$ and $N$, separated by a space, the number of rows and columns of the matrix representing the museum. The next $M$ lines contain the structure of the museum; each contains $N$ integers between $0$ and $10$ inclusive, separated by spaces. The line $M+2$ contains $10$ integers between $0$ and $10\ 000$ inclusive, representing the costs of tickets $1$, $2$, $3$, $\dots$, $10$ in that order.

# Output data

In the file `muzeu.out` you will print:

* on the first line the minimum sum necessary to go from ($1, 1$) to ($M, N$);
* on the second line the minimum number of moves $L$ made from one room to an adjacent room, to go from ($1, 1$) to ($M, N$);
* on the third line $L$ characters from the set $N$, $E$, $S$, $V$ representing movements towards North, East, South, or West.

# Constraints and clarifications

* $2 \leq N, M \leq 50$;

# Example

`muzeu.in`
```
5 6 
0 0 0 0 0 2
0 1 1 1 4 3
0 1 0 0 0 0
0 1 5 1 0 0
0 0 0 1 0 0
1000 5 7 100 12 1000 1000 1000 1000 1000
```

`muzeu.out`
```
12
9
EEEEESSSS
```
