At the beginning of the school year, an informatics teacher received the list of grades of the $N$ students from the 9th grade class they will be working with in the lab. These are natural numbers greater than or equal to $3$. To better learn informatics, the students will be divided into study groups such that, for each group, all the grades of the students in the group are divisible by the smallest grade of a student in that group. A group can also consist of a single student.

For example:

* a group can contain students with grades $5$, $10$; because $5$ is the minimum grade in the group, and $10$ is divisible by $5$;
* a group CANNOT contain students with grades $3$, $7$; because $3$ is the minimum grade in the group, and $7$ is not divisible by $3$.

# Task

Write a program that reads the number of students and their grades and determines the minimum number of groups in which the students can be divided according to the specified rule.

# Input data
The input file `aranjare.in` contains:
* The first line contains a natural number, $N$, representing the number of students;
* The second line contains two natural numbers $\\text{nota}[1]$ and $\\text{nota}[2]$, representing the grades of the first two students;
* The next grades will be generated using the formula: $\\text{nota}[i] = (17 \\cdot \\text{nota}[i - 2] + 35 \\cdot \\text{nota}[i - 1]) \\text{ mod } 666\\ 013 + 3$

# Output data
The output file `aranjare.out` will contain a natural number $G$, representing the minimum number of groups that can be formed.

# Constraints and clarifications
* $1 \\leq N \\leq 2\\ 000\\ 000$
* $3 \\leq \\text{nota}[1], \\text{nota}[2] \\leq 500\\ 000$
* For tests worth $40$ points, $N \\leq 1\\ 000$.
* For other tests worth $40$ points, $N \\leq 100\\ 000$.

# Example 1

`aranjare.in`
```
6
3 7
```

`aranjare.out`
```
4
```

## Explanation

The students' grades are: $3$, $7$, $299$, $10587$, $375631$, $6807$.

These can be divided into $4$ groups:
1) $[3, 10587, 6807]$
1) $[7]$
1) $[299]$
1) $[375631]$

# Example 2

`aranjare.in`
```
11
3 10
```

`aranjare.out`
```
8
```

## Explanation

The students' grades are: $3$, $10$, $404$, $14313$, $507826$, $34883$, $529768$, $486530$, $60102$, $384388$, $489044$.

These can be divided into $8$ groups:
1) $[3, 14313, 60102]$
1) $[10, 486530]$
1) $[404]$
1) $[34883]$
1) $[384388]$
1) $[489044]$
1) $[507826]$
1) $[529768]$