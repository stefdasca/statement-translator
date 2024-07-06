Ana and Bogdan have invented the game "Compar". Ana writes a sequence consisting of $N$ distinct natural numbers ranging from $1$ to $N$ on the board, then compares every two neighboring numbers in the sequence by writing between them the sign `<` or the sign `>`, as appropriate.

For example, if the sequence on the board is $6 \\ 4 \\ 2 \\ 1 \\ 3 \\ 5$, after comparing the neighboring elements and inserting the signs in the sequence, Ana gets: $6>4>2>1<3<5$.
Then Ana erases the $N$ elements of the sequence and keeps only the signs, as follows: `>>><<`.
In the end, Ana shows the signs string to Bogdan and asks him to reconstruct the initial sequence of natural numbers written on the board.

# Task

Knowing the signs string constructed by Ana, write a program to help Bogdan reconstruct the initial sequence of distinct natural numbers written on the board.

# Input data

The input file `compar.in` contains a sequence of characters from the set $\\{$`<`$,$ `>`$\\}$, representing the signs string obtained by Ana after comparing neighboring elements from the initial sequence.

# Output data

The output file `compar.out` will contain in the first line the natural number $N$, representing the length of the initial sequence. The second line will contain $N$ distinct natural numbers ranging from $1$ to $N$, separated by a space, representing the elements of the initial sequence, reconstructed based on the signs from the input file.

# Constraints and clarifications

* $1 < N \leq 100\ 000$;
* If there are multiple solutions, print any of them.
* For the correct determination of the sequence's length, $10\\%$ of the score per test is awarded.

# Example

`compar.in`
```
>>><<
```

`compar.out`
```
6
6 4 2 1 3 5
```

## Explanation

$6>4>2>1<3<5$
There are other possible solutions; this is just one of them.