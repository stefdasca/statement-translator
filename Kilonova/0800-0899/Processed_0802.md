Maria loves prime numbers and the powers of prime numbers. Starting from a prime number $p$, she constructs new numbers, each constructed number being a product of the form $p^y$ ($y \in \mathbb{N}$, $y \neq 0$) or $q \cdot p^m$, $m \in \mathbb{N}$ and $q$ a prime number, calling them $p$-prime numbers. For example, the numbers $2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17$ are the first $14$ $2$-prime numbers because $2 = 2^1$, $3 = 3 \cdot 2^0$, $4 = 2^2$, $5 = 5 \cdot 2^0$, $6 = 3 \cdot 2^1$, $7 = 7 \cdot 2^0$, $8 = 2^3$, $10 = 5 \cdot 2^1$, $11 = 11 \cdot 2^0$, $12 = 3 \cdot 2^2$, $13 = 13 \cdot 2^0$, $14 = 7 \cdot 2^1$, $16 = 2^4$, $17 = 17 \cdot 2^0$.

One day Maria found a sheet of paper, on which there was a sequence consisting of $n$ non-zero natural numbers. Since besides $p$-prime numbers she is also passionate about subarrays, she asked herself the following question: how many subarrays are on the sheet with the following properties:

* contain exactly $k$ $p$-prime numbers;
* start and end with a $p$-prime number.

In addition, Maria wants to know the starting and ending positions for each subarray discovered, relative to the sequence written on the sheet of paper.

# Task

Write a program that reads multiple data sets, each set being composed of numbers $n, p, k$, with the meanings from the statement, and the sequence with $n$ elements $a_1, a_2, a_3, \dots, a_n$, Maria's numbers. The program will determine for each set of data the number of subarrays that contain exactly $k$ $p$-prime numbers, as well as the starting and ending positions of these subarrays in the sequence from the set.

# Input data

The first line of the file `secvente.in` contains the number $D$ representing the number of data sets in the file. The data sets are written in the file on successive lines. For each data set, the first line contains three natural numbers: $n$ (the number of elements on the sheet), $p$ and $k$ (with the meaning from the statement), separated by a space, and each of the following $n$ lines contains one natural number of the sequence $a_1, a_2, a_3, \dots, a_n$, the numbers from Maria's sequence.

# Output data

The file `secvente.out` will contain $D$ solutions corresponding to the $D$ data sets. For each solution, the first line will contain a number $x$ representing the number of subarrays that meet the required properties, and each of the following $x$ lines will contain two natural numbers, separated by a space, representing the starting and ending position of each subarray, lines ordered in ascending order by the starting position. If there is no such subarray in the sequence, the first line of the set will contain the value $0$.

# Constraints and clarifications

* $1 \leq D \leq 15$;
* $1 \leq k, n \leq 15\ 000$;
* $2 \leq p \leq 30\ 000$; $p$ is a natural prime number
* $1 \leq a_1, a_2, a_3, \dots, a_n \leq 30\ 000$; $a_1, a_2, a_3, \dots, a_n \in \mathbb{N}$
* Positions in the sequence are numbered from 1.
* The number $1$ is not $p$-prime.
* A subarray in a sequence is composed of elements located on consecutive positions in the given sequence.

# Example

`secvente.in`
```
2
5 3 2
7
27
4
45
1
3 5 7
3
4
5
```

`secvente.out`
```
2
1 2
2 4
0
```

## Explanation

Since $D = 2$, the input file contains two data sets.
First data set: $n = 5$, $p = 3$, $k = 2$ and $a = (7, 27, 4, 45, 1)$.
The sequence in this set contains the following $3$-prime numbers:
$a_1 = 7$ (prime number), $a_2 = 27 = 3^3$ (power of $3$) and $a_4 = 45$ = $5 \cdot 3^2$ (prime number multiplied by a power of $3$).

In the sequence, there are two subarrays with two $3$-prime numbers each: $a_1, a_2$ respectively $a_2, a_3, a_4$.
On the first line of the output file, the value $2$ will be written, and on the next two lines, the starting and ending positions of the two determined subarrays.

The sequence a in the second data set, $n = 3$, $p = 5$, $k = 7$, $a = (3, 4, 5)$, does not contain any subarray with the required property. Thus, in the output file, on the fourth line, the value $0$ will be written.