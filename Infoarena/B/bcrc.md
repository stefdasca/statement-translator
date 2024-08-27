## Bcrc

Gigel is in a labyrinth consisting of $N$ rooms, numbered from $1$ to $N$, arranged in a circle. From room $K$ $(1 < K < N)$, he can move to rooms $K - 1$ and $K + 1$. From room $1$, he can move to rooms $2$ and $N$, and from room $N$, he can move to rooms $N - 1$ and $1$. Initially (at time $0$), Gigel is in room $1$. At each moment in time, Gigel can decide to stay in the room he is in or move to one of the $2$ adjacent rooms. Moving from one room to one of the adjacent rooms takes one unit of time. Therefore, if at time $T$ Gigel decides to move to an adjacent room, he will reach that room at time $T + 1$. From time to time, some rooms receive boxes, each containing a certain number of candies (possibly different from one box to another). Suppose a box appears in room $X$ at time $T$. If Gigel is in room $X$ at time $T$ (or enters that room precisely at time $T$), he takes the box and eats all the candies inside. Otherwise, Gigel will not be able to eat any candies from the box, as it will disappear by time $T + 1$.

## Task

Knowing the number of rooms in the labyrinth and the times at which the boxes with candies appear, determine the maximum number of candies Gigel can eat. The number of candies Gigel eats is the sum of the numbers of candies in each box he takes.

## Input data

The first line of the file `bcrc.in` contains two integers, separated by a space: $N$ and $M$, representing the number of rooms in the labyrinth and the number of boxes, respectively. Each of the following $M$ lines contains $3$ integers, separated by a space: $T$, $C$, and $B$. $T$ represents the time at which the box appears. $C$ represents the room number where the box appears. $B$ represents the number of candies the box contains. The boxes are given in the input file in ascending order of the times at which they appear.

## Output data

The file `bcrc.out` will contain a single number, representing the maximum number of candies Gigel can eat.

## Constraints and clarifications

$3 \leq N \leq 2048$

$0 \leq M \leq 50\ 000$

For each box:
$1 \leq T \leq 1\ 000\ 000\ 000$ 
$1 \leq C \leq N$
$1 \leq B \leq 9\ 999$

Multiple boxes can appear at the same time in different rooms (but not at the same time and in the same room).

$30\%$ of the test files will have $M \leq 5\000$

$30\%$ of the test files will have $N \leq 256$

## Example

`bcrc.in`
```
8 4
2 7 9
3 5 999
10 2 12
10 1 10
```

`bcrc.out`
```
21
```