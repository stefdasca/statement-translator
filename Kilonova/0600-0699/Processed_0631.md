During the Revolution of 1989, the building of the Central University Library of Bucharest was set on fire and thus many rare books with great historical value were lost. From the fire, only $N$ books were saved, and each of them could be identified by a unique code, represented by a natural number with a maximum of $18$ digits. Trying to arrange them in order on the shelves, the librarian decides to place only books with consecutive natural number codes next to each other on each shelf. 

# Task
What is the minimum number of shelves needed to arrange the $N$ books and what is the largest number of books placed on a single shelf?

# Input data
The first line of the input file contains a natural number $N$ representing the number of books. Each of the following $N$ lines contains a natural number representing the code of one book.

# Output data
The first line of the output file contains the minimum number of shelves required for arranging the books and the second line contains a natural number representing the largest number of books that can be arranged on a shelf.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000$
* $1 \leq$ value of a code $\leq 10^{18}$
* The $N$ codes are distinct

# Example

`biblioteca.in`
```
11
4
2
200
5
6
18
19
3
10
9
17
```

`biblioteca.out`
```
4
5
```

## Explanation

There are $11$ books. The minimum number of shelves on which the books can be placed is $4$. The largest number of books that can be placed on a shelf is $5$.