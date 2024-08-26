# Reactor

A reactor contains a circular particle acceleration tunnel made up of $N$ sectors numbered counterclockwise from $1$ to $N$. In each sector, there is initially one particle. Each particle has its own rotation speed measured by the number of sectors traversed counterclockwise in one second. When the reactor is started, all particles begin to rotate counterclockwise with their respective speeds. After each second, if two or more particles arrive in the same sector, they fuse. As a result of the fusion, a single particle is formed whose speed will be the sum of the speeds of the particles that fused.

## Task

Write a program that, for given initial speeds of the $N$ particles, answers $Q$ questions of the form "What is the speed of the particle located in sector $S$ $T$ seconds after the reactor is started?". If there is no particle in sector $S$ after $T$ seconds, the program should print $0$.

## Input data

The input file `reactor.in` contains the number $N$ of sectors on the first line. The second line will contain $N$ non-null natural numbers, $v_1, v_2, \dots, v_N$ separated by spaces representing the initial speeds of the $N$ particles. The third line will contain a single number $Q$ - the number of questions. The next $Q$ lines will each contain two numbers $S$ and $T$ separated by spaces representing the sector and the second corresponding to a question.

## Output data

The output file `reactor.out` will contain $Q$ lines. Each line will contain a number representing the answer to the corresponding question from the input file.

## Constraints and clarifications

$1 \leq N \leq 100$

$1 \leq Q \leq 100000$

$1 \leq S \leq N$ for each question.

$1 \leq T \leq 1000000000$ for each question.

The initial speeds of the particles are non-null natural numbers and do not exceed $40000$.

## Example

`reactor.in`

```
3
3 1 1
2
1 1
3 2
```

`reactor.out`

```
4
0
```

## Explanation

After one second, the particle in sector $1$ traverses $3$ sectors and returns to sector $1$, the particle in sector $2$ traverses $1$ sector and arrives at sector $3$, and the particle in sector $3$ traverses $1$ sector and arrives at sector $1$. It can be observed that the first and last particles fuse in sector $1$, thus forming a single particle with speed $4$. Thus, the answer to the first question is that in sector $1$ after one second, there is a particle with speed $4$. After another second, the particle in sector $1$ traverses $4$ sectors and arrives at sector $2$ while the particle in sector $3$ traverses one sector and arrives at sector $1$. No fusions occur. Thus, after $2$ seconds, there is no particle in sector $3$, so the answer to the second question is $0$.