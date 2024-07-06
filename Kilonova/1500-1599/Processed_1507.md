# Introductory Mouse
Remy wants to store the cheese cubes he has collected. He has built a rectangular warehouse divided into $N \cdot M$ identical rooms. In each room, the mouse has stored a certain amount of cheese cubes (as shown in $Figure \ A$) and decided to eat one cheese cube from each room with cheese every day. However, Remy's plan is disrupted by John, the lazy mouse from the neighboring house, who dislikes gathering cheese by himself and has decided to steal from Remy's warehouse. John, being a math enthusiast, has decided that every evening, after his neighbor finishes eating, he will wander through the warehouse and steal all the cheese from the rooms containing a perfect square number of cheese cubes. John enters the warehouse through the room at the top left corner, with coordinates $(1, 1)$, moves through the first row from the first to the last column, then the second row from the last column to the first, and so on, until he has visited all the rooms (as shown in $Figure \ B$).

~[soricel.png|align=center]

# Task

Write a program to determine:
1. The number of days it will take to empty Remy's warehouse and how many rooms John will empty on day $K$.
2. The maximum number of consecutive rooms emptied by John in one day and the day on which this will happen.

# Input data

The input file `soricel.in` contains:
- On the first line, the natural number $P$ representing the task to be solved.
- On the second line, the three non-zero natural numbers $N$, $M$ and $K$, separated by a space, as explained in the statement.
- Each of the next $N$ lines contains $M$ natural numbers separated by a space, representing the number of cheese cubes $C_{ij}$ stored in the room with coordinates $(i, j)$.

# Output data

If the value of $P$ is $1$, the output file `soricel.out` will contain two values according to task $1$, i.e., the number of days it will take to empty the warehouse and the number of rooms emptied by John on day $K$. The values should be displayed in the required order and separated by a space.

If the value of $P$ is $2$, the output file `soricel.out` will contain two values according to task $2$, i.e., the maximum number of consecutive rooms emptied by John in one day and the day on which this will happen. The values should be displayed in the required order and separated by a space.

# Constraints and clarifications

* $1 \leq N \leq 200$
* $1 \leq M \leq 200$
* $0 \leq C_{ij} \leq {10}^{8}$
* $1 \leq K \leq$ the number of days until the warehouse is empty 
* There is at least one room containing more than one cheese cube;
* The total number of cheese cubes stolen from consecutive rooms in one day will not exceed ${10}^{9}$
* The day Remy starts eating is considered day $1$
* If there are two or more days on which John empties an equal number of consecutive rooms, the day when he ate the most cheese cubes will be displayed, and if these amounts are also equal, the day with the highest value will be displayed
* We assume that the rows are numbered from top to bottom starting from $1$, and the columns from left to right starting from $1$
* Correct solving of task $1$ grants $40$ points, and if only the first value is correctly displayed for each test, half of the points for that test will be granted
* For task $1$ there will also be tests worth $20$ points, for which $0 \leq C_{ij} \leq 1 \ 000$, and $N, M \leq 30$
* Correct solving of task $2$ grants $60$ points, and if only the first value is correctly displayed for each test, two-thirds of the points for that test will be granted

# Example 1

`soricel.in`
```
1
5 4 1
2 6 5 10
25 16 0 5
100 17 67 3
20 104 8 13
53 13 55 47
```

`soricel.out`
```
19 5
```

## Explanation

At the end of the first day, the warehouse will look like this:
**0** $5$ **0 0**
$24 \ 15$ **0 0**
$99$ **0** $66 \ 2$
$19 \ 103 \ 7 \ 12$
$52 \ 12 \ 54 \ 46$
because Remy ate one cheese cube from each room and then John emptied the rooms where the remaining number of cheese cubes was a perfect square. Following these steps, each day Remy will be able to eat from the warehouse for $19$ days (after $19$ days all rooms are empty because all numbers have become perfect squares or zero values).

On day $1$, John will steal the cheese from $5$ rooms, those with coordinates: $(1, 1)$, $(1, 3)$, $(1, 4)$, $(2, 4)$, $(3, 2)$.

# Example 2

`soricel.in`
```
2
5 4 1
2 6 5 10
25 16 0 5
100 17 67 3
20 104 8 13
53 13 55 47
```

`soricel.out`
```
6 4
```

## Explanation

On day $4$, John will empty $6$ rooms, those with coordinates: $(4, 4)$, $(4, 3)$, $(4, 2)$, $(4, 1)$, $(5, 1)$ and $(5, 2)$. This is the longest sequence of consecutive rooms emptied on the same day.