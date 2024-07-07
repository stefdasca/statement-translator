
~[img1.jpg|align=right] Mircea and Andrei are passionate about building structures from Lego pieces. Each of them has a set consisting of $N$ **black cubes** with sides of length $1$ and several white **rectangular parallelepiped** pieces with which they build a rectangular parallelepiped building with a square base of side $2$ and height $H$.

All white pieces have a height of $2$ and the other sides equal to $1$ and **cannot** be turned over when assembled to construct the building. The building will always contain **all** black pieces from the set and as many white pieces as necessary to complete it.

Upon completing the buildings, the two boys notice that although they used the same set of pieces, the two buildings are different because the combinations of black and white colors on the facades (north, south, west, or east) of the buildings do not look the same.

# Task

Write a program to calculate the number $T$ of different buildings that can be constructed with the given pieces, knowing that two buildings are identical if **simultaneously** the following conditions are met:
* the northern facade of one is identical to the northern facade of the other;
* the eastern facade of one is identical to the eastern facade of the other;
* the southern facade of one is identical to the southern facade of the other;
* the western facade of one is identical to the western facade of the other.

The program will output **the remainder of** the division of the number $T$ by $666\ 013$. 

# Input data

The file `cladire.in` contains two natural numbers $N$ and $H$ (in this order), separated by a space and with the meanings defined in the statement.

# Output data

The file `cladire.out` will contain on the first line a single natural number representing the remainder of the division of the number $T$ by $666\ 013$.

# Constraints and clarifications

* $N$, $H$ are natural numbers and $N$ is an even number;
* $2 \leq N \leq 4H$ and $1 \leq H \leq 1\ 000$;
* there are as many white pieces as necessary;
* a white piece will always be placed with the base side $1$, either on top of another piece of the building or at its base;
* at least one building can be constructed with the given pieces;
* for $30\%$ of the tests $H \leq 25$.

# Example 1

`cladire.in`
```
2 2 
```

`cladire.out`
```
4
```

## Explanation

~[img2.jpg]

# Example 2

`cladire.in`
```
4 3
```

`cladire.out`
```
16
```
