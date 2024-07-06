It is considered that there are $n$ blue square-shaped cards. These cards are placed on a rectangular piece of white paper, large enough so that the cards fit entirely on the sheet. The sides of the cards are parallel to the sides of the sheet. The coordinates of the vertices of the cards are natural numbers. The cards can be fully or partially overlapped. We consider that the bottom-left corner of the white sheet has coordinates $(0,0)$.

# Task

Determine:

$a)$ the total area of the blue surface that will be visible when looking at the sheet from above;

$b)$ the maximum number of cards that have at least one common overlap.

# Input data

~[Poza1.png|align=right|width=10em]

The first line of the input file `drept.in` contains a natural number $n$, representing the number of cards.

Each of the following $n$ lines contains three natural numbers $x, y$, and $d$, separated by a space, numbers that describe the cards. The three numbers $x, y$, and $d$ correspond to a square card $ABCD$ having the following coordinates: $A(x,y), B(x+d,y), C(x+d,y+d), D(x,y+d)$.

# Output data

The first line of the output file `drept.out` will contain a natural number representing the total area occupied by the blue cards on the white sheet, and the second line will contain a natural number representing the maximum number of cards that have at least one common overlap.

# Constraints and clarifications

* $1 \leq n \leq 10\ 000$
* $0 \leq x, y, d \leq 5\ 000$
* The area of any blue surface is strictly less than $2^{31}$
* For correctly determining the value of the task $a)$, $40\%$ of the points assigned to that test are awarded, and for correctly determining the value of the task $b)$, $60\%$ of the points assigned to that test are awarded.

# Example 1

`drept.in`
```
4
1 1 2
2 0 2
3 1 2
5 3 1
```

`drept.out`
```
11
2
```

# Explanation

~[Poza2.png|align=left|width=20em]

# Example 2

`drept.in`
```
4
1 1 4
2 2 3
3 3 2
4 4 1
```

`drept.out`
```
16
4
```

# Explanation

The $4$ cards overlap in the area delimited by the points $(4,4),(4,5),(5,5),(5,4)$.

~[Poza3.png|align=left|width=20em]