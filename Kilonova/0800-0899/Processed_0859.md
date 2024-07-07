
A land represented by a matrix with $n$ rows and $n$ columns containing natural numbers is considered. Each element of the matrix stores the height of the terrain area corresponding to the position of that element. On this land, $m$ lasers are placed in known positions. A laser is directed towards one of the $4$ cardinal points, coded by numbers as follows: North by the value $1$, East by the value $2$, South by the value $3$, and respectively West by the value $4$. Each laser will make a single shot and as a result, it will decrease by $1$ the values of all elements in the matrix in its shooting direction, except for the laser's position.

After all the shots are fired, the positions of all the pits and trenches are sought. We call a pit an element in the matrix for which all $8$ neighboring elements in the line, column, or diagonals have values greater than or equal to it. We call a trench a maximal sequence formed of two or more pits located on the same line in consecutive columns. The sequence is called maximal if it cannot be extended at either end.

# Task

Knowing the configuration of the land and the placement of the lasers, resolve one of the following two tasks:
1. determine the number of pits in the land after the shots are fired;
2. determine the number of existing trenches after the shots are fired.

# Input data

The input file `lasere.in` contains on the first line a natural number $c$ which represents the task to be solved ($1$ or $2$). The second line contains two natural numbers $n$ and $m$, representing the number of rows and columns of the matrix, respectively the number of lasers. On the next $n$ lines, there are $n$ natural numbers each, representing the elements of the matrix. On the following $m$ lines, the $m$ lasers are described, one laser per line. A line describing a laser contains $3$ natural numbers $i \ j \ d$, meaning that there is a laser on row $i$ and column $j$, which shoots in direction $d$. The values on the same line are separated by a space.

# Output data

The output file `lasere.out` will contain on the first line a single natural number. This number represents the number of pits (if $c=1$) or the number of trenches (if $c=2$).

# Constraints and clarifications

* $4 \leq n \leq 200$;
* $1 \leq m \leq 200$;
* The numbering of rows and columns is from $1$ to $n$.
* The elements of the matrix in the input file are natural numbers with a maximum of $4$ digits.
* The positions of the lasers are distinct.
* For tests worth $30\%$ of the score, the task is $1$.

# Example 1

`lasere.in`
```
1
5 3
1 1 3 4 5
8 7 6 5 4
9 3 5 6 7
1 1 1 9 8
1 1 1 5 6
2 3 3
4 4 4
1 4 2
```

`lasere.out`
```
6
```

# Example 2

`lasere.in`
```
2
5 3
1 1 3 4 5
8 7 6 5 4
9 3 5 6 7
1 1 1 9 8
1 1 1 5 6
2 3 3
4 4 4
1 4 2
```

`lasere.out`
```
1
```

## Explanation

After the lasers act, the land looks like this:
```
1 1 3 4 4
8 7 6 5 4
9 3 4 6 7
0 0 -1 9 8
1 1 0 5 6
```
There are $6$ pits and one trench. Pits are counted even if they are part of a trench.
