```markdown
The $K$ members of a group of treasure hunters are in a rectangular complex made up of square rooms with side $1$. Normally, all rooms should be open, but some of them are closed and can only be opened with special cards. Thus, each room and each card is assigned a number between $0$ and $20$; a room with the number $0$ is open from the start, while one with a different number is initially closed, it can be opened from inside or outside from a neighboring room with a card with the corresponding number and will remain open afterwards. Cards with the number $0$ have no practical use. A number can be assigned to multiple cards, respectively rooms.

From one room you can move to another only if they are neighbors and both are open. Two rooms are considered neighbors if they have a wall (therefore a side) in common. In each room there are treasures with a value between $0$ and $10\ 000$. Also, in each room there is exactly one access card (with a number between $0$ and $20$); a treasure hunter can pick up and use the cards from the rooms he passes through, but he cannot give them to another hunter unless he is in the same room with them.

# Task

Given the configuration of the complex and the initial positions of the treasure hunters, determine the maximum value of the treasures they can collect.

# Input data

The input data is read from the file `comoara.in`, which has the following format:
 - the first line contains the dimensions of the complex, $m$ and $n$
 - the following $m$ lines contain the numbers associated with each room
 - the following $m$ lines contain the values of the treasures in each room
 - the following $m$ lines contain the numbers associated with the cards in each room
 - the next line contains the number $K$ of the group members
 - the following $K$ lines contain the initial positions of the group members in the complex

# Output data

The output data will be printed to the file `comoara.out`, which will contain the total value of the treasures that can be collected by the $K$ members of the group.

# Constraints and clarifications

* $1 \leq m, n \leq 40$;
* $1 \leq k \leq 10$;

# Example 1

`comoara.in`
```
3 3
0 0 11
14 0 10
19 0 0
5162 4331 1390
5230 1955 9796
5507 6210 1021
0 0 0
19 0 0
0 0 0
2
3 2
2 1
```

`comoara.out`
```
23909
```

## Explanation

We can observe that the second treasure hunter cannot enter the room ($3,1$), even though he has the corresponding card, because he cannot leave the room ($2,1$) in which he is initially placed.

# Example 2

`comoara.in`
```
5 5
0 0 2 0 0
0 0 2 0 0
0 0 1 0 0
0 0 2 0 0
0 0 2 0 0
1 1 1 1 1 
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 0 0 0 0
1
1 1
```

`comoara.out`
```
21
```
```