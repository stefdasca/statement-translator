The Free Dacians hid their treasure in one of the $N$ rooms of the fortress. Each room is guarded by a loyal servant. You have infiltrated the fortress with the goal of finding the treasure, so you start knocking on doors.

If you knock on door $i$, the servant will tell you if the treasure is in a room to the left of room $i$, to the right of room $i$, or in room $i$. The servant is a good person, but a small gratuity will help him remember better where the treasure is, so you will voluntarily reward him with $2^{P_i}$ kosons. Since you want to offer a unique experience to each servant, the values of $P_i$ will form a permutation of the set $\{1, \dots, N\}$.

To make sure everything goes smoothly, you imagine $Q$ scenarios such as: "If the treasure is in the range of rooms $[l, r]$, what would be the minimum number of kosons you will give to the servants, in the worst case, to find the treasure?". Since the answer can be very large, the remainder of its division by $10^9 + 7$ is required.

# Input data

The first line will contain the numbers $N$ and $Q$. The next line will contain $N$ distinct non-zero natural numbers. The following $Q$ lines will each contain two numbers $l_i$, $r_i$ representing scenario $i$.

# Output data

Print $Q$ lines, on line $i$ print the answer for the $i$-th scenario, modulo $10^9 + 7$.

# Constraints
* $1 \leq N, Q \leq 200\ 000$
* $1 \leq P_i \leq N$
* The array $P$ is a permutation.
* $1 \leq l_i \leq r_i \leq N$

## Subtask 1 (3 points)
* $1 \leq N, Q \leq 50$

## Subtask 2 (6 points)
* $1 \leq N, Q \leq 200$

## Subtask 3 (23 points)
* $1 \leq N, Q \leq 1\ 000$

## Subtask 4 (52 points)
* $1 \leq Q \leq 100$

## Subtask 5 (16 points)
* No additional restrictions

# Example
`stdin`
```
8 3
3 5 8 1 6 7 2 4 
2 7
5 6
3 8
```
`stdout`
```
70
64
68
```

`stdin`
```
10 3
2 8 3 9 7 10 5 6 4 1
1 10
6 6
4 5
```
`stdout`
```
168
0
128
```