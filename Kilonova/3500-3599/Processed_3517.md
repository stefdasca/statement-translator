**The difference between the Easy and Hard versions of the problem is that in the Easy version, the numbers on the notes received by the students cannot be equal, with each student receiving exactly one gift.**

# Task
A group of $N$ students from class 11 Pro Max $(2 \leq N \leq 10^6)$ gathered to organize Secret Santa.

The students are numbered from $1$ to $N$, each receiving a unique number so that there are no two students who receive the same number. Each student $i$ receives a note containing a number $a[i]$, representing the number of the student to whom they have to buy a gift. There are no two students with the same note, meaning that for every pair of students $i, j$ with $i \neq j$, we have $a[i] \neq a[j]$.

The students want to find out the largest group of students who can go together to buy gifts, such that there are no two students $i$ and $j$ in the group for which $a[i] = j$.

# Input data
The first line contains the natural number $2 \leq N \leq 10^6$.
The second line contains $N$ natural numbers $(1 \leq i, a[i] \leq N)$, where $a[i] \neq i$, representing the notes received by the students of class 11 Pro Max.

# Output data
The first line should contain a single natural number, representing the maximum number of students that can form a group.

# Constraints and clarifications

* $2 \leq N \leq 10^6$

|#| Score |        Constraints                                   | 
|-|---------|------------------------------------------------------|
|0|   0     | Examples                                              |
|1|   15    | $N \le 20$                                           |
|2|   26    | $N \le 1000$                                         |
|3|   59    | without additional constraints                         |

# Example

`stdin`
```
4
3 4 2 1
```

`stdout`
```
2
