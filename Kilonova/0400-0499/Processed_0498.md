# Task
You already know the famous Bob the Builder. He bought a plot of land and wants to build a house on it. Unfortunately, the problem is that the land has variable altitude.
\
The land is in the shape of a rectangle with a width of $N$ meters and a length of $M$ meters. It can be divided into $N*M$ squares.
Bob's house will be in the shape of a rectangle with sides parallel to the edges of the land, and its corners coincide with the corners of the squares.
The sides of the house can have equal lengths and must be of integer lengths, greater than or equal to $1$.
\
All the land covered by Bob's house must have exactly the same altitude to prevent the house from collapsing (Bob the Builder has the necessary knowledge to build a house on uneven terrain, but he does not want to work that hard on his own house).
\
Calculate the number of ways in which Bob the Builder can create his magnificent engineering work (the house), respecting the task.
\
**Note: Input data is read from the keyboard, and output data is displayed on the console.**

# Input data
The first input line contains the natural numbers $N$ $M$, the dimensions of the land.
Each of the next $N$ lines contains $M$ natural numbers $a_{ij}$, the altitude of each square piece of land.

# Output data
Print on the first line a single number, with the meaning from the task.
# Constraints and clarifications
- $1 \le N, M \le 1000$
- $1 \le a_{ij} \le 10^9$
- For tests worth 20 points, $N, M \le 50$.
- For tests worth 60 points, $N, M \le 500$.
# Example 1
  `stdin`
  ```
5 3
2 2 2
2 2 1
1 1 1
2 1 2
1 2 1
  ```

  `stdout`
  ```
  27 
  ```
# Example 2
  `stdin`
  ```
4 3
1 1 1
1 1 1
2 2 2
2 2 2
  ```

  `stdout`
  ```
36
  ```