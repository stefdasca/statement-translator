# Task

A group of $N$ students from class 11 Pro Max gathered to organize Secret Santa. The students are numbered, each receiving a number $i$ such that no two students receive the same number. Each student $i$ receives a slip with a number $a[i]$, indicating the student to whom they must buy a gift. There may be two students who have the same student on their slips. The students of class 11 Pro Max want to know the largest group of students who can go gift shopping under the condition that there is no student in the group whose designated gift recipient is also in the group with them, formally there should be no two students $i$, $j$ such that $a[i] = j$.

# Input data

The first line contains the natural number $2 \leq N \leq 10^6$.
The second line contains $N$ natural numbers $(1 \leq i, a[i] \leq N)$, where $a[i] \neq i$, representing the slips received by the students of class 11 Pro Max.

# Output data

The first line will contain a single natural number, representing the maximum number of students that can form a group.

# Constraints and clarifications

* $2 \leq N \leq 10^6$

|#| Score |        Constraints                                  | 
|-|-------|------------------------------------------------------|
|0|   0   | Examples                                              |
|1|   14  | $N \le 20$                                           |
|2|   39  | $N \le 1000$                                         |
|3|   47  | without additional constraints                       |

# Example

`stdin`
```
4
2 1 1 3
```

`stdout`
```
2
