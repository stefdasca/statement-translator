# Task

Gigel received a game with marbles for his birthday. The game contains $n$ marbles numbered with distinct natural numbers from $1$ to $n$. While playing, Gigel mixed the marbles so that they are now out of order. To put them back in the game's box, Gigel takes the marbles one by one from the table and places them in the box forming a sequence. However, Gigel is still playing, so he doesn't place the marbles one after another, but follows a rule he strictly adheres to. Thus, Gigel tries to place each marble he takes from the table exactly in the middle of the sequence of marbles already formed. If this is not possible (the sequence has an odd length), he places the marble at the end of the already formed sequence. After all the marbles have been placed in the box, Gigel realizes he didn't note the order in which he took the marbles from the table and naturally wonders if he can deduce this from the sequence of marbles he just formed.

# Task

Given the number of marbles and the final configuration of marbles in the sequence, determine:
1. the number of the last marble taken from the table;
2. the order in which the marbles were taken from the table.

# Input data

The input file `ordine.in` contains on the first line the number $n$ of marbles. The second line of the input file contains $n$ natural numbers, with values between $1$ and $n$, separated by spaces, representing the sequence of marbles obtained by Gigel in the box. The third line contains one of the values $1$ or $2$ representing task $1$, if the task is to determine the last marble taken by Gigel from the table, and task $2$, if the task is to determine the order in which Gigel took the marbles from the table.

# Output data

The output file `ordine.out` will contain on the first line a natural value representing the number of the last marble taken by Gigel, if the task was $1$, or $n$ natural numbers with values between $1$ and $n$, separated by spaces, which represent the order in which Gigel took the marbles from the table, if the task was $2$.

# Constraints and clarifications

* $1 \leq n \leq 250\ 000$;
* For task $1$, $30\\%$ of the score is awarded, and for task $2$, $70\\%$ of the score is awarded.

# Example 1

`ordine.in`
```
7
1 7 2 5 3 4 6
1
```

`ordine.out`
```
5
```

# Example 2

`ordine.in`
```
7
1 7 2 5 3 4 6
2
```

`ordine.out`
```
1 3 7 4 2 6 5
```
