A mouse experiment is conducted in a rectangular box divided into $m \times n$ equal square rooms. Each room contains a certain amount of food. The mouse must start from the corner $(1,1)$ of the box and reach the opposite corner, eating as much food as possible. It can move from one room to an adjacent room (two rooms are adjacent if they have a common wall), eating all the food in the room when it enters and never entering a room it has previously entered.

# Task

Determine the maximum amount of food the mouse can eat and the path it can take to collect this maximum amount of food.

# Input data

The input file `mouse.in` contains on the first line two numbers $m$ and $n$ representing the number of rows and columns of the box, respectively. On the next $m$ lines, the $m \cdot n$ numbers represent the amount of food in each room, with $n$ numbers per line, separated by spaces.

# Output data

In the output file `mouse.out`, the first line will contain two numbers separated by a space: the number of rooms visited and the maximum amount of food collected. On the following lines, a possible path for the given amount will be written, in the form of pairs of numbers, starting with $(1, 1)$ and ending with $(m, n)$.

# Constraints and clarifications

- All values in the file are natural numbers between $1$ and $100$.
- You will receive 40 points for displaying the first two numbers.

# Example

`mouse.in`
```
2 4
1 2 6 3
3 4 1 2
```
`mouse.out`
```
7 21
1 1
2 1
2 2
1 2
1 3
1 4
2 4
```

## Explanation
~[exemplu.gif|align=center|width=40em]