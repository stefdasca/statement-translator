It is considered an encryption machine consisting of an array with $n$ rows and $n$ columns, an array that contains all numbers from $1$ to $n^2$ placed "serpentine" along the rows, from the first row to the last row, on the odd rows from left to right, and on the even rows from right to left (as in the adjacent figure).

~[cff5d8861bae938b2eed0dd1708a990c.png]

We name "shuffling" the operation of unfolding spirally the values in the array in the order indicated by arrows and rearranging them in the same array, "serpentine" along the rows as in the previous case.

For example, unfolding the array leads to the sequence: $1 \ 2 \ 3 \ 4 \ 5 \ 12 \ 13 \ 14 \ 15 \ 16 \ 9 \ 8 \ 7 \ 6 \ 11 \ 10$, and rearranging this in the array leads to obtaining a new array represented in the second adjacent figure.

~[dfa4ef22ee11881dd041cd3cb27af121.png]

After any shuffling operation, the process can be resumed, performing a new shuffling. An interesting fact has been observed: after a number of shufflings, some values return to their initial position (which they had in the starting array). For example, after two shufflings, the $4 \cdot 4$ array contains $9$ of its elements in exactly the same position they were initially (see marked elements in the figure).

~[d95634cea4aeffce07125a58f99b99a1.png]

# Task

For given $n$ and $k$, write a program that determines the minimum number of shufflings of an $n$-rows array necessary to achieve an array with exactly $k$ elements back in their initial position.

# Input data

The input file `spirala.in` contains on the first line the two numbers $n$ and $k$ separated by a space.

# Output data

The output file `spirala.out` contains a single line which must contain the determined number of shufflings.

# Constraints and clarifications

* $3 \leq N \leq 50$
* The input data is chosen so that the minimum number of necessary shufflings does not exceed $2 \cdot 10^9$

# Example 1

`spirala.in`
```
4 9
```

`spirala.out`
```
2
```

# Example 2

`spirala.in`
```
6 36
```

`spirala.out`
```
330
```