In a vast desert represented as an $n \times m$ matrix, traders venture forth relying on predefined rules.

Each trader starts their journey from a specific location, marked by coordinates $(x, y)$, and follows an initial direction (`N`, `S`, `E`, or `W`). They continue moving straight until they encounter a market. These markets, scattered throughout the desert, redirect the traders' paths. Defined by coordinates $(x, y)$ and a specific direction (`N`, `S`, `E`, or `W`), they reconfigure the trader's trajectory at the intersection.

This interaction can either guide the trader towards the edge of the matrix, signaling the end of the journey, or introduce them into a *motion loop*. A *motion loop* refers to the situation where a trader's trajectory becomes predictable and repeats endlessly. More precisely, after a series of movements, the trader finds themselves repeating a sequence of steps, periodically returning to the same coordinates and direction.

# Task
The problem statement is as follows: "Measure the distance traveled by each trader before being caught in a *motion loop* and the size of the repeated sequence, if it exists."

[Here](trader.cpp) or in the "Attachments" section on the side, you can find a C++ program that implements this problem but contains a few bugs. Your task is to fix the program.

# Input data
The first line contains $n$ and $m$, with the meanings given in the statement.

The second line contains $n_{piete}$, representing the number of markets that change the direction of the traders.

The third line contains $n_{negustori}$, representing the number of traders for whom we want to find the answer.

Each of the next $n_{piete}$ lines contain the coordinates of a market in the matrix.

Each of the next $n_{negustori}$ lines contain the starting coordinates of a trader and their specific direction.

# Output data
Each line contains two numbers $d$ and $l$ — the distance traveled by the trader not part of a loop, and the length of the loop, respectively. Traders are taken in the order they appear in the input file.

If there is no loop, $d$ will be the distance traveled until exiting the matrix, and $l$ will be $0$.

# Constraints and clarifications
- $1 \le n, m \le 500$
- $0 \le n_{piete} \le n \cdot m$
- $0 \le n_{negustori} \le n \cdot m$
- **The coordinates of the markets and traders are indices starting from $1$**.
- A trader will never start directly from a market.

# Example 1
`stdin`
```
6 6
2
1
1 2 S
6 2 E
1 6 W
```
`stdout`
```
14 0
```
## Explanation
The trader is initially at coordinates $(1, 6)$ and is moving to the left.

The trader moves $4$ squares to the left until the market at coordinates $(1, 2)$.
Then, $5$ squares down, until the market at coordinates $(6, 2)$.
Then, $4$ squares to the right, until exiting the matrix.

This trader does not enter a loop, so the loop length is $0$.

# Example 2
`stdin`
```
7 7
10
2
1 7 S
5 7 W
5 1 N
1 1 E
2 2 E
2 4 S
6 4 E
6 6 N
4 6 W
4 2 N
1 2 E
1 2 S
```
`stdout`
```
0 20
1 16
```
## Explanation
The first trader is represented in the image below in green, and the second in blue.

The first trader is already in a loop of length $20$, determined by the first $4$ markets.
The second trader moves one square down until entering a loop of length $16$, determined by the last $6$ markets.

~[trader-example.png|width=30em]