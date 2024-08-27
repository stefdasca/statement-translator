# Hanoig

Consider 3 rods (denoted $A$, $B$, $C$). On rod $A$ there are $n$ disks of $k$ distinct sizes $d_1 > d_2 > \dots > d_k$. Specifically, there are $m_1$ disks of diameter $d_1$, $m_2$ disks of diameter $d_2$, $\dots$, $m_k$ disks of diameter $d_k$. Obviously, $m_1 + m_2 + \dots + m_k = n$. The disks are initially placed on rod $A$ in descending order of size, when viewed from the base to the top (so at the base are the $m_1$ disks of diameter $d_1$, then follow the $m_2$ disks of diameter $d_2$, $\dots$). In one move, a single disk can be moved from one rod to another, but a disk of larger diameter will never be placed over a disk with a smaller diameter. The goal is to move all the disks from rod $A$ to rod $B$, always maintaining the descending order of sizes. Rod $C$ can be used as an auxiliary rod.

## Task

Write a program to determine the minimum number of moves required to transfer the $n$ disks from rod $A$ to rod $B$.

## Input data

The input file `hanoig.in` contains on the first line the natural number $k$, with the meaning described above. The second line contains $k$ natural numbers separated by spaces $m_1$ $m_2$ $\dots$ $m_k$. 

## Output data

The output file `hanoig.out` will contain a single line which will contain the minimum number of moves required to move the $n = m_1 + m_2 + \dots + m_k$ disks from rod $A$ to rod $B$.

## Constraints

$0 < k \leq 1000$

$0 < m_i \leq 1000$, for any $i = 1 , 2 , \dots , k$

The disks are not numbered, so the disks of the same size are considered identical.

## Example

`hanoig.in` 
```
2 
2 3 
```

`hanoig.out` 
```
8 
```