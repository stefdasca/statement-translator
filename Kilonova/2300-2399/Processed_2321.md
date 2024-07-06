Liisa is playing with numbers. She writes several numbers on a piece of paper. She gazes at them for a long time and then gets the idea to add after each even digit, of each number, half of that digit. She calls these numbers, *result numbers*. To each *result number*, she attaches a number called *image number*, which she constructs using the following algorithm: she associates with the *result number* an array that contains the count of each digit in the *result number*, from digit $0$ to digit $9$. Then she constructs, using the occurrences array, a new number, in which the unit's place digit is the remainder of the division by $10$ of the highest digit occurrence in the *result number*, the tens place digit will be the remainder of the division by $10$ of the next highest digit occurrence in the *result number*, and so on until the digits of the *result number* are exhausted. This number is called by Liisa, the *image number* of the *result number*. When she finishes her task, she decides to make a small computer science problem out of this game, which she will give to her sister to solve, given that her sister is preparing for the upcoming informatics olympiad.

# Task

Knowing the number $N$ of numbers and the numbers written initially by Liisa on the paper, write a program that solves the following two tasks:
1. Determine the *result numbers* obtained by Liisa for the $N$ numbers.
2. Determine the largest among the *image numbers* obtained and its occurrence in the sequence of the $N$ *image numbers*.

# Input data

The input file `cifre.in` contains on the first line two natural numbers, separated by a space, $C$ and $N$, which represent the task that needs to be solved ($1$ or $2$), respectively the number of numbers written by Liisa on the paper. The second line of the file contains $N$ natural and non-zero numbers, separated by spaces, that represent the numbers written by Liisa on the paper.

# Output data

For task $1$, the output file `cifre.out` will have a single line that contains $N$ natural numbers, separated by spaces, representing the *result numbers* obtained.

If the task is $2$, the output file `cifre.out` will contain two natural numbers, separated by a space, representing the largest among the *image numbers* obtained and its occurrence in the sequence of the $N$ *image numbers*.

# Constraints and clarifications
* $1 \leq C \leq 2$
* $1 \leq N \leq 1 \ 000$
* The numbers in the input file are non-zero and have a maximum of $9$ digits.
* The numbers written in the output file will have at most $18$ digits.
* Correctly solving the first task yields $40$ points, while correctly solving the second task yields $50$ points.

# Example 1

`cifre.in`
```
1 1
7458
```

`cifre.out`
```
742584
```

## Explanation

After each even digit of the number in the sequence, a digit equal to half of it is inserted, resulting in the *result number*.

# Example 2

`cifre.in`
```
2 5
18442 4128 4289 7805609 5087069
```

`cifre.out`
```
41111111 2
```

## Explanation

It is observed that from the sequence of $n$ numbers, the largest *image number* is determined to be $41111111$ and there are two *result numbers* that yield this *image number*, as follows: for the number $7805609$, the *result number* is $78400563009$. The *image number* attached to it is $41111111$. For the number $5087069$, the *result number* is $50084700639$. The *image number* attached to it is $41111111$.