At a software company, work is being done on a large project. The project consists of executing $n$ ($n \in \N$) development phases, numbered with the numbers $1, 2, ..., n$. Some phases can be executed in parallel (at the same time), but the execution of other phases cannot start until the execution of certain phases is completed.

# Task
Write a program that determines:
a) the minimum time $t$ in which the project can be completed
b) for each phase $k$ ($k \in \{1, 2, ..., n\}$), the earliest time $c_k$ at which phase $k$ can start, and the latest time $d_k$ at which phase $k$ can start, without affecting the total duration of the project execution.

# Input data
The input file `pm.in` contains:
- the first line contains a natural number $n$, representing the number of phases of the project
- the second line contains $n$ natural numbers, separated by a space, representing the time required to complete each phase  
- on each line $k$ of the next $n$ lines, a natural number $m_k$ and a sequence $a$ consisting of $m_k$ natural numbers: $a_1, a_2, ..., a_{m_k}$, the $m_{k+1}$ numbers in the line being separated by a space, $m_k$ representing the number of phases that must be completed before the start of phase $k$, and the numbers in the sequence $a$ representing the order numbers of the phases that must be completed before the start of phase $k$.

# Output data
The output file `pm.out` will contain $n + 1$ lines. The first line will contain the natural number $t$, and on each line $k$ of the next $n$ lines, the two natural numbers $c_k$ and $d_k$, separated by a space, will be written.

# Constraints and clarifications
* $0 \leq n \leq 100$; $n \in \N$
* The time required to complete the execution of any phase will not exceed $1\ 000\ 000$
* It is considered that the project execution starts at time $0$
* There will be no circular dependencies (the project can always be completed)
* For solving task a), $40\%$ of the score is awarded, and for task b), $30\%$ for the first value and $30\%$ for the second value.

# Example

`pm.in`
```
7
2 3 5 3 3 3 2
0
0
1 2
1 1
1 1
3 3 4 5
1 3
```

`pm.out`
```
11
0 3
0 0
3 3
2 5
2 5
8 8
8 9
```