In a library, there are $C$ identical cabinets placed next to each other along the wall of a room, numbered from left to right with natural numbers from $1$ to $C$. Each cabinet contains $1\ 000$ shelves, arranged vertically one above the other, with the shelves of each cabinet being numbered from $1$ to $1\ 000$ from bottom to top.

Each cabinet is equipped with a ladder that can be used to reach any shelf. If the librarian climbs to a certain level $k$ on a specific cabinet $D$, she will be able to gather any book from shelves $1$ to $k$ inclusive, from cabinet $D$ and the neighboring cabinets (cabinet $D-1$ and cabinet $D+1$).

Knowing the cabinets and the shelves from which books need to be taken, the librarian wants to gather all the requested books, but the sum of the heights she needs to climb must be minimal.

# Task

Write a program that determines the minimum sum of the heights which the librarian needs to climb to gather all the requested books.

# Input data

The first line of the input file `rafturi.in` contains two natural numbers $C$ and $N$, separated by a space, representing the number of cabinets and respectively the number of books that the librarian needs to gather.

The next $N$ lines contain two natural numbers $a$ and $b$, separated by a space, representing the cabinet number and the shelf number from which a book needs to be taken.

# Output data

The output file `rafturi.out` will contain a single natural number representing the minimum sum of the heights which the librarian needs to climb to gather all the requested books.

# Constraints and clarifications

* $1 \leq C \leq 10\ 000$
* $1 \leq N \leq 50\ 000$

# Example

`rafturi.in`
```
10 4
5 4
1 1
6 2
3 8
```

`rafturi.out`
```
11
```

## Explanation

The librarian climbs as follows:

- to cabinet $1$ to shelf $1$
- to cabinet $4$ to shelf $8$
- to cabinet $6$ to shelf $2$