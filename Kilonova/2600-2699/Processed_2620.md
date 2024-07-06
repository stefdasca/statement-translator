In a classroom, there are $N$ students numbered from $1$ to $N$. These students can make either red objects or white objects.
Each student has a maximum limit of red and white objects they can create. The student with number $i$ can make a maximum of $a_i$ red objects and a maximum of $b_i$ white objects.
If a student makes more red objects than another student, they also make more white objects than that other student. Therefore, if $a_i \geq a_j$, then $b_i \geq b_j \ \forall \ i, j \in \{1, 2, \dots , N\}$.
To increase the number of objects made, students can choose to form a group. Two students agree to be part of a group and work together only if the absolute difference between their numbers is less than the number of students in the group. For example, students $1, 2, 3, 4$ can form a group, but students $1, 2, 3, 5$ cannot. Moreover, all students in the group will make the same number of objects. If one student in the group makes $5$ objects in total, then all students will each make $5$ objects in total.

# Task

Determine the maximum number of objects that can be made by a group of students if the students decide to make objects together, in a group.

# Input data

The first line of the input file `confectii.in` contains the natural number $N$, which signifies the number of students. The next $N$ lines contain two numbers, $a_i$ and $b_i$, representing the maximum number of red and white objects, respectively, that the student with number $i$ can make.

# Output data

The first line of the output file `confectii.out` must contain a single natural number, the maximum number of objects that can be made.

# Constraints and clarifications

* $1 \leq N \leq 10^6$
* $1 \leq a_i, \ b_i \leq 10^9$
* For 40% of the tests: $b_i = 0 \ \forall \ i \ \in \{1, 2, \dots, N\}$

# Example

`confectii.in`
```
5
10 12
30 35
50 59
20 18
40 37
```

`confectii.out`
```
152
```

## Explanation

Students $2, 3, 4, 5$ each make $20$ red objects and $18$ white objects.