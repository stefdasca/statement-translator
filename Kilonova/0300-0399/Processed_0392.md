Here is the translated competitive programming problem statement:

---

Maria is a first-year student at the Faculty of Computer Science and has received a list of $N$ problems, numbered from $1$ to $N$, that she needs to solve for the algorithms course, with each problem taking exactly one unit of time to solve. Because the professor wants to test the students' ability to make the best choices, for each problem, he has set the number of credits ($C_i$) the student will receive if they solve problem $i$, and also a limited number of time units ($T_i$) by which the problem can be solved.

# Task
Knowing the number of problems, the number of credits for each problem, and the time limit for solving each problem, write an algorithm to determine the `maximum number` of credits Maria can obtain.

# Input data
The first line of the input file `credits.in` contains a natural number $N$, representing the number of problems on the list.  
The following $N$ lines of the input file will contain the data about each problem, with line $i+1$ containing $2$ natural numbers $C_i$ and $T_i$, representing the number of credits, respectively the time limit for problem $i$.

# Output data
The output file `credits.out` will contain a single natural number, representing the maximum number of credits Maria can obtain.

# Constraints and clarifications

* $2 \\leq n \\leq 10 \\ 000$
* $2 \\leq C_i \\leq 1 \\ 000$
* $1 \\leq T_i \\leq 10 \\ 000$

# Example

`credits.in`
```
4
10 3
7 5
8 1
2 1
```

`credits.out`
```
25
```

## Explanation

Maria chooses to solve problem $3$, giving up on problem $4$ because it has fewer credits and the same time limit as problem $3$. After that, she will solve problems $1$ and $2$, gaining a total of $25$ credits.

