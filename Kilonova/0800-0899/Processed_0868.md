# Task

The preparatory class students are playing with numbers in math. The teacher has a bag full of tokens, each with a digit written on it. Each student picked multiple tokens from the bag to form a number. To make things more interesting, the students grouped in pairs. The teacher gave each pair of students a box to put their tokens together. For example, if one student from a team formed the number 5137131 and the other student formed the number $6551813$, then the team’s box will contain $5$ tokens with the digit $1$, $3$ tokens with the digit $3$ and $5$, and $1$ token with the digits $6, 7$, and $8$ respectively.

Only Andrei was upset because the class's number of students was odd, and he didn’t have a partner, so he didn’t pick any tokens. The teacher told him: "Pick a team from whose box you can take some tokens, but make sure that each of the two students can still form their numbers from the remaining tokens, and you can form a **non-zero** number with the extracted tokens!" But since Andrei was not satisfied with just a few tokens, he wanted to choose the team from whose box he could form the highest value number using the extracted tokens.

# Task

Write a program that reads the number $N$ of boxes and the numbers formed by the students of each pair and determines:

1. The number of boxes from which Andrei can take tokens respecting the condition set by the teacher;
2. What is the largest non-zero number that Andrei can form respecting the same condition.

# Input data

The file `cifre.in` contains on the first line the natural number $P$ representing the task from the problem that needs to be solved. The second line contains the natural number $N$, and the following $N$ lines contain two natural numbers separated by a space representing the numbers formed by the students of each pair.

# Output data

If the value of $P$ is $1$, the output file `cifre.out` will contain on the first line a natural number representing the solution to the first task, specifically the number of boxes from which Andrei can take tokens.

If the value of $P$ is $2$, the output file `cifre.out` will contain on the first line a natural number representing the solution to the second task, specifically the maximum number that Andrei can form.

# Constraints and clarifications

* $0 < N \leq 10\ 000$
* $1 \leq$ the number of tokens of each student $\leq 9$;
* $0 \leq$ digit written on any token $\leq 9$;
* It is guaranteed that there is at least one box from which Andrei can form a non-zero number
* For the correct solution of each task, $50$ points are awarded

# Example 1

`cifre.in`
```
1
3
1010 2000
12 34
1515 552
```

`cifre.out`
```
1
```

## Explanation

With the tokens extracted from the first box, Andrei cannot form a number different from $0$. From the second box, Andrei cannot take tokens such that the two students can still form the numbers $12$ and $34$. Andrei can extract tokens only from the third box (two tokens with the digit $5$).

# Example 2

`cifre.in`
```
2
5
16815 38861
12 385
5137131 6551813
15033 11583
4704 240
```

`cifre.out`
```
5311
```

## Explanation

The maximum number that Andrei can form is $5311$ and it is obtained from the third box.