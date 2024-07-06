In a country where corruption is rampant and the economy is struggling, in order to obtain all necessary approvals to start a business, the investor must pass through several rooms of a building where offices are located.

The building has a single floor where offices are adjacent to each other, forming a square grid of size $n \times n$. To facilitate access to offices, all neighboring rooms have doors between them. In each office, there is an official who demands a passage fee through the room (which can be, for some rooms, equal to $0$). The investor confidently enters through the top-left corner of the building (as seen from above the building plan) and wishes to reach the opposite corner of the building, where the exit is, paying a total fee as minimal as possible.

# Task

Knowing that he has $S$ _euros_ in his pocket and that each official demands the fee as soon as he enters the office, it is required to determine whether he can receive the necessary approvals and, if affirmative, what is the maximum amount of money that remains in his pocket upon exiting the building.

# Input data

The input file `taxe.in` contains on the first line the two numbers $S$ and $n$ separated by a space, and on the next $n$ lines, $n$ numbers separated by spaces representing the fees demanded by the officials in each office.

# Output data

The output file `taxe.out` contains a single line that contains the maximum number of euros that remain in the pocket or the value $\text{–}1$ if the investor does not have enough money to obtain the approval.

# Constraints and clarifications

* $3 \leq N \leq 100$
* $1 \leq S \leq 10\ 000$
* The values representing the fees demanded by the officials in offices are natural numbers, a fee not exceeding the value of $200$ _euros_.

# Example

`taxe.in`
```
10 3
1 2 5
1 3 1
0 8 1
```

`taxe.out`
```
3
```

## Explanation

~[f6e9603262d11a4578dcf349c249fd04.png]