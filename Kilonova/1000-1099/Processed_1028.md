In the city of Piticot, there live $N$ dwarves, each in a house on a one-way street. The houses are arranged along the street in the direction of travel starting from the house numbered $1$ to the house numbered $N$. In the city of Piticot, dwarves do not have ordinary names! They bear as their name the number of the house they live in. Their houses are also out of the ordinary! If you ring the doorbell of any house, you exert so much effort that you instantly lose a number of *dwarf*-kilograms.

Because they noticed that they have gained weight during the pandemic, each has set out to lose a number of *dwarf*-kilograms in a single day. For this, each dwarf will run along the street, starting from their own house and respecting the direction of travel of the street, and during the run, they will ring the bell at every house they encounter, including their own house, each only once. As an additional rule they will stop running in the following situations:

* Any dwarf will stop at the first house where, after ringing the bell, they notice that they have lost at least as much as they set out to lose since they started running;
* Any dwarf will stop running if they have rung the bell at the last house (house $N$), even if they have not managed to lose as much as they set out to.

# Task

Write a program that determines the maximum number of dwarves who have rung the bell at a house and how many houses were rung this maximum number of times.

# Input data

The input file `pitici.in` contains on the first line the natural number $N$. The second line contains $N$ natural numbers $A_i$, representing the number of *dwarf*-kilograms any dwarf loses if they ring the bell at house number $i\ (1 \leq i \leq N)$. The third line contains $N$ natural numbers $B_i$, representing the number of *dwarf*-kilograms that dwarf $i$ wants to lose. Within a line, the data is separated by a space.

# Output data

The output file `pitici.out` contains on the first line the numbers $Max$ and $Nr$, separated by a space, which represent the maximum number of dwarves who have rung the bell at a house and how many houses were rung this maximum number of times.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $1 \leq A_i \leq 1\ 000\ 000\ 000$
* $1 \leq B_i \leq 10^{18}$
* $A_i \leq B_i$, for any $1 \leq i \leq N$.

# Example

`pitici.in`
```
7
1 2 4 5 6 6 6
4 2 8 10 14 6 17
```

`pitici.out`
```
2 6
```

## Explanation

Dwarf $1$ in order to lose at least $4$ *dwarf*-kilograms rings the bells at houses $1, 2$, and $3$. Dwarf $2$ rings only at house $2$. Dwarf $3$ rings at houses $3$ and $4$. Dwarf $4$ rings at houses $4$ and $5$. Dwarf $5$ rings at houses $5, 6$, and $7$. Dwarf $6$ rings at house $6$ and dwarf $7$ rings only at house $7$ and does not manage to lose as much as they set out to lose. It is observed that at houses $2, 3, 4, 5, 6, 7$, the bell was rung $2$ times, which is also the maximum number of times.

