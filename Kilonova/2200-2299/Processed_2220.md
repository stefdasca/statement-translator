# Task

Two children, Train and Bus, are walking hand in hand through a matrix with $N$ rows and $M$ columns. Initially, they are located in the top-left corner of the matrix. Bus likes to move to the right, while Train likes to move downwards. Thus, their path will only consist of moves to the neighboring position either to the right or downwards. Their dream is to pass through all the positions in the matrix and return to the initial position.

When they are on the last column and move to the right, they will reach the first column of the same row, and if they move downwards from the last row, they will reach the first row of the same column. For each move, they write the letter `B` if the move is to the right and the letter `T` if the move is downwards.

Knowing $N$, $M$, and a natural number $K$, determine the $K$-th path in lexicographic order that starts from the top-left corner, passes exactly once through each position, and returns to the initial position of the matrix.

# Input data

The input file `trasee.in` contains on the first line the numbers $N$, $M$, and $K$ as described.

# Output data

The output file `trasee.out` must contain a string of $N \cdot M$ characters consisting of the letters `B` or `T` representing the encoding of the required path.

# Constraints and clarifications

* $1 \leq N \cdot M \leq 1\ 000\ 000$
* $1 \leq K \leq 10^{18}$
* for tests worth $5$ points, it is ensured that $N \cdot M \leq 25$
* for other tests worth $10$ points, it is ensured that $N, M \leq 15$
* for other tests worth $20$ points, it is ensured that $N = M$, prime number
* for other tests worth $35$ points, it is ensured that $N = M$
* for all tests, there is a solution
* Train and Bus are always in the same cell

# Example 1

`trasee.in`
```
2 2 2
```

`trasee.out`
```
TBTB
```

# Example 2

`trasee.in`
```
1 6 1
```

`trasee.out`
```
BBBBBB
