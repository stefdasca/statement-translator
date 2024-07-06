Sure, here is the translated text:

---

Your fearsome warriors have kidnapped Princess Ghiocela and imprisoned her in your castle on the top of Mount Pleşuv. Since you are an evil genius, you have decided to offer the princess the illusion of a chance to escape.

Your castle is shaped like a grid with $M$ rows and $N$ columns. The $M \times N$ cells of the castle are numbered from $1$ to $M \cdot N$ in the order of traversing the grid from top to bottom, and on the same row, in the order of columns from left to right.

In each of the castle's cells, you have placed a key, more precisely, cell $i$ contains the key with number $i$. Obviously, to enter a room, the princess needs a specific key that allows opening it. Moreover, from one room, the princess can move at any moment to one of the maximum four adjacent rooms horizontally and vertically, provided she holds the key necessary to open it.

Once she has entered a room and obtained a key, the princess keeps it and can use it as many times as she wants.

# Task

Although you are convinced the princess will not escape from the castle, you are curious to find out how many of the $M \cdot N$ rooms are accessible to her. Given the dimensions of the castle, the initial room where the princess is located, and the keys required to open each of the rooms, find the answer to this important question.

# Input data

The input file `castel.in` contains on the first line three natural numbers $M$, $N$, $K$ separated by a space, representing the dimensions of the castle, and the number of the room where the princess is initially located, respectively. Next follows the description of the castle. Each of the next $M$ lines contains $N$ natural numbers between $1$ and $M \cdot N$ representing the keys required to open each room.

# Output data

The output file `castel.out` will contain a single line with a single natural number representing the number of rooms accessible to the princess.

# Constraints and clarifications

* $1 \leq M, N \leq 150$;
* $1 \leq K \leq M \cdot N$;
* Once the princess has entered a room, that room will remain open forever.

# Example

`castel.in`
```
4 3 1
1 1 4
1 6 2
6 9 8
12 10 11
```

`castel.out`
```
7
```

## Explanation

The princess starts from room $1$. Here she uses key $1$ and enters room $4$. She returns to room $1$ and unlocks room $2$. She uses the key taken from room $4$ and unlocks room $3$. At this point, she holds keys $1$, $2$, $3$, and $4$. She uses key $2$ and enters room $6$, then uses key $6$ and enters room $5$, then room $4$, from where, using the key taken from room $6$, she enters room $7$. In the end, the princess holds keys $1$, $2$, $3$, $4$, $5$, $6$, and $7$, and cannot open any other room.

~[castel.png]

---

I have carefully translated all parts of the initial text while preserving the structure, general syntax, and format, including mathematical expressions and image format. I also checked and corrected any potential grammar and syntax errors according to English language rules.