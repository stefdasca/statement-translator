Ionel has $N$ cards. Each card has two numbers written on it (a number, $s$, on the left side, and another number, $d$, on the right side). He has arranged the cards in a sequence, glued together so that the number on the right side of the first card is glued to the number on the left side of the second card, the number on the right side of the second card is glued to the number on the left side of the third card, and so on. We say that two adjacent cards "match" if the number on the right side of the first card is equal to the number on the left side of the second card. Ionel observes that there are pairs of adjacent cards that "match" and even sequences of multiple adjacent cards where the first "matches" with the second, the second "matches" with the third, and so on.

# Task
Write a program that reads the number $N$ of cards, the numbers written on each card, and determines:
1) The number of pairs of cards that "match."
2) The number of cards in the longest sequence where every two adjacent cards "match."
3) The number of sequences with a maximum number of cards that "match."

# Input data
The input file `cartonase.in` contains only non-zero natural numbers:
- The first line contains the number $C$ which can only have the values $1$, $2$, or $3$ and represents the task to be solved. The second line of the file contains the natural number $N$, with the meaning given in the statement.
- On each of the following $N$ lines, there are, in this order, two natural numbers $s$ and $d$, separated by a space, with the meaning given in the statement for a card. The pairs of numbers are given in the order in which the corresponding cards appear in Ionel's sequence.

# Output data
The output file `cartonase.out` will contain on the first line a natural number representing the answer to the specified task.

# Constraints and clarifications
- $1 \leq N \leq 500$
- $1 \leq s \leq 10\ 000$
- $1 \leq d \leq 10\ 000$
- Each task is worth 30 points.

# Example 1
`cartonase.in`
```
1
5
2 10
10 5
10 2
2 10
37 5
```
`cartonase.out`
```
2
```
## Explanation
We solve the first task.
There are $2$ pairs of adjacent cards that "match":
- the first with the second: $(2, 10)$ and $(10, 5)$;
- the third with the fourth: $(10, 2)$ and $(2, 10)$.

# Example 2
`cartonase.in`
```
2
5
2 10
10 5
5 2
2 10
37 5
```
`cartonase.out`
```
4
```
## Explanation
We solve the second task.
The first four cards form a sequence where every two adjacent cards "match":
- the first card with the second: $(2, 10)$ and $(10, 5)$;
- the second card with the third: $(10, 5)$ and $(5, 2)$;
- the third card with the fourth: $(5, 2)$ and $(2, 10)$.

# Example 3
`cartonase.in`
```
3
6
2 10
10 5
2 8
6 2
2 10
37 5
```
`cartonase.out`
```
2
```
## Explanation
We solve the third task.
There are at most two adjacent cards that "match."
There are two sequences of two matching cards each: the first and second cards and the fourth and fifth cards.