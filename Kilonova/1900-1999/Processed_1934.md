A group of climbers, situated on the edge of a cliff on a mountainside, are caught in the middle of a storm. To take shelter, they need to find a sheltered area on the mountainside, formed of adjacent safe spaces in the North, South, East, and West directions, large enough to accommodate the entire group. The climbers have cameras mounted on their helmets that send live video footage to a team of rescuers. The informaticians manage to analyze the safe spaces of the mountainside and represent the mountainside using a binary matrix. Each safe space is encoded with $0$, and the values of $1$ represent blocked spaces.

They ask for your help to rescue the climbers.

# Task

Given the binary matrix encoding the mountainside, determine:

1) The maximum number of safe spaces that can form a sheltered area on the mountainside.
2) The maximum number of safe spaces in a rectangular sheltered area corresponding to a rectangle formed only of $0$ values in the given matrix.

# Input data

The input file `alpinistii.in` contains on the first line three natural numbers: $c$, $n$, and $m$, separated by a space. $c$ represents the task number that needs to be solved ($1$ or $2$), $n$ represents the number of rows of the matrix, and $m$ represents the number of columns. Each of the following $n$ lines contains $m$ digits of $0$ and $1$, separated by a space, with the significance from the statement.

# Output data

The output file `alpinistii.out` will contain on the first line a natural number representing the answer to the task being solved.

# Constraints and clarifications

* $1 \leq n, m \leq 200$
* The matrix contains only values of $0$ and $1$.
* For correctly solving task $1$, $40$ points are awarded, and for task $2$, $60$ points are awarded.

# Example 1

`alpinistii.in`
```
1
7 8
1 1 1 1 1 1 1 1 
1 0 0 1 1 1 1 0 
1 1 0 1 0 0 0 1 
1 1 0 1 0 0 1 1 
0 1 1 0 0 0 0 1 
0 0 1 0 0 0 0 1 
1 0 0 1 1 1 1 1
```

`alpinistii.out`
```
13
```

## Explanation

~[cerr1.png]

The sheltered area surrounded by yellow is the largest possible ($13$ safe spaces). The other sheltered areas have: $5$ safe spaces (green), $4$ safe spaces (brown), and $1$ safe space (blue).

# Example 2

`alpinistii.in`
```
2
7 8
1 1 1 1 1 1 1 1 
1 0 0 1 1 1 1 0 
1 1 0 1 0 0 1 1 
1 1 0 1 0 0 0 1 
0 1 1 0 0 0 0 1 
0 0 1 0 0 0 0 1 
1 0 0 1 1 1 1 1
```

`alpinistii.out`
```
9
```

## Explanation

~[cerr2.png]

The maximum number of safe spaces forming a rectangular sheltered area is $9$ (the area surrounded by yellow). It can be observed that the matrix also contains two other rectangular areas formed by $8$ safe spaces each (the areas surrounded by brown and green).