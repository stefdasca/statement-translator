Here is the translated competitive programming problem statement in English:

During the gym class, the $N$ students from the class lined up in a single row in front of the teacher. They did not try to arrange themselves by height, knowing that the teacher has his own method of ordering, which he applies at the beginning of each lesson. The teacher chooses a student, whom he sends to one of the two ends of the row. This process is repeated until the line of students is sorted in ascending order by height. The children thought to help the teacher perfect his method so that the number of students who will be moved by this process to one end or the other of the line is minimized.

# Task

Knowing the number of students, their heights, and their initial positions in the row, determine the minimum number of moves the gym teacher must apply to order the row of students in ascending order by height.

# Input data

The input file `sport.in` contains on the first line the natural number $N$ representing the number of children. The second line contains $N$ **distinct** natural numbers: $H_1$, $H_2$, $\\dots$, $H_N$, separated by a single space. The $i$-th number on the line represents the height of the child who is in position $i$ before any moving operations.

# Output data

In the output file `sport.out`, print on the first line a natural number $M$, representing the minimum number of moves the teacher can make to sort the row of students in ascending order by height.

# Constraints and clarifications

* $1 < N \leq 1 \ 000$
* $1 \leq H_i \leq 10 \ 000$

# Example 1

`sport.in`
```
4
2 1 3 5 
```

`sport.out`
```
1
```

## Explanation

The teacher moves the student of height $1$ to the left end: $1 \\ 2 \\ 3 \\ 5$

# Example 2

`sport.in`
```
3
3 2 1 
```

`sport.out`
```
2
```

## Explanation

The teacher has several options with a minimum of $2$ moves. One of them is:

Move the student of height $1$ to the left end: $1 \\ 3 \\ 2$
Move the student of height $3$ to the right end: $1 \\ 2 \\ 3$

# Example 3

`sport.in`
```
5
3 7 2 6 9
```

`sport.out`
```
3
```

## Explanation

A minimum of $3$ moves. One option is:

Move the student of height $7$ to the right end: $3 \\ 2 \\ 6 \\ 9 \\ 7$
Move the student of height $2$ to the left end: $2 \\ 3 \\ 6 \\ 9 \\ 7$
Move the student of height $9$ to the right end: $2 \\ 3 \\ 6 \\ 7 \\ 9$