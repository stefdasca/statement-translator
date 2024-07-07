
A natural number $N$ and a sequence of $N$ natural numbers $a_1, a_2, \dots, a_n$ are read. The numbers in the sequence do not contain the digit $0$. Starting from the first number in the sequence to the last, the following modifications will be made:

* If the last digit of a number is equal to the first digit of the next number in the sequence, the two numbers merge, with the second number attaching to the first. This newly formed number is transformed by keeping each digit only once: the leftmost occurrence of the digit is kept, subsequent occurrences are eliminated. For example, we can merge the numbers $21245$ and $51278$ resulting in the number $2124551278$. Taking the digits only once results in $214578$. The newly formed number can then be merged with the next number, and so on.
* If the last digit of a number is not equal to the first digit of the next number in the sequence, the two numbers do not merge, but the first number of the two will be transformed by keeping each digit only once: the leftmost occurrence of the digit is kept, subsequent occurrences are eliminated.

# Task

Given the $N$ numbers in the sequence, determine:

* How many numbers in the original sequence do not need transformation (contain only distinct digits)?
* How many numbers will the sequence contain after performing all the union operations?
* What is the maximum number of digits of a number in the new sequence and how many numbers have this maximum number of digits?

# Input data

The input file `siruri.in` contains on the first line a natural number $c$ ($1, 2$ or $3$). The second line contains a non-zero natural number $N$. The third line contains $N$ natural numbers separated by a space representing the initial sequence.

# Output data

In the output file `siruri.out` will contain depending on the given task:

* if $c = 1$, print on the first line the number of numbers that do not need transformation
* if $c = 2$, print on the first line the number of numbers in the sequence after performing all union operations
* if $c = 3$, print on the first line two numbers separated by a single space, representing the maximum number of digits of a number after performing the union operations, and the number of such numbers with the maximum number of digits

# Constraints and clarifications

* $c \in \{1, 2, 3\}$
* $1 \leq N \leq 100 \ 000$
* $1 \leq a_i \leq 1 \ 000 \ 000 \ 000$
* $a_i$ contains only non-zero digits
* For $18$ points, $c = 1$
* For $40$ points, $c = 2$
* For $42$ points, $c = 3$

# Example 1

`siruri.in`
```
1
8
21245 51278 869 33447 723 397897 545786 6783221
```

`siruri.out`
```
3
```

## Explanation

The task is $1$. There are $8$ numbers in the sequence, of which only $3$ have distinct digits: [$51278, 869, 723$].

# Example 2

`siruri.in`
```
2
8
21245 51278 869 33447 723 397897 545786 6783221
```

`siruri.out`
```
4
```

## Explanation

The task is $2$. There are $8$ numbers in the sequence, after transformations the sequence will look like: [$21457869, 3472, 3978, 54786321$].

# Example 3

`siruri.in`
```
3
9
21245 51278 869 33447 723 397897 545786 6783221 235788946
```

`siruri.out`
```
8 3
```

## Explanation

The task is $3$. There are $9$ numbers in the sequence, after transformations the sequence will look like: [$21457869, 3472, 3978, 54786321, 23578946$]. The maximum number of digits of a number in the new sequence is $8$ and there are $3$ numbers in the new sequence that have $8$ digits: [$21457869, 54786321, 23578946$].
